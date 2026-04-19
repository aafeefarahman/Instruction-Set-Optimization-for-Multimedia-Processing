# Instruction Set Optimization for Multimedia Processing

## Overview

This project demonstrates how optimized processing techniques significantly improve performance compared to traditional sequential methods.

It processes both images and videos using:

* Sequential (loop-based) approach
* Optimized (NumPy vectorized) approach

The execution time of both methods is measured and compared to show performance improvement.

---

## Tech Stack

* Python
* OpenCV (cv2)
* NumPy
* Matplotlib

---

## How to Run

1. Install dependencies:

```
pip install opencv-python numpy matplotlib
```

2. Keep these files in the same folder:

* `image_video_processing_optimization.py`
* `eagleeye.jpg`
* `ocean_video_fixed.mp4`

3. Run:

```
python image_video_processing_optimization.py
```

---

## Image Processing Outputs

### Original Image

This is the input image loaded into the system.
It is resized (if large) and converted from BGR to RGB format for correct display.

---

### Sharpened Image

The image after applying:

* Gaussian Blur (for noise reduction)
* Sharpening filter (to enhance edges and details)

This step improves visual quality before further processing.

---

### Sequential Processing Output

* Brightness is increased pixel-by-pixel using nested loops
* Each pixel is processed individually

**Observation:**

* Slower execution
* High computation time due to repeated operations

---

### Optimized Processing Output

* Brightness is increased using NumPy vectorized operations
* Entire image is processed at once

**Observation:**

* Extremely fast execution
* Efficient use of CPU

---

## Image Performance Graph (Bar Graph)

This graph compares execution time between:

* Sequential Processing
* Optimized Processing

**What it shows:**

* Sequential method has significantly higher execution time
* Optimized method is much faster
* Demonstrates clear performance improvement using vectorization

---

## Video Processing Outputs

### Original Video Frame

Frame extracted directly from the input video without any modification.

---

### Sequential Processed Frame

* Each pixel in the frame is processed using nested loops
* Brightness is adjusted individually

**Observation:**

* Noticeable delay
* Slower frame processing

---

### Optimized Processed Frame

* Frame processed using vectorized operations
* All pixels updated simultaneously

**Observation:**

* Smooth and fast processing
* Suitable for real-time applications

---

## Video Performance Graph (Line Graph)

This graph shows:

* X-axis → Frame Number
* Y-axis → Processing Time

**What it shows:**

**Sequential Processing:**

* Higher execution time
* Fluctuating performance

**Optimized Processing:**

* Very low execution time
* Stable and consistent

---

## Key Result

* Optimized processing is significantly faster than sequential processing
* Speedup is achieved by reducing pixel-by-pixel operations
* Demonstrates concepts like SIMD and vector processing

---

## Conclusion

This project proves that vectorized operations greatly improve performance in multimedia processing. It highlights how modern computing systems handle large data efficiently using optimized instruction execution.

---

## Feedback

Feel free to suggest improvements or enhancements.
