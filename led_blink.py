from pyfirmata import Arduino
import time

board = Arduino('COM10')

pin_8 = board.get_pin('d:8:o')

#while True:
pin_8.write(1)
    #time.sleep(1)
    #pin_8.write(1)
    #time.sleep(1)
