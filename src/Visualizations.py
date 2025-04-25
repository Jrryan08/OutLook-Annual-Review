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
    st.subheader(":violet[Customer Demographics]")
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    labels = ["11–19", "20–29","30–39",  "40–49",  "50–59",  "60–69", "70–79","80+"]
    dataset["Age Range"] = pd.cut(dataset["Age"], bins=bins, labels=labels, right=False)

    # Distribution selector
    distribution_type = st.selectbox("Select Distribution Type",["Gender", "Age Range"])

    # Distribution by Gender
    if distribution_type == "Gender":
        gender_counts = dataset['Gender'].value_counts()
        st.subheader(":violet[Customer Distribution by Gender]")
        fig, ax = plt.subplots()
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette("deep", len(gender_counts)))
        ax.axis('equal')  
        st.pyplot(fig)

    # Distribution by Age Range
    elif distribution_type == "Age Range":
        age_counts = dataset["Age Range"].value_counts().sort_index()
        st.subheader(":violet[Customer Distribution by Age Range]")
        fig, ax = plt.subplots()
        sns.barplot(x=age_counts.index, y=age_counts.values, palette="colorblind", ax=ax)
        ax.set_ylabel("Number of Customers")
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.set_xlabel("Age Range")
        st.pyplot(fig)
    
    # Map of Customer Distribution In California
    st.subheader(":violet[Map of Customer Distribution In California]")
    lat = dataset["Latitude"]
    lon = dataset["Longitude"]
    data = pd.DataFrame({'lat': lat, 'lon': lon})
    st.map(data)


    city_counts = dataset['City'].value_counts().reset_index()
    city_counts.columns = ['City', 'Customer Count']

    # Most Popular Cities
    st.subheader(":violet[Top Cities by Customer Count]")
    sorted_data = city_counts.sort_values(by='Customer Count', ascending=False)
    top_data = sorted_data.head(5)  
    fig, ax = plt.subplots()
    sns.barplot(x='Customer Count', y='City', data=top_data, palette='viridis', ax=ax)
    ax.set_xlabel("Customer Count")
    ax.set_ylabel("City")
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig)

    # Least Popular Cities
    st.subheader(":violet[Least Popular Cities by Customer Count]")
    sorted_data = city_counts.sort_values(by='Customer Count', ascending=True)
    bottom_data = sorted_data.head(10)
    st.dataframe(bottom_data[['City', 'Customer Count']] ,width=700)

    

# Page 2: Service and Subscription
if selected_page == "Services":
    st.subheader(":violet[Services and Subscriptions]")
    
# Page 3: Financial Trends and Customer Lifetime
if selected_page == "Financial Trends":
    st.subheader(":violet[Financial Trends and Customer Lifetime]")
    
