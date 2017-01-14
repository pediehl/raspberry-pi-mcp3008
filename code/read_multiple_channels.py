from MCP3008 import MCP3008
import time
adc = MCP3008()

while True:
    value = adc.read( channel = 0 )
    poti = adc.read( channel = 1 )
    print("Anliegende Spannung: %.2f V" % (value / 1023.0 * 3.3) )
    print("Widerstand am Potentiometer: %.2f \u2126" % (poti / 1023) )
    time.sleep(3)
