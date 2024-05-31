import serial
import time

# Set the serial port
port = "/dev/ttyACM10"
baudrate = 9600

# Create a serial object
ser = serial.Serial(port, baudrate)

# Write a byte to the Arduino
ser.write(b"1")

# Wait for 1 second
time.sleep(1)

# Read a byte from the Arduino
#data = ser.read()

# Print the data
#print(data)