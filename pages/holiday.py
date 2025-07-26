
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show(df, st):
    st.header("📊 Tren Penyewaan Harian berdasarkan Hari Libur")

    # Checkbox interaktif
    show_libur = st.checkbox("Tampilkan Hari Libur", value=True)
    show_nonlibur = st.checkbox("Tampilkan Hari Biasa (Bukan Libur)", value=True)

    # Filter berdasarkan checkbox
    selected_holidays = []
    if show_libur:
        selected_holidays.append(1)
    if show_nonlibur:
        selected_holidays.append(0)

    # Filter data
    filtered_df = df[df['holiday'].isin(selected_holidays)]

    # Statistik berdasarkan hari libur
    st.subheader("📈 Statistik Penyewaan berdasarkan Hari Libur")
    st.dataframe(
        filtered_df.groupby('holiday')['cnt'].agg(['mean', 'min', 'max', 'std']).round(2)
    )

    # Data agregat untuk plot
    agg_data = filtered_df.groupby("holiday")["cnt"].agg(["mean", "std"]).reset_index()
    agg_data["holiday_label"] = agg_data["holiday"].map({
        0: "Bukan Hari Libur",
        1: "Hari Libur"
    })

    # Plot rata-rata penyewaan
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="holiday_label", y="mean", data=agg_data, color="skyblue", ax=ax)
    ax.set_title("Rata-rata Pengguna Sepeda berdasarkan Hari Libur")
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_xlabel("Jenis Hari")

    st.pyplot(fig)

