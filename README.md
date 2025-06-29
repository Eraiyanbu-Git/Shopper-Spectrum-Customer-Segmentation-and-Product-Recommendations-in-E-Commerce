# 🛒 Shopper Spectrum  
**Customer Segmentation and Product Recommendations in E-Commerce**

![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%94-green) ![MachineLearning](https://img.shields.io/badge/Machine--Learning-KMeans%20%7C%20Cosine--Similarity-orange) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Project Overview

**Shopper Spectrum** is an end-to-end machine learning solution for the e-commerce domain. It segments customers based on their purchase behavior using **RFM analysis and KMeans clustering**, and recommends similar products using **item-based collaborative filtering** powered by **cosine similarity**. It is deployed through an interactive **Streamlit web application**.

---

## 🧠 Problem Statement

E-commerce platforms generate huge amounts of transactional data daily. Leveraging this data can unlock:
- **Customer segmentation** for targeted marketing
- **Product recommendations** to boost user engagement
- **Retention strategies** for at-risk customers
- **Inventory optimization** based on purchasing patterns

This project aims to deliver insights through **unsupervised learning** and **collaborative filtering**.

---

## 🧰 Tools & Technologies

- `Python`, `Pandas`, `NumPy`
- `Scikit-learn`, `Cosine Similarity`, `KMeans`
- `Matplotlib`, `Seaborn`
- `Streamlit`
- `Pickle` (for model persistence)

---

## 📂 Project Structure

```bash
shopper-spectrum/
│
├── app/
│   └── app.py                        # Streamlit application
├── data/
│   └── OnlineRetail.csv             # Input dataset
├── models/
│   ├── kmeans_model.pkl             # Saved clustering model
│   ├── scaler.pkl                   # Scaler for RFM features
│   └── product_similarity.pkl       # Cosine similarity matrix
├── notebooks/
│   └── eda_modeling.ipynb           # Full analysis & model training
└── README.md
✨ Author

Eraiyanbu
