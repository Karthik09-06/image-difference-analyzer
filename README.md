

# **Image Difference Analyzer**

A Python tool that compares two images using **SSIM (Structural Similarity Index)** and **OpenCV** to detect and highlight visual differences. It generates difference maps, marks changed regions, and preserves aspect ratio while displaying results. Useful for quality inspection, visual regression testing, defect detection, and before/after analysis.

---

## **Features**

* SSIM-based image comparison
* Highlights changed regions with bounding boxes
* Generates diff and threshold maps
* Resizes output to fit any screen without distortion
* Works with any image format supported by OpenCV

---

## **Installation**

### **Clone the Repository**

```bash
git clone https://github.com/Karthik09-06/image-difference-analyzer.git
cd image-difference-analyzer
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

Required packages:

* opencv-python
* scikit-image
* imutils

---

## **Usage**

```bash
python diff.py --first path/to/first_image.png --second path/to/second_image.png
```

Example:

```bash
python diff.py --first images/original.png --second images/modified.png
```

---

## **How It Works**

1. Loads the two input images
2. Converts them to grayscale
3. Computes the SSIM score and difference map
4. Thresholds the diff to isolate changed regions
5. Draws bounding boxes around differences
6. Displays all results, auto-scaled to fit a 1080p window

---

## **Output Windows**

* **Original** (with differences outlined)
* **Modified** (with differences outlined)
* **Diff map** (grayscale SSIM difference)
* **Threshold** (binary mask showing changed areas)

---

## **Use Cases**

* Visual regression testing
* Industrial quality inspection
* Before/after comparison
* Detecting image manipulation
* Automated UI testing

---
