# 📊 Customer Churn Prediction and Customer Segmentation

This project analyzes customer behavior, predicts customer churn, and identifies customer segments using machine learning techniques. The goal is to identify customers at risk of leaving, understand different customer groups, and provide actionable business insights to improve retention strategies.

---

## 🚀 Project Overview

Customer churn is a critical problem in telecom businesses. Retaining existing customers is often more cost-effective than acquiring new ones.

In this project:

- Cleaned and preprocessed real-world telecom data
- Performed exploratory data analysis (EDA)
- Applied customer segmentation to identify behavioral patterns
- Built multiple machine learning models for churn prediction
- Evaluated models using classification metrics
- Derived business insights for customer retention strategies

---

## 📂 Dataset

This project uses the **Telco Customer Churn dataset** from Kaggle.

Source: [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

The dataset contains customer demographics, subscription details, service usage information, and billing information used to analyze customer behavior and predict churn.

---

# 👥 Customer Segmentation

K-Means clustering was applied to identify groups of customers with similar behavioral patterns.

### Features used:

- Tenure
- Monthly Charges
- Total Charges

### Why these features?

These features represent:

- Customer loyalty and relationship duration (Tenure)
- Current spending behavior (Monthly Charges)
- Overall customer value over time (Total Charges)

Together, they provide meaningful information for identifying different customer segments.

### Outcome:

Customers were grouped into different segments:

- High-value loyal customers
- High-risk new customers
- Budget customers

These segments can support targeted retention and marketing strategies.

---

# 🧠 Machine Learning Pipeline

The following workflow was implemented:

- Data Cleaning
  - Handling hidden missing values
  - Converting data types
  - Removing inconsistencies

- Feature Engineering
  - Label encoding for binary variables
  - One-hot encoding for categorical variables

- Feature Scaling
  - StandardScaler applied to numerical features

- Model Training:
  - Logistic Regression
  - Random Forest
  - XGBoost

- Model Evaluation:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

- Feature Importance Analysis

---

# 📈 Model Performance

Three classification models were evaluated for customer churn prediction.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Logistic Regression | 80.62% | 66.03% | 55.61% | 60.38% |
| Random Forest | 78.85% | 63.10% | 48.93% | 55.12% |
| XGBoost | 77.86% | 59.69% | 51.07% | 55.04% |

📍 Logistic Regression was selected as the final model because it achieved the best overall balance between accuracy, recall, and interpretability.

---

# 🎯 Key Insights

The analysis identified several important factors influencing customer churn:

- Customers with **fiber optic internet service** show a higher likelihood of churn.
- Customers with **long-term contracts (especially two-year contracts)** are less likely to churn.
- **Higher monthly charges** are associated with increased churn probability.
- **Customers with shorter tenure** represent a higher-risk group.

---

# 💼 Business Recommendations

Based on the model findings:

- Encourage month-to-month customers to move towards long-term contracts using loyalty benefits.
- Provide onboarding support and engagement programs for new customers.
- Review pricing strategies for customers with high monthly charges.
- Investigate service quality issues among fiber optic customers.

---

# 🛠️ Tech Stack

- Python
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- XGBoost

---

# 🔄 How to Use the Saved Model

The complete Logistic Regression pipeline is saved as a `.pkl` file and can be reused without retraining.

The saved pipeline contains:

- Data preprocessing
- Feature encoding
- Feature scaling
- Trained Logistic Regression model

### Load the saved pipeline

```python
import pickle

with open("models/churn_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

```

### ⚠️ Note
The input data must follow the same format as the original dataset before prediction. Since preprocessing steps are included inside the pipeline, the same transformations will automatically be applied during inference.

---

## 🔮 Future Improvements

- Hyperparameter tuning for improved performance
- Deploy the model using FastAPI or Streamlit
- Develop a real-time customer churn prediction application

---

## 📌 Key Highlights

- Combined supervised learning (churn prediction) with unsupervised learning (customer segmentation)
- Built an end-to-end machine learning pipeline
- Applied explainable feature analysis for business interpretation
- Generated actionable insights for customer retention

---

## 📄 License

Copyright (c) 2026 Tayrin Tunzina

This project is licensed under the MIT License.
