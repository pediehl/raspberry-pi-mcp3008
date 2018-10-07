import time, gpiozero

poti = gpiozero.MCP3008 (channel = 0)

while True :
 wert =  int((poti.raw_value / 1023) * 1000)
 print ("Der Poti steht auf" , wert , "Ohm")
 time.sleep (1)
