import time
import neopixel
from machine import Pin

LED = neopixel.NeoPixel(Pin(21),1)
 
while True:
    LED[0] = (255, 0, 0)
    LED.write()
    time.sleep(0.5)
    LED[0] = (255, 255, 0)
    LED.write()
    time.sleep(0.5)
    LED[0] = (0, 255, 0)
    LED.write()
    time.sleep(0.5)
    LED[0] = (0, 255, 255)
    LED.write()
    time.sleep(0.5)
    LED[0] = (0, 0, 255)
    LED.write()
    time.sleep(0.5)
    LED[0] = (255, 0, 255)
    LED.write()
    time.sleep(0.5)

    



