# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
from PIL import Image

st.markdown("Main Page")

st.header("Streamlit Dashboard for Covid-19 ")
st.subheader("Assignment MSBA325- Data Visualization & Communication")
st.subheader("Student:Lara Ezzeddine/ID 202373146" )


image = Image.open("covid-4948866_1920-1200x803.jpg")

st.image(image)


