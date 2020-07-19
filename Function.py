import serial
import time
from time import sleep
from builtins import input
import matplotlib.pyplot as plt
import numpy as np


arduino = serial.Serial('COM3', 9600) # Establish the connection on a specific port
arduino1 = serial.Serial('COM4', 9600) # Establish the connection on a specific port

def data_accusition():
    data = arduino.readline()[:-2]
    data1 = arduino1.readline()[:-2]
    return data,data1

def data_accusition1():
    data = arduino.readline()[:-2]
    return data
a = []
b = []


def init(line):
    line.set_data([],[])
    return line

def animate(i, time, data, line):
    x = np.linspace(0, time, 1000)
    line.set_data(x, data)
    return line,

def activeteAccusition(t):
    c = data_accusition()
    c = data_accusition()
    close_time = time.time()+t
    move = time.time()+t/3
    down = time.time()+(t*2)/3
    j = 0
    while True:
        x,y = data_accusition()
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
        sleep(0.01)

    return a,b

def createFile(data1, data2, name, ke):
    name = "./data/"+ name + "-"+ ke + ".txt"
    print("Membuat file.. "+str(name))
    f = open(name, "w+")
    i = 0
    while i < len(data1) and i < len(data2):
        f.write(str(data1[i])+","+ str(data2[i])+"\n")
        i = i+1
    f.close()

def plotData(data1, data2,  time, name, ke):
    # time = [a for a in range(time)]
    saveto = "./image/"+name+"-"+ke+".png"
    name = "Hasil akusisi " + name + " percobaan ke-" + ke
    fig, axs = plt.subplots(2)
    fig.suptitle = (name)
    axs[0].plot(data1)
    axs[0].set_title("Sensor 1 (Bisep)")
    axs[0].axis(xmin = 0, xmax = time, ymin = 0, ymax = 6)
    axs[0].set_ylabel("Volt")
    axs[1].plot(data2, 'tab:red')
    axs[1].set_title("Sensor 2 (Bahu)")
    axs[1].axis(xmin = 0, xmax = time, ymin = 0, ymax = 6)
    axs[1].set_xlabel("time(s)")
    axs[1].set_ylabel("Volt")
    fig.savefig(saveto)
    plt.show()
    # plt.plot(data1)
    # plt.ylim(0,6)
    # plt.xlim(0, time)
    # plt.ylabel("volt")
    # plt.xlabel("time(s)")
    # plt.title(name)
    # plt.savefig(saveto)
    # plt.show()
def accusition(time):
    x = []
    y = []
    print("mengambil data dalam 5 detik...")
    sleep(2)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P2 (tangan naik setengah)")
    a,b = activeteAccusition(time)
    i = 0
    while i < len(a):
        x.append(a[i])
        y.append(b[i])
        i = i + 1
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P3 (tangan naik penuh keatas)")
    a,b = activeteAccusition(time)
    i = 0
    while i < len(a):
        x.append(a[i])
        y.append(b[i])
        i = i + 1
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P4 (tekuk tangan setengah)")
    a,b = activeteAccusition(time)
    i = 0
    while i < len(a):
        x.append(a[i])
        y.append(b[i])
        i = i + 1
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P5 (tekuk tangan full)")
    a,b = activeteAccusition(time)
    i = 0
    while i < len(a):
        x.append(a[i])
        y.append(b[i])
        i = i + 1
    time = time*4
    frequency = len(x)/time
    print ("Total Frequency : " + str(frequency))
    return x,y,time



def saveData(a, b, subjek, ke, time):
    print("Membuat data hasil... ")
    createFile(a, b, subjek, ke)
    plotData(a, b, time, subjek, ke)
    print("Pembuatan data selesai!")







        



