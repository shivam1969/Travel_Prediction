import pandas as pd
import numpy as np
import joblib
import streamlit as st

st.set_page_config(
    page_title="Travel Package Prediction",
    layout="centered"
)
st.title("Travel Package Predicition")

loaded_model=joblib.load('model.joblib')
loaded_preprocessor=joblib.load("preprocessor.joblib")