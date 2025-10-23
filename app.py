import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world!")

st.write("""
# SQL SRS
Spaced Repetition System SQL Practice
""")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme ...",
)

st.write('You selected', option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dogs", "Owl"])

with tab1:
    input_text = st.text_area(label='entrez votre input')
    st.dataframe(df)
