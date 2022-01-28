def mult():
    tal = int(input("Vad är dit tal?"))
    if tal <= 15:
        for i in range(1, tal+1):
            summa1 = 1 * i
            summa2 = 2 * i
            summa3 = 3 * i
            summa4 = 4 * i
            summa5 = 5 * i
            summa6 = 6 * i
            summa7 = 7 * i
            summa8 = 8 * i
            summa9 = 9 * i
            summa10 = 10 * i
            print(f"{summa1:5}{summa2:5}{summa3:5}{summa4:5}{summa5:5}{summa6:5}{summa7:5}{summa8:5}{summa9:5}{summa10:5}")

    else:
        mult()

mult()