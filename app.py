import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv('vehicles_us.csv')

st.title('VENTA DE AUTOS SEMI-NUEVOS')

st.header('Kilometraje')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Construir un histograma para conocer el kilometraje de nuestros autos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

st.header('Modelo del Auto')

disp_button = st.button('Construir un grafico de Dispersion')
if disp_button:
    st.write(
        'Muestra la relacion entre el modelo del auto y su precio')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig, use_container_widh=True)

group_condition = car_data.groupby('condition')
option = st.selectbox(
    'Seleciona la condicion que deseas tu auto', car_data['transmission'])
