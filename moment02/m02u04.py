antal_pennor = float(input("Hur många pennor har du köpt? "))
antal_äpplen = float(input("Hur många äpplen har du köpt? "))
vikt_äpplen = float(input("Hur många gram väger dina äpplen? "))

pris_för_pennor = float(input("Vad är priset för pennor? "))
pris_för_äpplen = float(input("Vad är kg priset för äpplen? ")) / 100

pris_pennor = antal_pennor * pris_för_pennor
pris_äpplen = antal_äpplen * vikt_äpplen * pris_för_äpplen

total_vikt_äpplen = antal_äpplen * vikt_äpplen
totalt = pris_pennor + pris_äpplen


print(f"""

Penna, {antal_pennor}st á {pris_för_pennor}kr           {pris_pennor} kr
Äpplen, {total_vikt_äpplen}g á {pris_för_äpplen} kr/kg    {pris_äpplen} kr
-----------------------------------
Summa                      {totalt} kr""")