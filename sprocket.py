import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


# reading all the three new data
CustomerDemographic_df = pd.read_csv('./new_data/CustomerDemographic_df.csv')
Transactions_df = pd.read_csv('./new_data/Transactions.csv')
CustomerAddress_df = pd.read_csv('./new_data/CustomerAddress_df.csv')

st.write()
st.image("./new_data/sprocket_central_logo.png", caption="Sprocket Central", use_column_width=True)
st.subheader("View Data of various cheatsheet")
col1, col2, col3 = st.columns(3)



if col1.button("Show Demographic Data"):
    st.subheader("Raw Data")
    st.dataframe(CustomerDemographic_df.head(5))

if col2.button("Show Transacions Data"):
    st.subheader("Raw Data")
    st.dataframe(Transactions_df.head(5))

if col3.button("Show Address Data"):
    st.subheader("Raw Data")
    st.dataframe(CustomerAddress_df.head(5))
# visualize CustomerDemograpgic
# CustomerAddress_df.head(5)

st.subheader("Distribution of a Selected Customer Demograph")
selected_feature = st.selectbox("Select a feature to display its distribution:", CustomerDemographic_df.columns[:-1])

hist_plot = px.histogram(CustomerDemographic_df, x=selected_feature, color="Health", nbins=30, marginal="box", hover_data=CustomerDemographic_df.columns)
st.plotly_chart(hist_plot)

st.subheader("Distribution of a Selected Customer Transaction")
selected_feature = st.selectbox("Select a feature to display its distribution:", Transactions_df.columns[:-1])

hist_plot = px.histogram(Transactions_df, x=selected_feature, color="Solex", nbins=30, marginal="box", hover_data=Transactions_df.columns)
st.plotly_chart(hist_plot)

st.subheader("Distribution of a Selected Customer Address")
selected_feature = st.selectbox("Select a feature to display its distribution:", CustomerAddress_df.columns[:-1])

hist_plot = px.histogram(CustomerAddress_df, x=selected_feature, color="state", nbins=30, marginal="box", hover_data=CustomerAddress_df.columns)
st.plotly_chart(hist_plot)


