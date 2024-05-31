import time
import serial
arduinoData = serial.Serial('com4',9600)
time.sleep(1)
while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataReceived=arduinoData.readline()
    dataReceived=str(dataReceived,"utf-8")#'utf-8'
    dataReceived=dataReceived.strip('\r\n')
    print(dataReceived)