import streamlit as st
import pandas as pd
st.write(""" # My first app Hallo World! """)
df=pd.read_csv("mydata.csv.xlsx")
st.linechart(df)
