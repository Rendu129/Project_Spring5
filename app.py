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
    fig = px.scatter(car_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig, use_container_widh=True)

st.header('Tipo de Transmision')

automatic = car_data.query("transmission=='automatic'")[
    ['price', 'model_year']]
manual = car_data.query("transmission=='manual'")[['price', 'model_year']]
hibrido = car_data.query("transmission=='other'")[['price', 'model_year']]

list = ['automatic', 'manual', 'hibrido']
option = st.selectbox(
    'Seleciona tipo de transmision', list, index=None)
st.write('Haz seleccionado:', option)

if option == 'automatic':
    st.write('Selecciona tipo de grafico para la transmision automatica:')
    check = st.checkbox('Histograma')
    check2 = st.checkbox('Grafico de lineas')
    if check:
        st.write('Relacion modelo vd precio autos automaticos')
        fig = px.histogram(automatic, x='model_year',
                           y='price', title='Transmision Automatica')
        st.plotly_chart(fig, use_container_width=True)
    if check2:
        st.write('Relacion modelo vd precio autos automaticos')
        fig = px.scatter(automatic, x='model_year', y='price',
                         title='Transmision Automatica')
        st.plotly_chart(fig, use_container_width=True)

elif option == 'manual':
    st.write('Selecciona tipo de grafico para la trasmision manual:')
    check = st.checkbox('Histograma')
    check2 = st.checkbox('Grafico de lineas')
    if check:
        st.write('Relacion modelo vd precio autos manual')
        fig = px.histogram(manual, x='model_year', y='price',
                           title='Transmision Manual')
        st.plotly_chart(fig, use_container_width=True)
    if check2:
        st.write('Relacion modelo vd precio autos manual')
        fig = px.scatter(manual, x='model_year', y='price',
                         title='Transmision Manual')
        st.plotly_chart(fig, use_container_width=True)
elif option == 'hibrido':
    st.write('Selecciona tipo de grafico para trasmision Hibrida')
    check = st.checkbox('Histograma')
    check2 = st.checkbox('Grafico de lineas')
    if check:
        st.write('Relacion modelo vd precio autos hibridos')
        fig = px.histogram(hibrido, x='model_year',
                           y='price', title='Transmision Hibrida')
        st.plotly_chart(fig, use_container_width=True)
    if check2:
        st.write('Relacion modelo vd precio autos hibridos')
        fig = px.scatter(hibrido, x='model_year', y='price',
                         title='Transmision Hibrida')
        st.plotly_chart(fig, use_container_width=True)
