import time, gpiozero

ldr = gpiozero.MCP3008 (channel = 0)

while True :
 wert =  int((ldr.raw_value / 1023) * 1000)
 print ("Der Wert am Foto-Widerstand beträgt: " , wert , "Ohm")
 time.sleep (1)
