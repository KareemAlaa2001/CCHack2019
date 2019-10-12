from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font3x5
import time

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)
matrix11x7.write_string(" Hello World!", y=1, font=font3x5)

while True:
    # Show the buffer
    matrix11x7.show()
    # Scroll the buffer content
    matrix11x7.scroll()
    # Wait for 0.1s
    time.sleep(0.1)