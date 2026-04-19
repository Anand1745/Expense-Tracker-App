import streamlit as st
import matplotlib.pyplot as plt

from src.data_processing import load_data, preprocess
from src.analysis import category_analysis, monthly_trend
from src.ml_model import train_model, predict, detect_anomaly

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Expense Analytics Dashboard",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("## 💰 Expense Analytics Dashboard")
st.caption("Analyze spending patterns, trends, and anomalies using Data Science & ML")

# ---------------------------
# LOAD DATA
# ---------------------------
df = preprocess(load_data())

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
st.sidebar.header("🔍 Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    df['category'].unique(),
    default=df['category'].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    df['payment_method'].unique(),
    default=df['payment_method'].unique()
)

df = df[
    (df['category'].isin(category_filter)) &
    (df['payment_method'].isin(payment_filter))
]

# ---------------------------
# KPI SECTION (STYLED)
# ---------------------------
st.markdown("### 📊 Key Metrics")

c1, c2, c3 = st.columns(3)

c1.markdown(f"""
### 💸 Total Spend  
## ₹ {df['amount'].sum():,.0f}
""")

c2.markdown(f"""
### 📈 Average Spend  
## ₹ {df['amount'].mean():,.2f}
""")

c3.markdown(f"""
### 🔥 Max Transaction  
## ₹ {df['amount'].max():,.0f}
""")

st.markdown("---")

# ---------------------------
# ANALYSIS
# ---------------------------
cat = category_analysis(df)
month = monthly_trend(df)

# ---------------------------
# CHART SECTION
# ---------------------------
st.markdown("### 📊 Spending Analysis")

col1, col2 = st.columns(2)

# Bar Chart
with col1:
    fig1, ax1 = plt.subplots(figsize=(5,3))
    cat.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title("Category-wise Spending")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Amount")
    plt.tight_layout()
    st.pyplot(fig1)

# Line Chart
with col2:
    fig2, ax2 = plt.subplots(figsize=(5,3))
    month.plot(ax=ax2, color='orange')
    ax2.set_title("Monthly Spending Trend")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Amount")
    plt.tight_layout()
    st.pyplot(fig2)

st.markdown("---")

# ---------------------------
# PIE CHART (CENTERED & FIXED SIZE)
# ---------------------------
st.markdown("### 🥧 Spending Distribution")

fig3, ax3 = plt.subplots(figsize=(4,4))
cat.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax3,
    textprops={'fontsize': 8}
)
ax3.set_ylabel("")
ax3.set_title("Distribution")
plt.tight_layout()

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.pyplot(fig3)

st.markdown("---")

# ---------------------------
# ML SECTION
# ---------------------------
st.markdown("### 🤖 Machine Learning Insights")

model, cols = train_model(df)

sample = df.sample(1)
pred = predict(model, cols, sample)

anomaly = detect_anomaly(df)

c4, c5 = st.columns(2)

c4.metric("🔮 Predicted Next Expense", f"₹ {pred[0]:.2f}")
c5.metric("🚨 Anomalies Detected", len(anomaly))

# Insights
st.info(f"""
📌 Key Insights:
- Highest spending category: **{cat.idxmax()}**
- Peak spending month: **{month.idxmax()}**
- Total anomalies detected: **{len(anomaly)}**
""")

# Anomaly Table
if len(anomaly) > 0:
    st.markdown("#### ⚠️ Suspicious Transactions")
    st.dataframe(
        anomaly[['date', 'category', 'amount']].head(10),
        use_container_width=True
    )

st.markdown("---")

# ---------------------------
# RAW DATA
# ---------------------------
st.markdown("### 📄 Raw Data Preview")

st.dataframe(df.head(20), use_container_width=True)