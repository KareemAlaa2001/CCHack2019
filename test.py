import time
import math
import VL53L1X
from matrix11x7 import Matrix11x7
from ltr559 import LTR559
from smbus2 import SMBus
from firebase import firebase
from bme280 import BME280

matrix11x7 = Matrix11x7()
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()
tof.start_ranging(1)
ltr559 = LTR559()
bus = SMBus(1)  
bme280 = BME280(i2c_dev=bus)

objectInField = False
maxBright = False
myUrl = 'https://cchack2019-50339.firebaseio.com'
firebase = firebase.FirebaseApplication(myUrl, None)


def convertDistanceToBrightness(distance):
    brightness = float(distance/600.0)
    return 1 - brightness

def setBrightness(value):
    for x in range(0, matrix11x7.width):
            for y in range(0, matrix11x7.height):   
                matrix11x7.pixel(x, y, value)
                
brightness = 0.2
numPeds = 0
setBrightness(brightness)
matrix11x7.show()

while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()

    distance_in_mm = tof.get_distance()
    backgroundLight = ltr559.get_lux()

    if backgroundLight > 10.0:
        setBrightness(0)
        matrix11x7.show()
        if distance_in_mm <= 200 and objectInField == False:
            objectInField = True
        elif distance_in_mm > 200 and objectInField == True: # They've left
            objectInField = False
            numPeds += 1
            result = firebase.patch(myUrl + '/light1', {'numPeds' : numPeds})
            telemResult = firebase.patch(myUrl + '/light1', {'numPeds' : numPeds, 'temp' : temperature, 'pressure' : pressure, 'humidity' : humidity})
            print(str(numPeds) + " people have passed through here")
        
    else:
        if distance_in_mm <= 200 and objectInField == False: #There's someone in range
            print("person detected")
            objectInField = True
            brightness = 0.2
            if(maxBright == False):
                start = time.time()
                end = 2
                elapsed = 0
                while brightness < 0.95:
                    brightness += 0.04
                    setBrightness(brightness)
                    matrix11x7.show()
                    time.sleep(0.01)
                maxBright = True
            
        elif distance_in_mm > 200 and objectInField == True: # They've left
            objectInField = False
            numPeds += 1
            result = firebase.patch(myUrl + '/Peds', {'numPeds' : numPeds})
            telemResult = firebase.patch(myUrl + '/light1', {'numPeds' : numPeds, 'temp' : temperature, 'pressure' : pressure, 'humidity' : humidity})
            print(str(numPeds) + " people have passed through here")
            maxBright = False
            start = time.time()
            end = 2
            elapsed = 0
            while brightness > 0.2:
                brightness -= 0.04
                setBrightness(brightness)
                matrix11x7.show()
                time.sleep(0.01)
            maxBright = False
            setBrightness(0.2) #Set an ambient brightness default
        
        elif distance_in_mm > 200:
            setBrightness(0.2)
            
        matrix11x7.show()
