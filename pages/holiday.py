import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show(df, st):
    st.header("Tren Penyewaan Harian berdasarkan hari libur")

    st.subheader("Statistik Penyewaan berdasarkan hari libur")
    st.dataframe(df.groupby('holiday')['cnt'].agg(['mean', 'min', 'max', 'std']).round(2))

    agg_data = df.groupby("holiday")["cnt"].agg(["mean", "std"]).reset_index()
    agg_data["holiday_label"] = agg_data["holiday"].map({0: "Bukan Hari Libur", 1: "Hari Libur"})

    plt.figure(figsize=(6,4))
    sns.barplot(x="holiday_label", y="mean", data=agg_data, color="blue")
    plt.title("Rata-rata dan Sebaran Pengguna Sepeda berdasarkan hari libur")
    plt.ylabel("Jumlah Pengguna")
    plt.xlabel("Jenis Hari")

    st.pyplot(plt.gcf())