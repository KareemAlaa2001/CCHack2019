import VL53L1X
import time

class DistanceSensor:
    #class attribute
    tof = ""

    # initializer / instance attributes
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

        #open and start ranging sensor
        tof = VL53L1X.VL53L1X(i2c_bus=bus, i2c_address=address)
        #might need to be global, hoping declaring outside of func makes it global

    def checkDistance(self):
        #get distance from sensor, do processing
        #return distance value from sensor
        pass
    
    def test(self):
        tof.open() # Initialise the i2c bus and configure the sensor
        tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
        distance_in_mm = tof.get_distance()
        print("Distance: " + distance_in_mm)
        time.sleep(0.1)
        tof.stop_ranging()