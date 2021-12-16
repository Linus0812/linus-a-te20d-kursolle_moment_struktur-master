namn = input("Vad heter du? ").strip().capitalize()
age = int(input("Hur gamml är du? ").strip())
bokstav = namn[0]
if age >= 18:
    myndig = "Du är myndig"
else:
    myndig = "Du är inte myndig"
print(f"Ditt namn är: {namn}. Första bokstaven i ditt namn är {bokstav}. {myndig}")

