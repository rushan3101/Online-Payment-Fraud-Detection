# 🛡️ Online Payment Fraud Detection

## 📌 Project Overview  
This project focuses on building a **fraud detection system** using machine learning.  
We worked with a large dataset of online transactions to identify fraudulent activity, starting from **data preprocessing and exploratory data analysis (EDA)** to **model training and evaluation**.  

The main objective was to compare multiple ML models and identify the most effective approach for fraud detection in highly imbalanced datasets.  

---

## ⚙️ Steps Involved  

### 🔍 1. Data Exploration & EDA  
- Inspected dataset structure, data types, and missing values.  
- Visualized fraud distribution, transaction type frequencies, and feature correlations.  
- Identified **heavy class imbalance**: fraud cases are extremely rare compared to non-fraud.  

### 🛠️ 2. Data Preprocessing  
- Applied **one-hot encoding** on categorical features (transaction type).  
- Dropped non-informative columns (`nameOrig`, `nameDest`, etc.).  
- Split dataset into **train & test sets** with stratification to preserve fraud ratio.  

### 🤖 3. Modeling  
- Implemented and compared three ML models:  
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
- Evaluated performance using **confusion matrix, accuracy, and AUC score**.  

### 📊 4. Results  
- Logistic Regression and Random Forest showed decent performance.  
- **XGBoost outperformed others** with:  
  - **Accuracy: ~98%**  
  - **AUC Score: ~99%**  
- XGBoost was selected as the **final model for fraud detection**.  

---

## 📂 Repository Structure  
```
📦 fraud-detection  
 ┣ 📜 fraud_detection.ipynb   # Main Jupyter Notebook  
 ┣ 📜 README.md               # Project Documentation  
```

---

## 📑 Dataset  
The dataset used in this project is publicly available on [Payments Fraud Dataset](https://drive.google.com/file/d/1txKoaCNnIOcwhBdJAM1MPUqEfjYaCZhk/view?usp=drive_link).  

---

## 🏆 Conclusion  
This project demonstrates the **end-to-end process of building a fraud detection pipeline**, from raw data analysis to selecting the best-performing ML model.  
By leveraging **XGBoost**, we achieved **high accuracy and AUC**, making it a strong candidate for real-world fraud detection systems.  
