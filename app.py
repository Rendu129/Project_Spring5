import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv(
    r"C:\Users\ed_rs\OneDrive\Documentos\Programacion\Tripleten\Proyecto_Spring5\Project_Spring5\vehicles_us.csv")

st.header('Venta de Autos')
st.write('Esta app esta en construccion')

hist_button = st.button('Construir histograma')
if his_button:
    st.write(
        'Construir un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
