## About me
Hi! I'm a Data Science & AI student at **State University of Londrina (UEL)**. This project was developed focusing on the practical application of unsupervised learning techniques (K-Means).

---

# 🤖 Custom K-Means Implementation & Cluster Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/Library-NumPy-lightgrey?style=for-the-badge&logo=numpy)
![Machine Learning](https://img.shields.io/badge/Focus-Unsupervised%20Learning-orange?style=for-the-badge)

This repository contains a "from-scratch" implementation of the **K-Means Clustering** algorithm. The goal was to build a functional model to segment data (Gym Customer Segmentation) while exploring the mathematical foundations of centroid optimization.

## 🧠 Technical Decisions & Strategy

For this first implementation, I prioritized a clear and functional logic over extreme complexity:

1.  **Smart Centroid Initialization:** Instead of generating random coordinates in space, the model selects **actual samples** from the dataset as initial centroids. This ensures the algorithm starts within the data boundaries, leading to faster convergence.
2.  **Linear Algebra with NumPy:** To calculate Euclidean distances, I leveraged `np.linalg.norm`. This "shortcut" provided a clean, readable, and mathematically robust way to handle the norm calculation without reinventing basic distance formulas.
3.  **Optimization via Elbow Method:** To solve the classic K problem," I implemented a loop to calculate the **WCSS (Within-Cluster Sum of Squares)** across multiple potential K values.
4.  **Visual Perception:** The final decision on the number of clusters was made through visual analysis of the **Elbow Plot**, identifying the point where the rate of decrease in WCSS shifts significantly.

## 📈 Methodology Flow

* **Step 1:** Run the custom K-Means for K in range (1, 8).
* **Step 2:** Compute WCSS for each iteration.
* **Step 3:** Generate the **Elbow Chart** to determine the optimal K.
* **Step 4:** Execute the final model and visualize the **Scatter Plot** with final clusters and their respective centroids.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/arcseno/kmeans-clustering-from-scratch.git](https://github.com/arcseno/kmeans-clustering-from-scratch.git)
    ```
2.  **Navigate to the folder:**
    ```bash
    cd kmeans-clustering-from-scratch
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the analysis:**
    ```bash
    python main.py
    ```

## 🛠️ Technologies
* **Python 3**
* **NumPy:** Vectorized operations and distance norms.
* **Matplotlib:** Data visualization and Elbow method plotting.
