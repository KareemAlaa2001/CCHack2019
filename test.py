import time
import math

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
for x in range(0, matrix11x7.width):
        for y in range(0, matrix11x7.height):   
            matrix11x7.pixel(x, y, 1)
            
matrix11x7.show()