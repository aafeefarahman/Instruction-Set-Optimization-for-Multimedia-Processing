import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
print("Processing Image...")
image = cv2.imread("eagleeye.jpg")
if image is None:
    print("Error: Image not found")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Resize if image is too large
max_size = 800
h, w = image.shape[:2]
if h > max_size or w > max_size:
    scale = max_size / max(h, w)
    image = cv2.resize(image, (int(w * scale), int(h * scale)))
# Apply blur (denoising)
denoise = cv2.GaussianBlur(image, (3, 3), 0)
# Sharpen image
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(denoise, -1, kernel)

# Sequential pixel processing
loop_image = sharpened.copy()
start = time.time()
for i in range(loop_image.shape[0]):
    for j in range(loop_image.shape[1]):
        for k in range(3):
            pixel = int(loop_image[i, j, k]) + 40
            loop_image[i, j, k] = min(255, pixel)
loop_time = time.time() - start
print("Sequential Processing Time:", loop_time)
# Optimized (vectorized) processing
start = time.time()
vector_image = np.clip(sharpened + 40, 0, 255)
vector_time = time.time() - start
print("Optimized Processing Time:", vector_time)

# Speedup calculation
speedup = loop_time / vector_time
print("Speedup Factor:", speedup)
# Display results
plt.figure(figsize=(14, 6))
plt.subplot(1, 4, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")
plt.subplot(1, 4, 2)
plt.title("Sharpened Image")
plt.imshow(sharpened)
plt.axis("off")
plt.subplot(1, 4, 3)
plt.title("Loop Processing")
plt.imshow(loop_image)
plt.axis("off")
plt.subplot(1, 4, 4)
plt.title("Optimized Processing")
plt.imshow(vector_image)
plt.axis("off")
plt.show()

# Execution time comparison (image)
methods = ["Sequential", "Optimized"]
times = [loop_time, vector_time]
plt.bar(methods, times)
plt.title("Execution Time Comparison (Image)")
plt.ylabel("Time (seconds)")
plt.xlabel("Processing Method")
plt.show()
print("\nProcessing Video...")
cap = cv2.VideoCapture("ocean_video_fixed.mp4")
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
frame_count = 0
max_frames = 50
seq_times = []
opt_times = []
frame_numbers = []
while True:
    ret, frame = cap.read()
    if not ret or frame_count >= max_frames:
        break
    frame_count += 1
    frame_numbers.append(frame_count)

    # Sequential processing
    seq_frame = frame.copy()
    start = time.time()
    for i in range(seq_frame.shape[0]):
        for j in range(seq_frame.shape[1]):
            for k in range(3):
                pixel = int(seq_frame[i, j, k]) + 30
                seq_frame[i, j, k] = min(255, pixel)
    seq_time = time.time() - start
    seq_times.append(seq_time)
   
 # Optimized processing
    start = time.time()
    opt_frame = np.clip(frame + 30, 0, 255)
    opt_time = time.time() - start
    opt_times.append(opt_time)
    # Display frames
    cv2.imshow("Original Video", frame)
    cv2.imshow("Sequential Processing", seq_frame)
    cv2.imshow("Optimized Processing", opt_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print("Video Processing Complete")

# Video performance graph
plt.figure(figsize=(10, 5))
plt.plot(frame_numbers, seq_times, label="Sequential Processing")
plt.plot(frame_numbers, opt_times, label="Optimized Processing")
plt.title("Video Frame Processing Time Comparison")
plt.xlabel("Frame Number")
plt.ylabel("Processing Time (seconds)")
plt.legend()
plt.show()
