import cv2
from skimage.metrics import structural_similarity as ssim
import argparse
import imutils

# Usage: python diff.py --first first.png --second second.png

parser = argparse.ArgumentParser()
parser.add_argument("--first", required=True, help="path to first image")
parser.add_argument("--second", required=True, help="path to second image")
args = parser.parse_args()

# Resize while keeping aspect ratio, allowing upscale/downscale
def resize_to_screen(image, max_width=1080, max_height=720):
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h)  # allows upscale or downscale
    new_w = int(w * scale)
    new_h = int(h * scale)
    return cv2.resize(image, (new_w, new_h))

# Load images
imageA = cv2.imread(args.first)
imageB = cv2.imread(args.second)

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

# Threshold
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Draw bounding boxes
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Resize all for display (no distortion)
imageA_disp = resize_to_screen(imageA)
imageB_disp = resize_to_screen(imageB)
diff_disp   = resize_to_screen(diff)
thresh_disp = resize_to_screen(thresh)

# Show results
cv2.imshow("Original", imageA_disp)
cv2.imshow("Modified", imageB_disp)
cv2.imshow("Diff", diff_disp)
cv2.imshow("Thresh", thresh_disp)

cv2.waitKey(0)
