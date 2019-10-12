from ltr559 import LTR559
import time

class LightSensor:
    currentBrightness = float()
    isDaytime = bool()
    ltr559 = LTR559()

    def getLux(self):#returns light levels
        lux = LTR559.get_lux()
        return lux

    
    def isDaytime(self):#check whether light levels are about 50lux /daytime
        lux = getLux()
        
        if lux < 50:
            isDaytime = False
            return False
        else:
            isDaytime = True
            return True
        

        



    



