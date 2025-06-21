import pandas as pd
from pathlib import Path

def wczytaj_dane_historyczne(miasto, zakres="hourly"):
    folder = Path("historia") / miasto.replace(" ", "_")
    plik = folder / f"{miasto}_{zakres}.parquet"
    if not plik.exists():
        print(f"⚠️ Brak danych historycznych dla {miasto}")
        return None
    return pd.read_parquet(plik)

def statystyki_miesieczne(df):
    df["data"] = pd.to_datetime(df["time"] if "time" in df.columns else df["date"])
    df["miesiac"] = df["data"].dt.to_period("M")
    return df.groupby("miesiac").agg({
        "temperature_2m": "mean",
        "precipitation": "sum",
        "relative_humidity_2m": "mean"
    }).round(1).reset_index()
