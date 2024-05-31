import serial
arduinoData=serial.Serial('com4',9600)

while True:
    command=input("Please Enter Your Command: ")
    command=command+'\r'
    arduinoData.write(command.encode())