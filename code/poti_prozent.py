import time, gpiozero

poti = gpiozero.MCP3008 (channel = 0)

while True :
 wert = int ( poti.value * 100)
 print ("Der Poti steht auf" , wert , "%")
 time.sleep (1)
