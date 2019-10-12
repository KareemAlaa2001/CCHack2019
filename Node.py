class Node:
    def __init__(self, nodeID):
        self.nodeID = nodeID
        self.dSens = DistanceSensor()
        self.lSens = LightSensor()
        self.led = LED()


    def loop(self):
        while(true):
            if(self.lSens.isDaytime() == False):
                if(self.dSens.getDistance() == DistanceSensor.FAR):
                    self.led.setBrightness(LED.BASE_BRIGHTNESS)

                






class DistanceSensor:

    FAR = 999999

    def getDistance(self):
        return DistanceSensor.FAR
        
class LightSensor:
    def isDaytime(self):
        return False

class LED:
    BASE_BRIGHTNESS = 0.5

    def setBrightness(self, brightness):
        pass