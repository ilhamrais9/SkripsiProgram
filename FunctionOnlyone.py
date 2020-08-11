import serial
import time
from time import sleep
from builtins import input
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rc
import matplotlib.animation as animation
import numpy as np
import os
from datetime import datetime 
from scipy import fftpack
from scipy.signal import butter, lfilter, firwin, freqz, welch, filtfilt, group_delay
from math import sqrt
import cmath

def activate():
    arduino = serial.Serial('COM8', 74880) # Establish the connection on a specific port
    arduino1 = serial.Serial('COM6', 74880) # Establish the connection on a specific port
    return arduino, arduino1

def activate1():
    arduino = serial.Serial('COM3', 115200) # Establish the connection on a specific port
    return arduino

def activate2():
    arduino1 = serial.Serial('COM8', 115200) # Establish the connection on a specific port
    return arduino1

def data_accusition(arduino, arduino1):
    data = arduino.readline()[:-2]
    data1 = arduino1.readline()[:-2]
    return data,data1

def data_accusition1(arduino):
    data = arduino.readline()[:-2]
    return data

def data_accusition2(arduino):
    data1 = arduino.readline()[:-2]
    return data1

def activeteAccusition(a,b,t):
    # f =  open("./temp.txt", "w+")
    arduino, arduino1 = activate()
    i = 0
    c = data_accusition(arduino, arduino1)
    c = data_accusition(arduino, arduino1)
    close_time = time.time()+t
    move = time.time()+t/3
    down = time.time()+(t*2)/3
    j = 0
    while True:
        x,y = data_accusition(arduino, arduino1)
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
    return a,b

def addData(data1, data2):
    data=[]
    i=0
    j=0
    jumlah=len(data1)
    jumlahAll = (len(data1)+len(data2))
    while jumlah > i :
        data.append(data1[i])
        i = i + 1
        j = j + 1
    i = 0
    while jumlahAll > j:
        data.append(data2[i])
        i = i+1
        j = j+1
    return data

def activeteAccusition1(a, t):
    # f =  open("./temp.txt", "w+")
    arduino = activate1()
    i = 0
    c = data_accusition1(arduino)
    c = data_accusition1(arduino)
    close_time = time.time()+t
    move = time.time()+t/3
    down = time.time()+(t*2)/3
    j = 0
    while True:
        x = data_accusition1(arduino)
        try:
            a.append(float(x))
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
    return a

def activeteAccusition2(a, t):
    # f =  open("./temp.txt", "w+")
    arduino = activate2()
    i = 0
    c = data_accusition2(arduino)
    c = data_accusition2(arduino)
    close_time = time.time()+t
    move = time.time()+t/3
    down = time.time()+(t*2)/3
    j = 0
    while True:
        x = data_accusition2(arduino)
        try:
            a.append(float(x))
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
    return a

def check():
    arduino, arduino1 = activate()
    while True:
        try: 
            data_accusition(arduino, arduino1)
            break
        except:
            print("Module Belum terconnect")
            i=input("coba lagi? y/n")
            if i == "y":
                pass
            else:
                exit()



# def activeteAccusition(a, t):
#     # f =  open("./temp.txt", "w+")
#     i = 0
#     arduino = activate1()
#     c = data_accusition1(arduino)
#     c = data_accusition1(arduino)
#     close_time = time.time()+t
#     move = time.time()+t/3
#     down = time.time()+(t*2)/3
#     j = 0
#     while True:
#         x = data_accusition1(arduino)
#         try:
#             a.append(float(x))
#         except:
#             pass
#         if time.time()>close_time:
#             print("Selesai!")
#             break
#         elif time.time()>move and time.time()< down:
#             if j == 0:
#                 print("Gerak!\r")
#                 j = j+1
#         elif time.time()>down:
#             if j == 1:
#                 print("Relax\r")
#                 j = j + 1
#         # f.write(str(float(x)) + ","+str(float(y))+"\n")
#         # f.close()
#         sleep(0.001)
#     #     f =  open("./temp.txt", "a+")
#     # f.close()
#     return a

def writeToDatabase(subjek, data, time, freq, ave, ket, ke):
    f = open("./data/database.txt", "a+")
    write = (subjek, data, time, freq, ave, ket, ke)
    f.write("\n", str(write))
    f.close()



def create_readme (subjek,folder, time, freq, ave, ket, ke):
    f = open("./data/" + str(folder) +  "/README.txt", "a+")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    t = ("date and time =", dt_string)
    write = str("\nData " + subjek + " dengan Freq : " + freq + " denga waktu : " + time + " avarege data: " + ave + " " + ket + " "+ str(t) + " Destinasi: " + ke) 
    f.write(write)
    f.close()

def ave(data):
    return (sum(data)/len(data))


def createFile(data1, name, ke, subjek="TEST"):
    name = "./data/"+ str(subjek)+ "/data/" + name +  ke + ".txt"
    print("Membuat file.. "+str(name))
    f = open(str(name), "w+")
    i = 0
    while i < len(data1) :
        f.write(str(data1[i]))
        i = i+1
    f.close()
    
def createFile2(data1, data2, name, ke, subjek="TEST", INFO=False):
    if INFO == True:
        name = str("./data/"+ str(subjek)+ "/" + name +  ke + ".txt")
    else:
        name = str("./data/"+ str(subjek)+ "/data/" + name +  ke + ".txt")

    print("Membuat file.. "+str(name))
    f = open(str(name), "w+")
    i = 0
    while i < len(data1) and i < len(data2):
        f.write(str(data1[i])+","+ str(data2[i])+"\n")
        i = i+1
    f.close()

def plotData(data1, time, name, ke):
    # time = [a for a in range(time)]
    saveto = "./image/"+name+ke+".png"
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    # fig, axs = plt.plots(1)
    plt.figure(figsize=(18,6), )
    plt.suptitle = (name1)
    plt.plot(data1)
    # plt.rcParams('seaborn-deep')
    # plt.set_title("Sensor 1 (Bisep)")
    plt.title(name1)
    # plt.xscale()
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")

    plt.savefig(saveto)
    plt.show()
    plt.close()
def plotData20(data1, data2, time, j, name, ke):
    # time = [a for a in range(time)]
    saveto = "./image/"+name+ke+".png"
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    i = 0
    h = (time/(time/j)/3)
    oi = []
    o = []
    o1 = []
    q = 1
    o.append(0)
    o1.append(0)
    while i <= time:
        oi.append(str(i))
        o.append(int((len(data1)*q)/20))
        o1.append(int((len(data2)*q)/20))
        i = i + j
        q = q + 1 
        
    grid = plt.GridSpec(2, 1, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
    plt.figure(figsize=(18,6))
    plt.subplot(grid[0,0])
    plt.plot(data1)
    plt.title("Tangan Kanan {}")
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.title("Tangan Kiri")
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o1, oi)
    plt.savefig(saveto)
    plt.show()
    plt.close
    return (saveto)

j = []
k = []
def plotData2VOLT(data1, data2, time, name, ke,subjek="TEST", limx=False, limy=False,fillb=False, show=False, detail=True, save=False, printInfo=False):
    saveto = str("./data/"+ str(subjek) + "/image/"+name+ke+".png")
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
    o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    freq = int(len(data1)/int(time))
    freq2 = int(len(data2)/int(time))
    ket1 = str("Tangan Kanan \nFreq : " + str(freq))
    ket2 = str("Tangan Kiri \nFreq :  " + str(freq2))
    if fillb == True:
        i=0
        P=[]
        while i<len(data1):
            P.append(i)
            i=i+1
    grid = plt.GridSpec(2, 1, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
    plt.figure(figsize=(18,6))
    plt.subplot(grid[0,0])
    plt.plot(data1)
    if detail == True:
        plt.plot(data1.index(max(data1[int(len(data1)/3):int(len(data1)*2/3)])), max(data1[int(len(data1)/3):int(len(data1)*2/3)]), 'x', color='red', linewidth=2)
    if fillb == True:
        plt.fill_between(P[int(len(P)/3):int(len(P)*2/3)], data1[int(len(P)/3):int(len(P)*2/3)], 0,color='aqua')
    plt.title(ket1)
    plt.grid()
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o, oi)
    if limx != False:
        plt.xlim(limx)
    if limy != False:
        plt.ylim(limy)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    if detail == True:
        plt.plot(data2.index(max(data2[int(len(data2)/3):int(len(data2)*2/3)])), max(data2[int(len(data2)/3):int(len(data2)*2/3)]), 'x', color='red', linewidth=2)
    if fillb == True:        
        plt.fill_between(P[int(len(P)/3):int(len(P)*2/3)], data2[int(len(P)/3):int(len(P)*2/3)], 0,color='aqua')
    plt.title(ket2)
    plt.ylabel("Volt")
    plt.grid()
    plt.xlabel("Waktu (s)")
    plt.xticks(o1, oi)
    if limx != False:
        plt.xlim(limx)
    if limy != False:
        plt.ylim(limy)
    if save == True:
        plt.savefig(saveto)
    if show ==True:
        plt.show()
    plt.close()
    j.append(freq)
    k.append(freq2)
    if printInfo == True:   
        print("Freq A : ", freq, " Freq B : ", freq2)
        print("Freqlist A: ", j)
        print("Freqlist B: ", k)
    return (saveto)

def plotData2ADC(data1, data2, time, name, ke,subjek="test",ylimit=False, show=False, save=False):
    if ylimit == False:
        ylimit = findplotlim(data1, data2)
    saveto = str("./data/"+ str(subjek)+ "/image/" +str(name)+str(ke)+".png")
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
    o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    freq = int(len(data1)/int(time))
    freq2 = int(len(data2)/int(time))
    ket1 = str("Tangan Kanan \nFreq : " + str(freq))
    ket2 = str("Tangan Kiri \nFreq :  " + str(freq2))
    # fig, axs = plt.plots(1)
    grid = plt.GridSpec(2, 1, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
    plt.figure(figsize=(18,6))
    plt.subplot(grid[0,0])
    plt.plot(data1)
    plt.title(ket1)
    plt.ylim(ylimit)
    plt.grid()
    plt.ylabel("ADC")
    plt.xlabel("Waktu (s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.ylim(ylimit)
    plt.title(ket2)
    plt.ylabel("ADC")
    plt.grid()
    plt.xlabel("Waktu (s)")
    plt.xticks(o1, oi)
    if save == True:
        plt.savefig(saveto)
    if show ==True:
        plt.show()
    plt.close
    j.append(freq)
    k.append(freq2)
    print("Freq A : ", freq, " Freq B : ", freq2)
    print("Freqlist A: ", j)
    print("Freqlist B: ", k)
    return (saveto)


# def plotData2(data1, data2, time, name, ke):
#     # time = [a for a in range(time)]
#     saveto = str("./image/"+name+ke+".png")
#     name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
#     o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
#     o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
#     oi =["0", str(time/3), str((time*2)/3), str(time)]
#     # fig, axs = plt.plots(1)
#     grid = plt.GridSpec(2, 1, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
#     plt.figure(figsize=(18,6))
#     plt.subplot(grid[0,0])
#     plt.plot(data1)
#     plt.title("Tangan Kanan {}")
#     plt.ylabel("Volt")
#     plt.xlabel("Waktu (s)")
#     plt.xticks(o, oi)
#     plt.subplot(grid[1,0])
#     plt.plot(data2)
#     plt.title("Tangan Kiri")
#     plt.ylabel("Volt")
#     plt.xlabel("Waktu (s)")
#     plt.xticks(o1, oi)
#     plt.savefig(saveto)
#     plt.show()
#     plt.close
#     return (saveto)


def plotData3(data1, data2, data3, time, name, ke):
    # time = [a for a in range(time)]
    saveto = "./image/"+name+ke+".png"
    name1 = "Hasil akusisi " + name + " percobaan ke-" + ke
    o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
    o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
    o2 = [0, len(data3)/3, (len(data3)*2)/3, len(data3)]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    # fig, axs = plt.plots(1)
    grid = plt.GridSpec(3, 1, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
    plt.figure(figsize=(18,10))
    plt.subplot(grid[0,0])
    plt.plot(data1)
    plt.title("Tangan Kanan {}")
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.title("Tangan Kiri")
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o1, oi)
    plt.subplot(grid[2,0])
    plt.plot(data3)
    plt.title("Tangan Kiri")
    plt.ylabel("Volt")
    plt.xlabel("Waktu (s)")
    plt.xticks(o2, oi)
    plt.savefig(saveto)
    plt.show()
    plt.close

def plotFigure2(a, b, c,d,e,f,FullA, FullB, time, ke, name):
    name = "./data/" + name +  ke + ".png"
    j = []
    x = []
    j.append(x)
    j.append(a)
    j.append(b)
    j.append(c)
    j.append(d)
    j.append(e)
    j.append(f)
    j.append(FullA)
    j.append(FullB)
    data = len(f)   
    o = [0, data/3, (data*2)/3, data]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    grid = plt.GridSpec(5, 2, wspace=0.2, hspace=1.5, left=0.05, bottom=0.07, right=0.95, top=0.88)
    fig = plt.figure(figsize=(20,20))
    plt.style.use('seaborn-pastel')
    plt.subplot(grid[0,0])
    plt.plot(a)
    plt.title("A")
    plt.ylabel("Volt")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    # plt.ylim([0,6])
    plt.subplot(grid[0,1])
    plt.plot(b)
    # plt.ylim([0,6])
    plt.title("B")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(c)
    # plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.title("C")
    plt.ylabel("Volt")
    plt.xticks(o, oi)
    plt.subplot(grid[1,1])
    plt.plot(d)
    # plt.ylim([0,6])
    plt.title("D")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[2,0])
    plt.plot(e)
    # plt.ylim([0,6])
    plt.title("E")
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.xticks(o, oi)
    plt.subplot(grid[2,1])
    plt.plot(f)
    plt.xlabel("time(s)")
    # plt.ylim(0,6)
    plt.title("F")
    plt.xticks(o, oi)
    plt.subplot(grid[3,:2])
    plt.plot(FullA)
    # plt.ylim(top=6, bottom=0)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaA")
    plt.subplot(grid[4,:2])
    plt.plot(FullB)
    # plt.ylim(top=6, bottom=0)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaB")
    plt.savefig(name)
    plt.show()
    plt.close

def plotFigure(self, a, b, c,d,e,f,FullA, FullB, time):
    fig, axs = plt.subplot(4,2)
    axs[0,0].plot(a)
    axs[0,1].plot(b, 'tab:blue')
    axs[1,0].plot(c)
    axs[1,1].plot(d, 'tab:blue')
    axs[2,0].plot(e)
    axs[2,1].plot(f, 'tab:blue')
    axs[3,0].plot(FullA)
    axs[4,0].plot(FullB)
def accusition(self, time):
    a = []
    print("mengambil data dalam 5 detik...")
    sleep(2)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P2 (tangan naik setengah)")
    a = activeteAccusition(a, time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P3 (tangan naik penuh keatas)")
    a = activeteAccusition(a, time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P4 (tekuk tangan setengah)")
    a = activeteAccusition(a,time)
    print("mengambil data dalam 3 detik...")
    sleep(3)
    print("Pengambilan data dimulai!")
    print("siap siap mengambil data gerakan P5 (tekuk tangan full)")
    a = activeteAccusition(a,time)
    time = time*4
    frequency = len(a)/time
    print ("Total Frequency : " + str(frequency))
    return a,time, frequency



def saveData(a, subjek, ke, time):
    print("Membuat data hasil... ")
    plotData(a, time, subjek, ke)
    createFile(a, subjek, ke)
    print("Pembuatan data selesai!")

def saveReadme(self, subjek, ke, freq, time):
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


def ADCtoVolt(a):
    ai = []
    for element in a:
        ai.append(5*float(element)/1024)
    return ai

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def recrification(a, Ave=False):
    mA = []
    A = ave(a)
    for element in a:
        if Ave == True:
            c = element-A
        else:
            c = element
        mA.append(c*c)
    return(mA)

def movingAvarage(a,ws):
    i = 0
    r= []
    while i < len(a) - ws + 1:
        tW = a[i:i+ws]
        wA = sum(tW)/ws
        r.append(wA)
        i += 1
    return r

def RMS(a, ws):
    rms = []
    i = 0
    while i < len(a) - ws + 1:
        tW = a[i:i+ws]
        t2 = sum(tW)/ws
        wA = sqrt(t2*t2)
        rms.append(wA)
        i += 1 
    return(rms)

def bandpass_firwin(ntaps, lowcut, highcut, fs, window='hamming'):
    nyq =  0.5 * fs
    taps = firwin(ntaps, [lowcut, highcut], nyq=nyq, pass_zero=False,
                  window=window)
    return taps

def bandpass_firwin_filter(data, ntaps, lowcut, highcut, fs):
    taps = bandpass_firwin(ntaps, lowcut, highcut, fs)
    # w,h = freqz(taps, 1, worN=2000)
    y = filtfilt(taps,1.0, data)
    # y = lfilter(taps,1.0, data)
    return y[int(fs):]

def showResponFilter(taps, lowcut, highcut,fs):
    plt.figure(1, figsize=(12,9))
    plt.clf()
    rect = plt.Rectangle((lowcut,0), highcut-lowcut, 1.0, facecolor="#60ff60", alpha=0.2)
    plt.gca().add_patch(rect)
    w,h = freqz(taps, 1, worN=2000)
    plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="Respon Filter")
    plt.xlim(0, fs+fs/10)
    plt.ylim(0, 1.1)
    plt.grid(True)
    plt.legend()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.title('Frequency response of FIR filter')
    plt.show()
    plt.close()

def signalProcessingFirwin (signal, t, lowcut,highcut,ws, Ave=False, NilaiRMS = 500, process = False , show=False, save=False, RMS1 = True):
    fs = len(signal)/t
    if process == True :
        print("filtering..")
    signal = bandpass_firwin_filter(data = signal, ntaps=1300, lowcut=lowcut, highcut=highcut,fs= int(len(signal)/t))
    signal = signal.tolist()
    if process == True : 
        print("Recrificationing...")
    signal = recrification(signal, Ave=Ave)
    if process == True :
        print("Moving avareging...")
    signal = movingAvarage(signal, ws)
    if RMS1 == True:
        if process == True :
            print("Processing RMS...")
        signal = RMS(signal, NilaiRMS)
    return signal

def fastFourierTransform(signal, time, name="TEST", plot=True, save=True,fs = True):
    if fs == True:
        fs = len(signal)/time
    Signal = fftpack.fft(signal)
    freqs = fftpack.fftfreq(len(signal))*fs
    if plot == True:
        fig, ax = plt.subplots()
        plt.plot(freqs, abs(Signal))
        plt.xlabel('Frequency in Hz')
        plt.xlim(-1, 520)
        plt.ylabel('Frequency Domain (spectrum) Magnitude')
        plt.grid(True)
        n = str("./image/"+ str(name) +"FFT")
        plt.savefig(n)
        if save == True:
            plt.show()
        plt.close()
    return Signal, freqs

    
def welchFunction(data, time):
    fs = data/time
    f , Pxx_den = welch(data, fs)
    plt.semilogy(f, Pxx_den)
    # plt.ylim([0.5e-3, 1])
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()
    plt.close()

def ReadFile(dataName, subjek="TEST", ADC = True):
    path = str("./data/" + str(subjek) + "/data/" + dataName + ".txt")
    with open(path) as f:
        content =f.readlines()
    i = 0
    c = []
    d = []
    while i < len(content):
        a,b = content[i].split(',')
        if ADC == True:
            a = (5*float(a))/1024
            b = (5*float(b.strip()))/1024
        if ADC == False:
            a = float(a)
            b = float(b.strip())
        c.append(a)
        d.append(b)
        i = i + 1
    return c,d 


def GetInfo(name1, j, time,subjek="TEST" , ke="", printInfo=True):
    Ap = []
    Bp = []
    At = []
    Bt = []
    Ai = []
    Bi = []
    Pa = []
    Pb = []
    k = 1
    for i in range(j):
        if k != 90:
            name = str(name1 + str(k))
            # print("Processing Data.. ", name)
            a,b = ReadFile(name, subjek=subjek)
            ai = signalProcessingFirwin(a,15,20,500,500,Ave=False)
            bi = signalProcessingFirwin(b,15,20,500,500,Ave=False)
            peak1 = max(ai[int(len(ai)/3):int(len(ai)*2/3)])
            peak2 = max(bi[int(len(bi)/3):int(len(bi)*2/3)])
            peakt1 = (ai.index(max(ai[int(len(ai)/3):int(len(ai)*2/3)]))/len(ai))*time
            peakt2 = (bi.index(max(bi[int(len(bi)/3):int(len(bi)*2/3)]))/len(bi))*time
            ave1 = ave(ai)
            ave2 = ave(bi)
            P1 = sum(ai[int(len(ai)/3):int(len(ai)*2/3)])
            P2 = sum(bi[int(len(bi)/3):int(len(bi)*2/3)])
            Pa.append(P1)
            Pb.append(P2)
            Ap.append(peak1)
            Bp.append(peak2)
            At.append(peakt1)
            Bt.append(peakt2)
            Ai.append(ave1)
            Bi.append(ave2)
        k = k + 1 
        i = i + 1
    createFile2(Ai,Bi, str(str(name) + "RataRataData"), ke, subjek=subjek)
    plotInfo(Ai, Bi, j,xl="Data Pengambilan ke", yl="",subjek=subjek, name=str(str(name)+"RataRataData" ), title="Rata rata data")
    createFile2(Ap,Bp, str(str(name) +"PeakValueData"), ke, subjek=subjek)
    plotInfo(Ap, Bp, j,xl="Data Pengambilan ke", yl="Volt",subjek=subjek, name=str(str(name)+"PeakValue"), title="Nilai Peak data")
    createFile2(At, Bt, str(str(name) + "WaktuPeakData"), ke, subjek=subjek)
    plotInfo(At, Bt, j,xl="Data Pengambilan ke", yl="Waktu (s)",subjek=subjek, name=str(str(name)+"WaktuPeakData"), title="Waktu Peak Data")
    createFile2(Pa, Pb, str(str(name)+"LuasData"), ke, subjek=subjek)
    plotInfo(Pa, Pb, j,xl="Data Pengambilan ke", yl="",subjek=subjek, name=str(str(name)+"LuasData"), title="Nilai Luas Data")
    meanA = [ave(Ai), ave(Ap), ave(At), ave(Pa)]
    meanB = [ave(Bi), ave(Bp), ave(Bt), ave(Pb)]
    createFile2(meanA, meanB, name="INFODATA", ke="", subjek=subjek, INFO=True)
    # plotInfo(Ai, Bi, 2, xl = '', yl = '', subjek=subjek,name=str(str(name)+"RataRataDataRT"), title="Perbandingan rata rata dari tangan kanan dan kiri",labels=["Tangan Kanan", "tangan kiri"] )
    # plotInfo(Ap, Bp, 2, xl = '', yl = '', subjek=subjek,name=str(str(name)+"PeakValueRT"), title="Perbandingan Peak Value dari tangan kanan dan kiri",labels=["Tangan Kanan", "tangan kiri"] )
    # plotInfo(At, Bt, 2, xl = '', yl = '', subjek=subjek,name=str(str(name)+"WaktuPeakDataRT"), title="Perbandingan Waktu Peak rata dari tangan kanan dan kiri",labels=["Tangan Kanan", "tangan kiri"] )
    # plotInfo(Pa, Pb, 2, xl = '', yl = '', subjek=subjek,name=str(str(name)+"LuasDataRT"), title="Perbandingan Luas Data dari tangan kanan dan kiri",labels=["Tangan Kanan", "tangan kiri"] )

    if printInfo == True:
        print("Rata Rata data A : ", ave(Ai))
        print("Rata Rata data B : ", ave(Bi))
        print("Peak Data A : ", ave(Ap))
        print("Peak Data B : ", ave(Bp))
        print("Time Peak Data A : ", ave(At))
        print("Time Peak Data B : ", ave(Bt))
        print("Luas Data A : ", ave(Pa))
        print("Luas Data B : ", ave(Pb))


    
# def plotInfo(data1,data2,jumlahData,xl, yl,name="TEST",title="INFO", ke="", save=True, show=False):
#     saveto = str("./image/" + str(name) + str(ke) +"INFO.png")
#     labels = []
#     width = 0.35
#     i = 1
#     j = []
#     while i <= jumlahData:
#         j.append(i)
#         G = str("G"+str(i))
#         labels.append(G)
#         i += 1
#     i = 0
#     k = []
#     while i <= jumlahData:
#         k.append(str(i))
#         i += 1
#     i = 0
#     m = []
#     while i <= jumlahData:
#         m.append(i)
#         i += 1

#     # grid = plt.GridSpec(1, 1, wspace=0.2, hspace=0.7, left=0.09, bottom=0.12, right=0.95, top=0.88)
    # plt.figure(figsize=(18,6))
#     # plt.subplot(grid[0,0])
#     plt.plot(j,data1, label="Data tangan kanan")
#     plt.plot(j,data2, label="Data tangan kiri")
#     plt.title(str(str(title) + " " + str(ke)))
#     plt.xlabel(str(xl))
#     plt.ylabel(str(yl))
#     plt.xticks(m,k)
#     plt.grid(True)
#     plt.savefig(saveto)
#     if show == True:
#         plt.show()
#         plt.close()

# def plotInfoLast(data1, )

def plotInfo(data1,data2,jumlahData,xl, yl,subjek="subjek",name="TEST",title="INFO", ke="",labels=False, save=True, show=False):
    saveto = str("./data/" + str(subjek)+ "/image/" + str(name) + str(ke) +"INFO.png")
    if labels == False:
        labels = []
        i = 1
        j = []
        while i <= jumlahData:
            G = str("G"+str(i))
            labels.append(G)
            i += 1  
    men_means = data1
    women_means = data2
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    grid = plt.GridSpec(1, 1, wspace=0.2, hspace=0.7, left=0.09, bottom=0.12, right=0.95, top=0.88)
    fig, ax = plt.subplots(figsize=(18,6))
    rects1 = ax.bar(x - width/2, men_means, width, label='Tangan Kanan')
    rects2 = ax.bar(x + width/2, women_means, width, label='Tangan Kiri')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(str(yl))
    ax.set_xlabel(str(xl))
    ax.set_title(str(title))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    # for rect in rects1:
    #     height = rect.get_height()
    #     ax.annotate('{}'.format(height),
    #                 xy=(rect.get_x() + rect.get_width() / 2, height),
    #                 xytext=(0, 3),  # 3 points vertical offset
    #                 textcoords="offset points",
    #                 ha='center', va='bottom')
    # for rect in rects2:
    #     height = rect.get_height()
    #     ax.annotate('{}'.format(height),
    #                 xy=(rect.get_x() + rect.get_width() / 2, height),
    #                 xytext=(0, 3),  # 3 points vertical offset
    #                 textcoords="offset points",
    #                 ha='center', va='bottom')
    fig.tight_layout()
    if save ==True:
        plt.savefig(saveto)
    if show==True:
        plt.show()
    plt.close()

    

def plotData2LAST(data1, data2, time, name="TestLAST", ke="", show=False, save=False):
    saveto = str("./image/"+name+ke+".png")
    o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
    o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    peak = []
    ave1 = FunctionOnlyone.ave(data1)
    ave2 = FunctionOnlyone.ave(data2)
    i = 0
    P = []
    while i<len(data1):
        P.append(i)
        i=i+1
    ket1 = str("Waktu(s)\nRata-rata : " + str(ave1) )
    ket2 = str("Waktu(s)\nRata-rata : " + str(ave2) )
    grid = plt.GridSpec(2, 1, wspace=0.2, hspace=0.7, left=0.09, bottom=0.12, right=0.95, top=0.88)
    plt.figure(figsize=(18,6))
    plt.subplot(grid[0,0])
    plt.plot(data1)
    P = np.array(P)
    plt.fill_between(P[int(len(P)/3):int(len(P)*2/3)], data1[int(len(P)/3):int(len(P)*2/3)], 0,color='aqua')
    plt.plot(data1.index(max(data1[int(len(data1)/3):int(len(data1)*2/3)])), max(data1[int(len(data1)/3):int(len(data1)*2/3)]), 'x', color='red', linewidth=2)
    plt.title("Tangan Kanan")
    plt.ylabel("Volt")
    plt.grid()
    plt.ylim(0,0.0025)
    plt.xlabel(ket1)
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.plot(data2.index(max(data2[int(len(data2)/3):int(len(data2)*2/3)])), max(data2[int(len(data2)/3):int(len(data2)*2/3)]), 'x', color='red', linewidth=2)
    plt.fill_between(P[int(len(P)/3):int(len(P)*2/3)], data2[int(len(P)/3):int(len(P)*2/3)], 0,color='aqua')
    plt.title("Tangan Kiri")
    plt.ylabel("Volt")
    plt.ylim(0,0.0025)
    plt.xlabel(ket2)
    plt.grid()
    plt.xticks(o1, oi)
    if save == True:
        plt.savefig(saveto)
    if show == True:
        plt.show()
    plt.close
    return (saveto)

def findplotlim(data1, data2, low=False, i=100):
    a = max(data1)
    b = max(data2)
    am = min(data1)
    bm = min(data2)
    if a > b:
        lim = a + a/i
    else:
        lim = b + b/i
    
    if low == True:
        low = 0
    elif am < bm:
        low = am - am/i
    else: 
        low = bm - bm/i
    return (low,lim)



def programPPT23Juli2020(dataname, subjek, save=True, Show=False):
    """
    Program untuk memproduksi kembali data data setelah dilakukan perubahan 

    """
    dataname1 = str(str(dataname) + "1")
    a,b = ReadFile(str(dataname1), subjek=subjek)
    # #FILTER
    time = 15
    # ave1 = ave(a)
    # ave2 = ave(b)
    # for element in a:
    #     element = element-ave1
    # for element in b:
    #     element = element-ave2
    a = bandpass_firwin_filter(a, 1400, 20, 500, len(a)/time)
    b = bandpass_firwin_filter(b, 1400, 20, 500, len(b)/time)
    a = a.tolist()
    b = b.tolist()
    lim = findplotlim(a,b)
    plotData2VOLT(a,b,time,name=str(str(dataname1)+"FilterFirwin"), ke="",subjek=str(subjek),limy=lim,show=show, save=save)
    a = recrification(a, Ave=False)
    b = recrification(b, Ave=False)
    lim = findplotlim(a,b)
    plotData2VOLT(a,b,time,name=(str(dataname1) + "Retrification"), ke="", subjek=str(subjek) ,limy=lim ,show=show, save=save)
    a = movingAvarage(a,500)
    b = movingAvarage(b, 500)
    lim = findplotlim(a,b)
    plotData2VOLT(a,b,time,name=(str(dataname1) + "MovingAverage"), ke="", subjek=str(subjek) ,limy=lim,fillb=True, show=True, save=True)
    a = RMS(a, 500)
    b = RMS(b, 500)
    lim = findplotlim(a,b)
    plotData2VOLT(a,b,time,name=(str(dataname1) + "RMS"), ke="", subjek=str(subjek) ,limy=lim,fillb=True, show=True, save=True)
    n = [1, 10, 20]
    for element in n:
        name = str(str(dataname) + str(element))
        a,b = ReadFile(name, subjek=subjek)
        a = signalProcessingFirwin(a, time, 20, 500, 500,Ave=False, save=True,show=False)
        b = signalProcessingFirwin(b,time,20,500,500,Ave=False, save=True, show=False)
        name = str(str(name)+"PPT")
        plotData2VOLT(a,b,time, name, str(element), subjek=str(subjek) ,limy=(0,0.002),fillb=True, show=False, save=True)
    GetInfo(str(dataname), 20, time, subjek=subjek)
    print("Successss!!!")

def createDatabaseid(subjek, subjekfolder):
    path = str("./data/DatabaseSubjek.txt")
    f = open(path, "a+")
    info = str("\n"+str(subjek) + "," + str(subjekfolder)+',0')
    f.write(info)
    f.close()

def recreateDatabaseid(subjek,folder, i):
    path = str("./data/DatabaseSubjek.txt")
    f = open(path, "w+")
    for k in range(len(subjek)):
        if k == 0:
            info = str(str(subjek[k]) + "," + str(folder[k])+','+str(i[k]))
        else:    
            info = str("\n"+str(subjek[k]) + "," + str(folder[k])+','+str(i[k]))
        f.write(info)
    f.close()

def GetSubjek():
    path = str("./data/DatabaseSubjek.txt")
    with open(path) as f:
        content = f.readlines()
    i = 0
    c = []
    d = []
    e = []
    while i < len(content):
        a,b,k = content[i].split(',')
        c.append(a.strip())
        d.append(b.strip())
        e.append(k.strip())
        i+=1
    return c,d,e

def fftProgram(data, time ,fs=True):
    if fs == True:
        fs = len(data)/time
    # Defide the data to every seccond.
    i = 0
    mean = []
    while i < 14:
        signal = data[int(len(data)*i/time):int(len(data)*(i+1)/time)]
        Signal = fftpack.fft(signal)
        freqs = fftpack.fftfreq(len(data))*fs
        if i < 13:
            signal2 = data[int(len(data)*(i+0.5)/time):int(len(data)*(i+1.5))]
            Signal2 = fftpack.fft(signal)
            freqs2 = fftpack.fftfreq(len(data))*fs

        # print(data.index(signal[0]), data.index(signal[-1]))
        Signal = fftpack.fft(signal)
        freqs = fftpack.fftfreq(len(data))*fs
        # to get data fft mean
        # freqs = freqs.tolist()
        # Signal = Signal.tolist()
        # m = []
        # S = 0
        # FreqM = 0
        # for element in Signal:
        #     meanS = element * abs(freqs[int(Signal.index(element))])
        #     S = S + meanS
        #     FreqM = FreqM + freqs[int(Signal.index(element))]
        # mean.append(meanS/FreqM)
        i += 1
        if i < 5:
            plot = True
        else:
            plot = False
        
        if plot == True:
            # fig, ax = plt.subplots()
            plt.plot(freqs, abs(c))
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Frequency Domain (spectrum) Magnitude')
        plt.grid(True)
    plt.show()

def CheckData(data):
    a = ave(data[100:200])
    a1 = a+100
    a2 = a-100
    i = 0
    while i < 100:
        if data[i] > a1:
            data[i] = a
        elif data[i] < a2:
            data[i] = a
        i +=1
    return data

    # Signal = fftpack.fft(signal)
    # freqs = fftpack.fftfreq(len(signal))*fs

def welchdata(a,b,ffirwin=True):
    if ffirwin==True:
        a = bandpass_firwin_filter(a, 1400, 20, 500, len(a)/15)
        b = bandpass_firwin_filter(b, 1400, 20, 500, len(b)/15)
    awalA = a[0:int(len(a)/3)]
    tengahA = a[int(len(a)/3):int(len(a)*2/3)]
    akhirA = a[int(len(a)*2/3):-1]
    awalB = b[0:int(len(b)/3)]
    tengahB = b[int(len(b)/3):int(len(b)*2/3)]
    akhirB = b[int(len(b)*2/3):-1]




# a,b = ReadFile("rafliA1", subjek="Rafli")
# a = bandpass_firwin_filter(a,1400, 20,500, fs=(int(len(a)/15)))
# a = recrification(a)
# print(len(a))
# fftProgram(a, 15)
# GetSubjek()

    


# programPPT23Juli2020("rafliA", "Rafli")


# GetInfo("ilham20keC", 20, 15, subjek="ilham")
