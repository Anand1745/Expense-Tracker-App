# 💰 Expense Analytics Dashboard (Data Science + ML)

## 📊 Overview

This project is a data-driven expense tracking and analytics system built using Python and Streamlit. It helps analyze spending behavior, visualize trends, and generate intelligent insights using machine learning.

---

## 🎯 Problem Statement

Managing expenses is often unstructured and lacks actionable insights. Users struggle to:

* Track spending patterns
* Identify overspending
* Make informed financial decisions

---

## 💡 Solution

This project provides:

* Structured expense tracking using synthetic data
* Data analysis and visualization
* Machine learning-based predictions
* Anomaly detection for unusual spending

---

## ⚙️ Features

### 📊 Data Analysis

* Category-wise spending analysis
* Monthly trend visualization
* Spending distribution (pie chart)

### 📈 Interactive Dashboard

* Built using Streamlit
* Sidebar filters (category, payment method)
* KPI metrics (total, average, max spending)
* Clean dark-themed UI

### 🤖 Machine Learning

* Expense Prediction using Linear Regression
* Anomaly Detection using Isolation Forest
* Insight generation for decision-making

---

## 🧱 Tech Stack

* Python
* Pandas, NumPy
* Matplotlib
* Streamlit
* Scikit-learn

---

## 📂 Project Structure

```
Expense-Tracker-App/
│
├── data/
│   └── expenses.csv
│
├── src/
│   ├── data_generation.py
│   ├── data_processing.py
│   ├── analysis.py
│   └── ml_model.py
│
├── app/
│   └── dashboard.py
│
├── images/
├── outputs/
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repo-link>
cd Expense-Tracker-App
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Generate dataset:

```
python main.py
```

5. Run dashboard:

```
streamlit run app.py
```

---

## 🧠 Key Insights

* Identify highest spending categories
* Detect peak spending months
* Monitor abnormal transactions
* Predict future expenses

---

## 🚀 Future Improvements

* Time-series forecasting (LSTM / Prophet)
* Budget recommendation system
* Real-time data integration
* Database integration (SQLite/PostgreSQL)
* Cloud deployment

---

## 💼 Use Cases

* Personal finance tracking
* Business expense monitoring
* Budget planning and optimization
* Financial analytics systems

---

## 👨‍💻 Author

Anand Ramesh Karunakaran

---

## ⭐ Conclusion

This project demonstrates how data science, machine learning, and visualization can be combined to build a real-world financial analytics system.
