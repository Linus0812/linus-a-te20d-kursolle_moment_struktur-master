# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.

# exchange_rate dollar_to_sek = 8,82
# det ska vara understreck mellan rate och dollar och det ska var punkt inte komma tecken i 8,82
exchange_rate_dollar_to_sek = 8.82

# print(Detta är ett program där vi kan växla mellan SEK & dollar)
# det är inga fnuttar i parenteserna
print("Detta är ett program där vi kan växla mellan SEK & dollar")

# 1sek = input("Hur många SEK vill du växla till dollar: )
# en variabel kan inte börja med en siffra och det är inget slut fnutt inom paerentesen och det ska var en interger inte string
sek = int(input("Hur många SEK vill du växla till dollar: "))

# dollar = 1sek / exchange_rate_dollar_to_sek
# nu funkade inte "1sek" längre eftersom variabeln bytte namn
dollar = sek / exchange_rate_dollar_to_sek

# print("Du ville växla {0} SEK vilket blir {1} dollar.".format(1sek, dollar)
# "1sek" variabeln funkar inte här heller längre och det saknades en parentes i slutet
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek, dollar))