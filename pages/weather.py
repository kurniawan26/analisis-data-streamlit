import seaborn as sns
import matplotlib.pyplot as plt

def show(df, st):
    st.header("🌤️ Tren Penyewaan Harian berdasarkan Cuaca")

    show_mendung = st.checkbox("Tampilkan cuaca mendung", value=True)
    show_cerah = st.checkbox("Tampilkan cuaca cerah", value=True)
    show_hujan = st.checkbox("Tampilkan cuaca hujan ringan", value=True)
    show_badai = st.checkbox("Tampilkan cuaca hujan lebat / badai petir", value=True)

    selected_weather = []
    if show_mendung:
        selected_weather.append(1)
    if show_cerah:
        selected_weather.append(2)
    if show_hujan:
        selected_weather.append(3)
    if show_badai:
        selected_weather.append(4)


    filtered_df = df[df['weathersit'].isin(selected_weather)]

    st.subheader("📈 Statistik Penyewaan berdasarkan Hari Libur")
    st.dataframe(
        filtered_df.groupby('weathersit')['cnt'].agg(['mean', 'min', 'max', 'std']).round(2)
    )

    agg_data = filtered_df.groupby("weathersit")["cnt"].agg(["mean", "std"]).reset_index()
    agg_data["weather_label"] = agg_data["weathersit"].map({
        1: 'Cerah',
        2: 'Awan Mendung',
        3: 'Hujan Ringan',
        4: 'Hujan Lebat / Badai Petir'
    })

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="weather_label", y="mean", data=agg_data, color="skyblue", ax=ax)
    ax.set_title("Rata-rata Pengguna Sepeda berdasarkan cuaca")
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_xlabel("Jenis Cuaca")

    st.pyplot(plt.gcf())