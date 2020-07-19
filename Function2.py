import serial
import time
from time import sleep
from builtins import input
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rc
import matplotlib.animation as animation
import numpy as np
import os

def activate ():
    arduino = serial.Serial('COM3', 9600) # Establish the connection on a specific port
    arduino1 = serial.Serial('COM4', 9600) # Establish the connection on a specific port
    return arduino, arduino1

def data_accusition(arduino, arduino1):
    data = arduino.readline()[:-2]
    data1 = arduino1.readline()[:-2]
    return data,data1

def data_accusition1(arduino):
    data = arduino.readline()[:-2]
    return data
a = []
b = []


def activeteAccusition(a, b, t):
    # f =  open("./temp.txt", "w+")
    arduino, arduino1 = activate()
    i = 0
    c = data_accusition1(arduino)
    c = data_accusition1(arduino)
    close_time = time.time()+t
    move = time.time()+t/3
    down = time.time()+(t*2)/3
    j = 0
    while True:
        x,y = data_accusition1(arduino, arduino1)
        try:
            a.append(float(x))
            b.append(float(y))
        except:
            pass
        if time.time()>close_time:
            print("Selesai!")
            break
        elif time.time()>move and time.time()< down:
            if j == 0:
                print("Gerak!\r")
                j = j+1
        elif time.time()>down:
            if j == 1:
                print("Relax\r")
                j = j + 1
        # f.write(str(float(x)) + ","+str(float(y))+"\n")
        # f.close()
        # sleep(0.001)
    #     f =  open("./temp.txt", "a+")
    # f.close()
    return a,b

def createFile(data1, data2, name, ke):
    name = "./data/"+ name +"/" + name +  ke + ".txt"
    print("Membuat file.. "+str(name))
    f = open(str(name), "w+")
    i = 0
    while i < len(data1) and i < len(data2):
        f.write(str(data1[i])+","+ str(data2[i])+"\n")
        i = i+1
    f.close()

def plotData(data1, data2,  time, name, ke):
    # time = [a for a in range(time)]
    saveto = "./image/"+name+ke+".png"
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    fig, axs = plt.subplots(2)
    fig.suptitle = (name1)
    axs[0].plot(data1)
    axs[0].set_title("Sensor 1 (Bisep)")
    axs[0].axis(xlim = time, ylim = 6)
    axs[0].set_ylabel("Volt")
    axs[1].plot(data2, 'tab:red')
    axs[1].set_title("Sensor 2 (Bahu)")
    axs[1].set_xlim(left=0, right=time, auto=True)
    # axs[1].axis(xmin = 0, xmax = time, ymin = 0, ymax = 6)
    axs[1].set_xlabel("time(s)")
    axs[1].set_ylabel("Volt")
    plt.figure(figsize=(16,9), dpi=100)
    fig.savefig(saveto)

    plt.show()

def accusition(time):
    a = []
    b = []
    print("mengambil data dalam 5 detik...")
    sleep(2)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P2 (tangan naik setengah)")
    a,b = activeteAccusition(a,b,time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P3 (tangan naik penuh keatas)")
    a,b = activeteAccusition(a,b,time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P4 (tekuk tangan setengah)")
    a,b = activeteAccusition(a,b,time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P5 (tekuk tangan full)")
    a,b = activeteAccusition(a,b,time)
    time = time*4
    frequency = len(a)/time
    print ("Total Frequency : " + str(frequency))
    return a,b,time, frequency



def saveData(a, b, subjek, ke, time):
    print("Membuat data hasil... ")
    plotData(a, b, time, subjek, ke)
    createFile(a, b, subjek, ke)
    print("Pembuatan data selesai!")

def saveReadme(subjek, ke, freq, time):
    x = input("Mau beri ketentuan file? (Y/N)")
    if x == "y" or x == "Y":
        Readme = subjek + "-" + ke + " dengan frequency : " +str(freq) + " Dengan waktu : "  + str(time) 
        ReadmePath = "./data/" + subjek+ "/" + subjek +".txt"
        try: 
            os.mkdir(ReadmePath)
        except:
            pass
        f = open(ReadmePath, "a+")
        f.write(Readme)
        f.close()





        



