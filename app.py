import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sales Dashboard", 
                   page_icon=":bar_chart:", 
                   layout="wide")

df = pd.read_csv("supermarket_sales.csv")

# Run the appication
st.dataframe(df)
