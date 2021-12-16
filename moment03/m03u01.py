from time import localtime

t = localtime()

timma = t.tm_hour

if timma >= 16:
    print("skoldagen är slut")
else:
    print("Skoldagen är inte slut")