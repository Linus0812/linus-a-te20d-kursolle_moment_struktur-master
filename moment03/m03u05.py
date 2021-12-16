from time import localtime

t = localtime()

timma = t.tm_hour
minut = t.tm_min
tid = timma + minut

if 0 > tid >= 60:
    print("Skoldagen är slut")
elif 0 <= tid < 23:
    print("Skoldagen har inte påbörjat")
else:
    print("Skoldagen pågår")