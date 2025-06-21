import pandas as pd
from pathlib import Path

def zapisz_do_parquet(miasto, data, dane):
    df = pd.DataFrame({
        "miasto": miasto,
        "data": data,
        "czas": dane["time"],
        "temperatura": dane["temperature_2m"],
        "wilgotnosc": dane["relative_humidity_2m"],
        "wiatr": dane["windspeed_10m"],
        "opady": dane["precipitation"]
    })

    folder = Path("dane") / data
    folder.mkdir(parents=True, exist_ok=True)
    plik = folder / f"{miasto}.parquet".replace(" ", "_")
    df.to_parquet(plik, engine="pyarrow", index=False)
    print(f"💾 Dane zapisane w: {plik}")
