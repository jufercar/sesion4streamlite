
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

# ------------ Titulo de la pagina ------------
st.title("Titanic dashboard 🚢")
st.subheader("Análisis de datos del Titanic")