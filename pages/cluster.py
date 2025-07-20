import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

def show(df):
    st.header("Tren Penyewaan Harian per Cluster")

    st.header("Ringkasan Data")
    total = df.shape[0]
    unique_clusters = df['cluster'].nunique()
    st.metric("Total Data", total)
    st.metric("Jumlah Cluster", unique_clusters)

    st.subheader("Jumlah Data per Cluster")
    st.bar_chart(df['cluster'].value_counts())

    st.subheader("Statistik Penyewaan per Cluster")
    st.dataframe(df.groupby('cluster')['cnt'].agg(['mean', 'min', 'max', 'std']).round(2))

    cluster_pilihan = st.multiselect("Pilih Cluster", options=df['cluster'].unique(),
                                     default=df['cluster'].unique())
    df_filter = df[df['cluster'].isin(cluster_pilihan)]

    plt.figure(figsize=(14, 8))
    sns.scatterplot(data=df_filter, x='dteday', y='cnt', hue='cluster')
    plt.title("Jumlah Penyewaan Sepeda Harian berdasarkan Cluster")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Penyewaan (cnt)")
    plt.tight_layout()
    st.pyplot(plt.gcf())