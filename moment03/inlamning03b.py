#fråga om månadslön
lon = float(input("Vad är din månadslön? "))

#omvandla till årslön
ars_lon = lon * 12

#kolla om lönen går över brytpunkten och beräkna all skatt och skriva ut
if ars_lon <= 19247:
    komm_skatt = 0
    lands_skatt = 0
    print(f"""Utskrift:

Månadslön:  {lon}kr Årslön: {ars_lon}kr
Eftersom du tjänar under brytpuknten betalar du ingen skatt!""")
else:
    komm_skatt = ars_lon * 0.2136
    lands_skatt = ars_lon * 0.1148
    lon_kvar = ars_lon - komm_skatt - lands_skatt
    print(f"""Utskrift:

Månadslön:  {lon}kr Årslön: {ars_lon}kr
Kommunal skatt: {round(komm_skatt)}kr
Landstingsskatt: {round(lands_skatt)}kr
Kvar efter skatt: {round(lon_kvar)}""")