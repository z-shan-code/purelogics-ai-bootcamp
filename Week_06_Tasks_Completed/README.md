# 👁️ Week 6 — Computer Vision: CNNs, Architectures & Object Detection

> Week 6 was a deep dive into Computer Vision — starting from the fundamentals of Convolutional Neural Networks and building up to real, practical applications: recognizing objects, drawing bounding boxes around them, and segmenting images pixel by pixel.

---

## 🧠 What This Week Covered

### 🔲 Convolutional Neural Networks (CNNs)
- Built CNNs from scratch and trained them on the MNIST dataset to understand the core building blocks of image-based deep learning: convolutional layers, pooling, and feature extraction
- Learned how CNNs automatically learn spatial hierarchies of features from raw pixel data

### 🏛️ CNN Architectures — VGGNet & ResNet
- Studied well-known, industry-standard CNN architectures — **VGGNet** and **ResNet** — and how their design choices (deeper layers, residual/skip connections) solve real training challenges like vanishing gradients
- Understood why architecture design matters as much as the training process itself in computer vision

### 🎯 Object Detection with YOLO
- Implemented object detection using **YOLOv8**, one of the fastest and most widely used real-time object detection frameworks
- Learned how to work with **bounding boxes** — detecting not just *what* is in an image, but *where* it is
- Got hands-on with the libraries and tooling that make YOLO practical to use in real projects

### ✂️ Image Segmentation with U-Net
- Implemented **U-Net**, a specialized architecture for image segmentation
- Learned the difference between classification (what's in the image), object detection (what and where, via bounding boxes), and segmentation (labeling every individual pixel)

---

## 🧠 Key Takeaways
- End-to-end understanding of the computer vision task spectrum: classification → detection → segmentation
- Practical experience with industry-standard architectures (VGG, ResNet) and modern detection frameworks (YOLOv8)
- Comfortable working with bounding box-based object detection pipelines
- Hands-on experience with U-Net, a widely used architecture in fields like medical imaging and autonomous systems

---

## 🛠️ Tech Stack
`Python` · `TensorFlow` / `PyTorch` · `YOLOv8` · `OpenCV` · `Jupyter Notebook`

## 📁 Folder Structure
```
Week_06_Tasks_Completed/
├── Week_6_Day_1_Task (3-Aug)/     → CNN fundamentals (MNIST)
├── Week_6_Day_2_Task (4-Aug)/     → CNN architectures — VGGNet & ResNet
├── Week_6_Day_3_Task (5-Aug)/     → Object detection with YOLOv8 & bounding boxes
└── Week_6_Day_4_Task (6-Aug)/     → Image segmentation with U-Net
```