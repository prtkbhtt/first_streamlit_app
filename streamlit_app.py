import streamlit
import pandas as pd

streamlit.title('my parants')

df = pd.read_csv("C:\Users\prateek.bhatt\Downloads\veg_plant_height.csv")
streamlit.line_chart(df)                   

