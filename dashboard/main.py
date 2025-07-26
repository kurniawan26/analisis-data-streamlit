import os
import pandas as pd
import streamlit as st

import pages.cluster as cluster
import pages.holiday as holiday
import pages.weather as weather
import utils.data_formatter as utils

@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data", "day.csv")
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

all_df = load_data()

holiday_data = utils.create_by_holiday(all_df)
season_data = utils.create_by_season(all_df)

menu = st.sidebar.radio("Pilih Halaman", ["Hari libur", "Cuaca","Tren Cluster"])

st.title("Analisis Penyewaan Sepeda Harian")

if menu == "Hari libur":
    holiday.show(all_df, st)

elif menu == "Cuaca":
    weather.show(all_df, st)

elif menu == "Tren Cluster":
    cluster.show(all_df, st)
