import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv('vehicles_us.csv')

st.header('VENTA DE AUTOS')
st.caption('Muetra los odometros de los autos que manejamos')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Construir un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

st.header('Modelo del Auto')
st.caption('Muestra la relacion entre el modelo del auto y su precio')

disp_button = st.button('Construir un grafico de Dispersion')
if disp_button:
    st.write(
        'Construir un grafico de dispersion para el conjunto de anuncion de venta de coches')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig, use_container_widh=True)
