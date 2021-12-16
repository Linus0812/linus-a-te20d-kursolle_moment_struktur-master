#fråga efter hens lön
lon = float(input("Vad är din lön? "))

#beräkna kommunalskatten
komm_skatt = lon * 0.2136

#beräkna landstingsskatten
lands_skatt = lon * 0.1148

#beräkna det av lönen som finns kvar
lon_kvar = lon - komm_skatt - lands_skatt

#skriv ut allt
print(f"""Utskrift:

Månadslön:  {lon}
Kommunal skatt: {round(komm_skatt)}
Landstingsskatt: {round(lands_skatt)}
Kvar efter skatt: {round(lon_kvar)}""")