from fpdf import FPDF
import matplotlib.pyplot as plt
from pathlib import Path

def stworz_pdf(miasto, data, pliki):
    pdf = FPDF()
    pdf.add_font("DejaVu", "", str(Path("fonts/DejaVuSans.ttf")), uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    for plik in pliki:
        pdf.add_page()
        pdf.set_font("DejaVu", size=12)
        pdf.cell(0, 10, f"{miasto} - {data}", ln=True)
        pdf.image(plik, x=10, y=20, w=180)
    nazwa = f"raport_{miasto}_{data}.pdf".replace(" ", "_")
    pdf.output(nazwa)
    print(f"📄 Zapisano raport PDF jako: {nazwa}")

def generuj_wykresy(miasto, data, dane):
    from datetime import datetime
    from pathlib import Path
    Path("wykresy").mkdir(parents=True, exist_ok=True)
    czasy = [datetime.fromisoformat(t).strftime("%H:%M") for t in dane["time"]]
    temperatury = dane["temperature_2m"]
    wilgotnosc = dane["relative_humidity_2m"]
    wiatr = dane["windspeed_10m"]
    opady = dane["precipitation"]

    pliki = []

    # Wykres 1 — Temperatura
    plt.figure(figsize=(12, 5))
    plt.plot(czasy, temperatury, marker="o", color="orangered")
    plt.title(f"Temperatura w {miasto} ({data})")
    plt.xlabel("Godzina")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plik1 = f"wykresy/temperatura_{miasto}_{data}.png".replace(" ", "_")
    plt.savefig(plik1)
    plt.close()
    pliki.append(plik1)

    # Wykres 2 — Wilgotność i Wiatr
    plt.figure(figsize=(12, 5))
    plt.plot(czasy, wilgotnosc, label="Wilgotność (%)", color="cornflowerblue")
    plt.plot(czasy, wiatr, label="Wiatr (km/h)", color="seagreen")
    plt.title(f"Wilgotność i Wiatr w {miasto} ({data})")
    plt.xlabel("Godzina")
    plt.ylabel("Wartości")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plik2 = f"wykresy/wilgotnosc_wiatr_{miasto}_{data}.png".replace(" ", "_")
    plt.savefig(plik2)
    plt.close()
    pliki.append(plik2)

    # Wykres 3 — Opady
    plt.figure(figsize=(12, 5))
    plt.bar(czasy, opady, color="mediumpurple")
    plt.title(f"Opady w {miasto} ({data})")
    plt.xlabel("Godzina")
    plt.ylabel("Opady (mm)")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plik3 = f"wykresy/opady_{miasto}_{data}.png".replace(" ", "_")
    plt.savefig(plik3)
    plt.close()
    pliki.append(plik3)

    return pliki
