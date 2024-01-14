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

automatic = car_data.query("transmission=='automatic'")[
    ['price', 'model_year']]
manual = car_data.query("transmission=='manual'")[['price', 'model_year']]
other = car_data.query("transmission=='other'")[['price', 'model_year']]

list = ['automatic', 'manual', 'other']
option = st.selectbox(
    'Seleciona tipo de transmision', list, index=None)
st.write('Haz seleccionado:', option)

if option == 'automatic':
    st.write('Selecciona tipo de grafico para la transmision automatica:')
elif option == 'manual':
    st.write('Selecciona tipo de grafico para la trasmision manual:')
elif option == 'other':
    st.write('Selecciona tipo de grafico para trasmision electrica')
