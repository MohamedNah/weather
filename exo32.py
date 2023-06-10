import streamlit as st
import plotly.express as px
import pandas as pd


st.header('In Search for Happiness')
xaxis = st.selectbox('Select the data for the X-axis', ['GDP', 'Happiness',
                     'Generosity', 'Country'])
yaxis = st.selectbox('Select the data for the Y-axis', ['Generosity', 'GDP',
                     'Happiness', 'Country'])
st.subheader(f'{xaxis} and {yaxis}')

df = pd.read_csv('happy.csv')

match xaxis:
    case 'GDP':
        xdata = df['gdp']
    case 'Happiness':
        xdata = df['happiness']
    case 'Generosity':
        xdata = df['generosity']
    case 'Country':
        xdata = df['country']

match yaxis:
    case 'GDP':
        ydata = df['gdp']
    case 'Happiness':
        ydata = df['happiness']
    case 'Generosity':
        ydata = df['generosity']
    case 'Country':
        ydata = df['country']


figure = px.scatter(x=xdata, y=ydata, labels={'x': xaxis, 'y': yaxis})
st.plotly_chart(figure)
