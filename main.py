import pandas as pd
import streamlit as st

import pages.cluster as cluster
import utils.data_formatter as utils

@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

all_df = load_data()

holiday_data = utils.create_by_holiday(all_df)
season_data = utils.create_by_season(all_df)

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Tren Cluster"])

st.title("Analisis Penyewaan Sepeda Harian Berdasarkan Cluster")

if menu == "Tren Cluster":
    cluster.show(all_df)