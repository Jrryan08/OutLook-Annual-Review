import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from PIL import Image
import codecs
import streamlit.components.v1 as components
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
st.subheader(":violet[Data Overview]")

dataset = pd.read_csv("assets/telecom_customer_churn.csv")
dataset_dictionary = pd.read_csv("assets/telecom_data_dictionary.csv", encoding='latin1')

selected = option_menu(menu_title=None, options=["01: Summary", "02: Dictionary"], orientation="horizontal")
if(selected=="01: Summary"):
    # Display Few Sample Rows
    st.write("### First Look at the Data")
    view_option = st.radio("View from:", ("Top", "Bottom"))
    if view_option == "Top":
        st.dataframe(dataset.head(5))
    else:
        st.dataframe(dataset.tail(5))

    # Shape of the dataset
    st.write(f"**Dataset Shape:** {dataset.shape[0]} rows and {dataset.shape[1]} columns")

    # Basic statistics
    st.write("### Statistical Summary")
    st.write(dataset.describe())

    # Missing values
    st.write("### Missing Values")
    missing = dataset.isnull().sum()
    st.write(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")

    # Data types
    st.write("### Data Types")
    st.write(dataset.dtypes)
    
elif(selected=="02: Dictionary"):
    field_options = dataset_dictionary['Field'].unique()  
    selected_field = st.selectbox("Select a field to view its description:", field_options)
    selected_row = dataset_dictionary[dataset_dictionary['Field'] == selected_field].iloc[0]
    st.markdown('<span style="color:blue; font-weight:bold;">Description</span>', unsafe_allow_html=True)
    st.code(f'"{selected_row["Description"]}"')