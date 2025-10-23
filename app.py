import streamlit as st
import pandas as pd

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dogs", "Owl"])

with tab1:
    input_text = st.text_area(label='entrez votre input')
    st.dataframe(df)
