# 🧠 Week 5 — Deep Learning Foundations, AutoML & Deep Learning Frameworks

> Week 5 marked the transition from classical machine learning into deep learning — understanding what's actually happening inside a neural network during training, and getting hands-on with the two frameworks that power nearly all modern AI development: TensorFlow and PyTorch.

---

## 🧠 What This Week Covered

### 🤖 AutoML
- Explored Automated Machine Learning (AutoML) — tools and techniques that automate model selection, hyperparameter tuning, and pipeline optimization
- Understood the trade-offs between building models manually vs. letting automated systems search for optimal configurations

### 🔁 Forward & Backward Pass in Neural Networks
- Went beyond just using neural networks to understanding how they actually learn:
  - **Forward pass** — how input data flows through a network's layers to produce a prediction
  - **Backward pass (backpropagation)** — how the network calculates error and updates its weights through gradient computation
- Built a genuine intuition for what's happening mathematically during model training, not just the code that triggers it

### 🔥 TensorFlow & PyTorch
- Hands-on practice with both major deep learning frameworks side-by-side
- Learned the core building blocks in each: tensors, layers, model definition, and training loops
- Understood key differences in how TensorFlow and PyTorch approach model building — valuable since real-world teams use both depending on the project

### 🏗️ Deep Neural Networks
- Built deep neural networks (DNNs) from the ground up, applying the forward/backward pass concepts in practice
- Practiced structuring multi-layer networks and training them on real data

### ⚡ GPU-Accelerated Training
- Explored running deep learning workloads on GPU to understand the performance difference in training larger neural networks

---

## 🧠 Key Takeaways
- Solid conceptual understanding of how neural networks actually learn (forward + backward pass), not just how to call `.fit()`
- Practical, comparative experience with both TensorFlow and PyTorch
- Exposure to AutoML as a tool for accelerating the model-building process
- First experience with GPU-accelerated training, setting up the foundation for the CNNs and larger architectures covered in later weeks

---

## 🛠️ Tech Stack
`Python` · `TensorFlow` · `PyTorch` · `AutoML` · `NumPy` · `Jupyter Notebook`

## 📁 Folder Structure
```
Week_05_Tasks_Completed/
├── Week_5_Day_1_Tasks_27_July/     → AutoML
├── Week_5_Day_2_Tasks_28_July/     → TensorFlow & PyTorch, forward/backward pass
├── Week_5_Day_3_Tasks_29_July/     → GPU-accelerated training
└── Week_5_Day_4_Tasks_30_July/     → Deep Neural Networks
```