import time
import serial
arduinoData = serial.Serial('com4',9600)
time.sleep(1)
while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataReceived=arduinoData.readline()
    dataReceived=str(dataReceived,'utf-8')
    dataReceived=dataReceived.strip('\r\n')
    if len(dataReceived) > 1:
        dataReceived = dataReceived.split(",")
        temp = dataReceived[0]
        soilMoistValue = dataReceived[1]
        soilMoistPercentage = dataReceived[2]
        print(temp)
        print(soilMoistValue)
        print(soilMoistPercentage)
    
    if dataReceived == "OOF":
        dataReceived = "OON"
        dataReceived=dataReceived+'\r'
        arduinoData.write(dataReceived.encode())
    elif dataReceived == "OON":
        dataReceived = "OOF"
        dataReceived=dataReceived+'\r'
        arduinoData.write(dataReceived.encode())
    
    time.sleep(2)