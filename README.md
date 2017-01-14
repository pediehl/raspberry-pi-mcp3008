# Raspberry Pi: Raspberry Pi und MCP3008 (Analog-Digital Wandler)

## Einleitung
Viele Sensoren bieten keine digitale Schnittstelle und sind nur analog auslesbar.
Der Raspberry Pi mit seinen GPIOs kann keine analogen Signale auslesen. Um analoge Sensoren am Raspberry Pi auslesen zu könnenen, benötigen wir einen Analog-Digital Wandler z.B. den MCP3008. Damit können bis zu 8 analoge Eingänge über den SPI Bus am Raspberry Pi ausgelesen werden.

## Vorbereitung
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev git

Lade dir jetzt das passende Github-Repository für die weihnachtskarte herunter

cd Documents
git clone https://github.com/pediehl/raspberry-pi-mcp3008.git

```
Bevor es weiter geht, muss der SPI Bus noch aktiviert werden, wenn das noch nicht geschehen ist. Aktiviere in der Konfiguration des Raspberry Pi unter dem Punkt „Schnittstellen“ die Option „SPI“. Starte danach zur Sicherheit das System neu (Reboot).

![](images/spi_raspberry-pi.png)

## Aufbau
![](images/mcp3008_raspberry_Steckplatine.png)

![](images/mcp3008_Schaltplan.png)

MCP3008|Raspberry Pi
--|--
MCP3008 VDD | Raspberry Pi 3.3 V
MCP3008 VDD | Raspberry Pi 3.3 V
MCP3008 VREF | Raspberry Pi 3.3 V
MCP3008 AGND | Raspberry Pi GND
MCP3008 CLK | Raspberry Pi SCLK
MCP3008 DOUT | Raspberry Pi MISO
MCP3008 DIN | Raspberry Pi MOSI
MCP3008 CS/SHDN | Raspberry  Pi CE0

## Beispiele starten

Auf deinem Raspberry solltest du jetzt unter Documents einen weiteren Ordner  haben. Öfnne den Ordner raspberry-pi-mcp3008 und gehe auf code. Hier gibt es zwei Python-Skripte:

read_multiple_channels.py (Beispieldatei- nur diese Datei ausführen !)
MCP3008.py (notwendige Python-Klasse - muss sich im gleichen Verzeichnis befinden)

## Wie starte ich das Python-Skript auf meinem Raspbery Pi?

Wechsel in den Ordner Documents/raspberry-pi-mcp3008/code/
Wähle die Datei "read_multiple_channels.py" und starte die Datei mit einem Doppel-Klick.
Starte das Programm mit F5.
