from cmath import pi
import math

radie = int(input("Vad har cirkeln för radie? "))


def area():
    global area
    
    area = radie * radie * pi

def omkrets():
    global omkrets

    omkrets = radie * 2 * pi

area()
print(f"Arean på cirkeln är {round(area)}m^2")
omkrets()
print(f"Omkretsen på cirkeln är {round(omkrets)}m")
