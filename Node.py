import VL53L1X
import time


class Node:
    def __init__(self, nodeID):
        self.nodeID = nodeID
        self.dSens = DistanceSensor(4,0x29)
        self.lSens = LightSensor()
        self.led = LED()


    def loop(self):
        while(True):
            if(self.lSens.isDaytime() == False):
                if(self.dSens.checkDistance() == DistanceSensor.FAR):
                    self.led.setBrightness(LED.BASE_BRIGHTNESS)
                else:
                    self.manageBrightnessWithDistance()

    def manageBrightnessWithDistance(self):



class DistanceSensor:
  
    #class attribute for distance value when nothing detected
    FAR = 9999999
    MAX_DISTANCE = 4000

    # initializer / instance attributes
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

        #open and start ranging sensor
        self.tof = VL53L1X.VL53L1X(i2c_bus=bus, i2c_address=address)
        #might need to be global, hoping declaring outside of func makes it global

    def checkDistance(self):
        #get distance from sensor, do processing
        #return distance value from sensor
        pass
    
    def test(self):
        self.tof.open() # Initialise the i2c bus and configure the sensor
        self.tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
        distance_in_mm = self.tof.get_distance()
        print("Distance: " + distance_in_mm)
        time.sleep(0.1)
        self.tof.stop_ranging()

    

        
class LightSensor:
    def isDaytime(self):
        return False

class LED:
    BASE_BRIGHTNESS = 0.5

    def setBrightness(self, brightness):
        pass

