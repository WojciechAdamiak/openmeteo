import pandas as pd

def wczytaj_liste_miast(sciezka="miasta.csv"):
    df = pd.read_csv(sciezka)
    return df["miasto"].tolist()

miasta = wczytaj_liste_miast()
