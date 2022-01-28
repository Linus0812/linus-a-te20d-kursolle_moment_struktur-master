sida_1 = int(input("Storlek sida 1: "))
sida_2 = int(input("Storlek sida 2: "))

storlek = sida_1 * sida_2

if sida_1 == sida_2:
    kvadrat = "Detta är en kvadrat"
else:
    kvadrat = "Detta är inte en kvadrat"

print(f"{kvadrat}. Storleken är {storlek}cm^2")
print("Rektangelns volym med höjden 1-10 cm:")
for i in range(1, 10):
    print(i * storlek)