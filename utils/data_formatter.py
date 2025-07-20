def create_by_holiday(df):
    weather_labels = {
        1: 'Cerah',
        2: 'Awan Mendung',
        3: 'Hujan Ringan',
        4: 'Hujan Lebat / Badai Petir'
    }
    df['weather_label'] = df['weathersit'].map(weather_labels)

    df.groupby(by="weather_label").agg({
        "cnt": ["max", "min", "mean", "std"]
    })

    df = df.groupby("holiday")["cnt"].agg(["mean", "std"]).reset_index()
    df["holiday_label"] = df["holiday"].map({0: "Bukan Hari Libur", 1: "Hari Libur"})
    return df


def create_by_season(df):
    weather_labels = {
        1: 'Cerah',
        2: 'Awan Mendung',
        3: 'Hujan Ringan',
        4: 'Hujan Lebat / Badai Petir'
    }
    df['weather_label'] = df['weathersit'].map(weather_labels)
    return df

exports = {
    create_by_holiday: create_by_holiday,
    create_by_season: create_by_season
}