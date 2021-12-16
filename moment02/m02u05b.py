sekunder = int(input("Hur många sekunder ska omvandlas?: "))

minuter = sekunder // 60

timmar = minuter // 60

minuter = minuter - timmar * 60

sekunder = sekunder - timmar * 60 * 60 - minuter * 60

print(f"{timmar:02d}h{minuter:02d}m{sekunder:02d}s")