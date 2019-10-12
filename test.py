import time
import math
import VL53L1X
from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()
tof.start_ranging(3)

def convertDistanceToBrightness(distance):
    brightness = (distance/(400*10))
    return brightness

# Avoid retina-searage!
def setBrightness(value):
    for x in range(0, matrix11x7.width):
            for y in range(0, matrix11x7.height):   
                matrix11x7.pixel(x, y, value)
        
while True:
    distance_in_mm = tof.get_distance()
    setBrightness(convertDistanceToBrightness(distance_in_mm))
    matrix11x7.show()