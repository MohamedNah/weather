import streamlit as st
import plotly.express as px
from backend import get_data

st.header('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcast days', min_value=1, max_value=5,
                 help='Select number of days to be forecasted')
data = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{data} for the next {days} days in {place}')

# dates = ['02-04-2023', '07-04-2023', '12-04-2023', '17-04-2023']
# temperature = [20, 18, 15, 22]
# temperature = [(days * i)/4 for i in temperature]

dates, info = get_data(place, days, data)
print(info)
fig = px.line(x=dates, y=info, labels={'x': 'Dates', 'y': 'Temperature'})
st.plotly_chart(fig)





