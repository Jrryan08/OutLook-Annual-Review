import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from streamlit_option_menu import option_menu

st.markdown(
    """
    <div style='white-space: nowrap; overflow-x: auto;'>
        <h1 style='color: purple; display: inline-block; font-size: 2.2em; margin: 0;'>
            OutLook Telecom: Annual Data Review
        </h1>
    </div>
    """,
    unsafe_allow_html=True)
st.subheader(":violet[Data Visualization]")

dataset = pd.read_csv("assets/telecom_customer_churn.csv")

dataset_cleaned = dataset.dropna(subset=['Gender', 'Churn Category', 'Tenure in Months', 'Monthly Charge', 'Total Charges'])

# Horizontal navigation for pages
selected_page = option_menu(
    menu_title=None, 
    options=["Demographics", "Services", "Financial Trends"],
    orientation="horizontal",
    icons=['house', 'person', 'bar-chart'],
    default_index=0
)

# Page 1: Customer Demographics
if selected_page == "Demographics":
    st.title("Customer Demographics and Churn Analysis")

# Page 2: Service and Subscription
if selected_page == "Services":
    st.title("Service and Subscription Features vs Churn")
    
# Page 3: Financial Trends and Customer Lifetime
if selected_page == "Financial Trends":
    st.title("Financial Trends and Customer Lifetime")
    
