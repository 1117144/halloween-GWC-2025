import streamlit as st
import pandas as pd
st.title("Halloween Candy Recommender")

df = pd.read_csv("candy-data.csv")
sugar_level = st.slider("Sugar Level: " , 0, 10)
df["sugar_scale"] = df["sugarpercent"] * 9 + 1
candy_types = ["Chocolate", "Fruity", "Caramel", "Contain Nuts", "Nougat", "Crispy Wafer", "Hard", "Bar", "Puribus (one of many in a bag/box)"]
selected_types = st.multiselect(
    "What type/s of candy do you prefer?",
    options = candy_types,
    default = ["Chocolate"]
)