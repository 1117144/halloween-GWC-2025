import streamlit as st
import pandas as pd
st.title("Halloween Candy Recommender")

df = pd.read_csv("candy-data.csv")
sugar_level = st.slider("Sugar Level: " , 0, 10)
