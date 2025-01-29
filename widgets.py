import streamlit as st
import numpy as np
st.checkbox('Yes')
st.sidebar.radio('Pick your gender',['Male', 'Female'])
st.selectbox('Pick a Fruit',['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Mercury', 'Earth'])
st.select_slider('Pick a Mark', ['Bad', 'Good', 'Excellent', 'Average'])
st.slider('Pick a number',0,50)
st.number_input('Pick a number',0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('College time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favourite color')
