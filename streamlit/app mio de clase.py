
# --------- Librerias ---------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
# ------------ Configuracion de la pagina ------------
st.set_page_config(
    page_title="Titanic dashboard",
    page_icon="🚢",
    layout="wide", # wide, centered...)
)

# ------------ Titulo de la pagina ------------
st.title("Titanic dashboard 🚢")
st.subheader("Análisis de datos del Titanic")

df = pd.read_csv("titanic_clean.csv")
df

# ------------- Textos -------------
st.markdown("Hola")


# ------------- Tabla -------------
# ------------- Tabs -------------
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
        st.write("Contenido del Tab 1")
with tab2:
        st.write("Contenido del Tab 2")
with tab3:
        st.write("Contenido del Tab 3")