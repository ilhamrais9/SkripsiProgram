import serial
from time import sleep

arduino = serial.Serial('COM3',74800)
while True:
    data = arduino.readline()[:-2]
    print(data)
    sleep(2)