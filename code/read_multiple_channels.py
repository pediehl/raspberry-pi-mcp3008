from MCP3008 import MCP3008
import time
adc = MCP3008()

while True:
    wassersensor = adc.read( channel = 0 )
    poti = adc.read( channel = 1 )
    print("Spannung Wassersensor: %.2f V" % (wassersensor / 1023.0 * 3.3) )
    print("Widerstand am Potentiometer: %.2f K\u2126" % (poti / 1023) )
    print("Widerstand am Potentiometer: %.0f \u2126" % (poti / 1023.0 + 1000))
    time.sleep(3)
