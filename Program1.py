import serial
import time
from time import sleep
from builtins import input

def data_accusition():
    data = arduino.readline()[:-2]
    return data


t = int(input("Input Time (s): "))
arduino = serial.Serial('COM3', 9600) # Establish the connection on a specific port
a =[]
close_time=time.time()+t
while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    a.append(int(float(data)))
    sleep(0.001)
    if time.time()>close_time:
        break
print(a)
# for i in a:
#     print(a[i])
# print(len(a))
# print(a)