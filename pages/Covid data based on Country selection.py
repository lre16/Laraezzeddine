# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:04:26 2022

@author: AUB
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.offline as py
import plotly.figure_factory as ff
import streamlit as st

df=pd.read_csv("covid.csv")

df1=pd.read_csv("covid_grouped.csv")


st.header("Covid Demo per Region")

country_select=st.sidebar.selectbox('This a demo Dashboard that will enable you to see the Covid data of any country selected of your choice.The result will fall under three main categories :Confirmed, Death,Recovered cases between Febraury and July 2020', df1['Country/Region'])


country_selected=df1[df1['Country/Region']==country_select]

st.text_area('Total Confirmed cases', value=sum(country_selected['Confirmed']))
              
st.text_area('Total Death cases', value=sum(country_selected['Deaths']))

st.text_area('Total Recovered cases', value=sum(country_selected['Recovered']))

st.subheader("Covid Confirmed cases ")

fig=px.line(country_selected, x="Date", y="Confirmed" )
st.plotly_chart(fig,use_container_width=False)

st.subheader("Covid Death cases ")
fig1=px.line(country_selected, x="Date", y="Deaths" )
st.plotly_chart(fig1,use_container_width=False)

st.subheader("Covid Recovered cases ")
fig2=px.line(country_selected, x="Date", y="Recovered" )
st.plotly_chart(fig2,use_container_width=False)


