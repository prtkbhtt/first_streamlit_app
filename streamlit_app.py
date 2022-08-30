import streamlit
import pandas as pd

streamlit.title("""My Web Application
      *Hellow World!*""")

df = pd.read_csv("C:\Users\prateek.bhatt\Downloads\veg_plant_height")
streamlit.line_chart(df)                   

