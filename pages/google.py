import streamlit as st
import pytrends
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pytrends.request import TrendReq


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Trends", page_icon="⚙️")

st.title('Novus Trends ⚙️')
st.header("Monitores de Tendencias en Google en tiempo real💹")

pytrends = TrendReq(hl='en-US', tz=360)
st.write("Tendencias Hoy en Estados Unidos 🇺🇸")
# Google Trends data
df1 = pytrends.trending_searches(pn='united_states')
st.dataframe(df1.head(10))

pytrends1 = TrendReq(hl='es', tz=360)
st.write("Tendencias Hoy en España 🇪🇸")
# Google Trends data
df2 = pytrends1.trending_searches(pn='spain')
st.dataframe(df2.head(10))

st.write("Tendencias Hoy en Colombia 🇨🇴")
# Google Trends data
df3 = pytrends.trending_searches(pn='colombia')
st.dataframe(df3.head(10))

st.write("Tendencias Hoy en Nigeria 🇳🇬")
# Google Trends data
df4 = pytrends.trending_searches(pn='nigeria')
st.dataframe(df4.head(10))

