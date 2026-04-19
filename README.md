# Instruction Set Optimization for Multimedia Processing

## Overview

This project demonstrates how optimized processing techniques improve performance in multimedia applications. It compares traditional sequential (loop-based) processing with optimized vectorized processing using NumPy.

The project processes both images and videos, measures execution time, and visualizes performance differences using graphs.

---

## Tech Stack

* Python
* OpenCV (cv2)
* NumPy
* Matplotlib

---

## How to Run

1. Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

2. Keep these files in the same folder:

* image_video_processing_optimization.py
* eagleeye.jpg
* ocean_video_fixed.mp4

3. Run the program:

```bash
python image_video_processing_optimization.py
```

---

## Image Processing Results
<img width="971" height="400" alt="image" src="https://github.com/user-attachments/assets/5347414d-95ab-4df3-85ba-03f3ae38d5d2" />


* **Original Image**
  The input image loaded into the system before any processing.

* **Sharpened Image**
  The image after applying Gaussian blur for noise reduction and a sharpening filter to enhance edges and clarity.

* **Loop Processing (Sequential)**
  Brightness is increased pixel-by-pixel using nested loops.
  This method is slower because each pixel is processed individually.

* **Optimized Processing**
  Brightness is increased using NumPy vectorized operations.
  This method processes all pixels simultaneously, resulting in much faster execution.

---

## Image Performance Graph
<img width="578" height="458" alt="image" src="https://github.com/user-attachments/assets/761cddcb-3743-4164-aaad-86cf8b1029c1" />


This bar graph compares execution time between sequential and optimized processing
* Sequential processing takes significantly more time due to repeated pixel operations
* Optimized processing is much faster due to vectorized computation
* The graph clearly highlights the performance improvement

---

## Video Processing Results

<img width="1140" height="524" alt="image" src="https://github.com/user-attachments/assets/54b1fe6e-9c8a-4418-9968-08a91be9b91c" />


* **Original Frame**
  A frame extracted directly from the input video.

* **Sequential Processed Frame**
  Each pixel is processed individually using nested loops to adjust brightness.
  This results in slower performance and visible delay.

* **Optimized Processed Frame**
  Brightness adjustment is applied using vectorized operations.
  This results in smooth and fast processing suitable for real-time applications.

---

## Video Performance Graph
<img width="756" height="399" alt="image" src="https://github.com/user-attachments/assets/96e7b9c8-7190-4980-ac3e-f8b22db0296f" />

This line graph shows processing time per frame.
* **X-axis:** Frame number
* **Y-axis:** Execution time

**Observations:**

* Sequential processing shows higher and fluctuating execution time
* Optimized processing remains low and consistent
* Demonstrates efficiency of vectorized operations in continuous workloads

## Performance Metrics

### Image Processing Time

- **Sequential Processing Time:** ~1.72 seconds  
- **Optimized Processing Time:** ~0.0076 seconds  

### Speedup

- **Speedup Factor:** ~226× faster  

### Video Processing Time

- Sequential processing takes significantly higher time per frame  
- Optimized processing maintains very low and consistent execution time  

---

## Key Results

* Optimized processing is significantly faster than sequential processing
* High speedup is achieved using vectorization
* Efficient CPU utilization is demonstrated
* Suitable for real-time multimedia applications

---

## Conclusion

This project proves that vectorized operations drastically reduce execution time compared to traditional loop-based methods. It highlights the importance of instruction set optimization techniques such as SIMD and parallel processing in modern computing.

---

## Future Scope

* Real-time webcam processing
* GPU acceleration (CUDA/OpenCL)
* Integration with AI models
* High-resolution (4K+) processing
* Parallel computing (multithreading/multiprocessing)

---

## Feedback

Suggestions and improvements are welcome.
