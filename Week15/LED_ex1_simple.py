from gpiozero import LED
from time import sleep

yellowR = LED(20)
yellowL = LED(26)
red = LED(21)

while True:

    yellowR.on()
    yellowL.on()
    red.on()
    sleep(5)

    yellowR.off()
    yellowL.off()
    red.off()
    sleep(1)
    
    