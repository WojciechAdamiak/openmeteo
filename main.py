from datetime import date, timedelta
from utils.api import znajdz_lokalizacje, pobierz_dane_godzinowe
from utils.raport import stworz_pdf, generuj_wykresy
from utils.parquet_writer import zapisz_do_parquet
from utils.analiza import wczytaj_dane_historyczne, statystyki_miesieczne


def wczytaj_liste_miast(sciezka="miasta.csv"):
    df = pd.read_csv(sciezka)
    return df["miasto"].tolist()

nazwa = input("📍 Podaj nazwę miejscowości: ")
lok = znajdz_lokalizacje(nazwa)
lat, lon = lok["lat"], lok["lon"]
miasto = lok["display_name"].split(",")[0]

dni = [str(date.today() + timedelta(days=i)) for i in range(5)]
print("\n📅 Wybierz dzień prognozy:")
for i, d in enumerate(dni): print(f"{i+1}. {d}")
try:
    wybor = int(input("Numer dnia [1–5]: ")) - 1
    data = dni[wybor] if 0 <= wybor < 5 else dni[0]
except:
    data = dni[0]

dane = pobierz_dane_godzinowe(lat, lon, data)
zapisz_do_parquet(miasto, data, dane)
# --- Analiza danych historycznych ---
df_hist = wczytaj_dane_historyczne(miasto, "hourly")
if df_hist is not None:
    stats = statystyki_miesieczne(df_hist)
    ostatni = stats.tail(1)
    print("\n📊 Ostatni miesiąc (średnie wartości):")
    print(ostatni.to_string(index=False))
pliki = generuj_wykresy(miasto, data, dane)
stworz_pdf(miasto, data, pliki)
