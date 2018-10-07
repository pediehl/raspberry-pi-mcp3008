import time, gpiozero

adc = gpiozero.MCP3008 (channel = 0)

while True:
 voltage = adc.voltage
 print("Spannung am Wassersensor: %.2f V" % voltage)
 time.sleep (1)
