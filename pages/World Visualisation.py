# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:01:40 2022

@author: AUB
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.offline as py
import plotly.figure_factory as ff
import streamlit as st

df=pd.read_csv("C:/Users/AUB/OneDrive/OneDrive - American University of Beirut/Desktop/pages/pages/covid.csv")


df1=pd.read_csv("C:/Users/AUB/OneDrive/OneDrive - American University of Beirut/Desktop/pages/pages/covid_grouped.csv")

st.subheader(" Covid data as per Continent")
st.write("The following Visualisation will show Covid data in each Continent")


vis2= st.radio('Select', ['Total Cases','Death Rate','Recovered'],key='3')

if vis2== 'Total Cases':
    total_number_covid= px.bar(df,x='Continent',y='TotalCases',color='TotalCases',hover_data=['Continent'])

if vis2== 'Death Rate':
    total_number_covid= px.bar(df,x='Continent',y='TotalDeaths',color='TotalDeaths',hover_data=['Continent'])

if vis2== 'Recovered':
    total_number_covid= px.bar(df,x='Continent',y='TotalRecovered',color='TotalRecovered',hover_data=['Continent'])
    
st.plotly_chart(total_number_covid, use_container_width=False)



st.subheader("Please Select one of the options below to display the data" )


vis= st.radio('', ['Total Cases','Death Rate'],key='2')

if vis== 'Total Cases':
    st.subheader("Top 10 Countries impacted by Covid")
    vis1=px.pie(df.head(10), values='TotalCases', names='Country/Region')



if vis== 'Death Rate':
    st.subheader("Top 10 Countries with the Highest Death rate due to covid")
    vis1=px.pie(df.head(10), values='TotalDeaths', names='Country/Region') 
    
st.plotly_chart(vis1,use_container_width=False)


st.subheader("Scatter plot presenting highest death rates registered due to covid in 30 countries")
total_cases_deaths_covid= px.scatter(df.head(30), x='TotalCases', y= 'TotalDeaths', color='TotalDeaths', size= 'Population', hover_name="Country/Region",size_max=100)
total_cases_deaths_covid.update_layout(xaxis_title='Total Covid Cases',yaxis_title='Death rate')
st.plotly_chart(total_cases_deaths_covid,use_container_width=False)

st.subheader("Covid Map showing Death recorder from January 2020 to July 2020 per region")
map_visual_covid_death=px.choropleth(df1,
              locations='iso_alpha',
              color="New deaths",
              hover_name="Country/Region",
              color_continuous_scale=px.colors.sequential.Plasma,
              projection="natural earth",
              animation_frame="Date" )
st.plotly_chart(map_visual_covid_death,use_container_width=False)    
                                                                                                                        
 
 

    


