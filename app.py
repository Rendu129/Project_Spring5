import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv(
    r"C:\Users\ed_rs\OneDrive\Documentos\Programacion\Tripleten\Proyecto_Spring5\Project_Spring5\vehicles_us.csv")

st.header('Venta de Autos')
st.write('Esta app esta en construccion')
fig = px.histogram(car_data, x='odometer')
print(car_data.head())
