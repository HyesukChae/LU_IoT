# NeoPixel <rainbow.py>
import spidev
import numpy as np
import time
spi = spidev.SpiDev()
spi.open(0,0)
nLED = 8 # number of connected WS2812 
gData = np.zeros((nLED,3),dtype=np.uint8)
"""
T0H: 0.35 -> 2p=0.31 3p=0.47
T0L: 0.80 -> 6p=0.94 5p=0.78
T1H: 0.70 -> 4p=0.625 5p=0.78
T1L: 0.60 -> 4p=0.625 3p=0.47
"""

def write2812(spi,data):
    #print spi
    d=np.array(data).ravel()
    tx=np.zeros(len(d)*4, dtype=np.uint8)
    for ibit in range(4):
        #print ibit
        #print ((d>>(2*ibit))&1), ((d>>(2*ibit+1))&1)
        tx[3-ibit::4]=((d>>(2*ibit+1))&1)*0x60 + ((d>>(2*ibit+0))&1)*0x06 + 0x88
        #print [hex(v) for v in tx]
    #print [hex(v) for v in tx]
    spi.xfer(tx.tolist(), int(4/1.25e-6)) #works, on Zero (initially didn't?)
###########################################################################
def turnOnLamp(col):
    a, b, c = col
    write2812(spi, [[b, c, a]]*nLED)


def wheel(i):
    # Period of panorama is 0x300
    k = 0
    m = 0
    i = i%0x300; m = i&0xFF; k = i&0x300
    if k == 0x000:
        tb = 0xFF-m
        tg = m
        tr = 0
    elif k == 0x100:
        tb = 0
        tg = 0xFF-m
        tr = m
    else:
        tb = m
        tg = 0
        tr = 0xFF-m
    return(tg, tr, tb)

def rainbow(c, b, t):
    '''
    rainbow(step, length, time) display panorama color having period
    step: number of steps
    length: color distance(angle)
    t: delay time in each color step(mS unit)
    '''
    a = 0 # init angle
    for i in range(c):
        gData[0] = wheel(a+b*0); a += 1
        gData[1] = wheel(a+b*1); a += 1
        gData[2] = wheel(a+b*2); a += 1
        gData[3] = wheel(a+b*3); a += 1
        gData[4] = wheel(a+b*4); a += 1
        gData[5] = wheel(a+b*5); a += 1
        gData[6] = wheel(a+b*6); a += 1
        gData[7] = wheel(a+b*7); a += 1
        write2812(spi, gData)
        time.sleep(t/1000)
##########################################################################

#rainbow(1000, 80, 20) # rainbow color
color = 255, 0, 255 # set the color value.(B,G,R) (range:0~255)
turnOnLamp(color)