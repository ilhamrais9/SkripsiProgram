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
from scipy.signal import butter, lfilter, firwin, freqz, welch
from math import sqrt

def activate():
    arduino = serial.Serial('COM3', 74880) # Establish the connection on a specific port
    arduino1 = serial.Serial('COM8', 74880) # Establish the connection on a specific port
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



def create_readme (subjek, time, freq, ave, ket, ke):
    f = open("./data/README.txt", "a+")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    t = ("date and time =", dt_string)
    write = str("\nData " + subjek + " dengan Freq : " + freq + " denga waktu : " + time + " avarege data: " + ave + " " + ket + " "+ str(t) + " Destinasi: " + ke) 
    f.write(write)
    f.close()

def ave(data):
    return (sum(data)/len(data))


def createFile(data1, name, ke):
    name = "./data/"+ name +  ke + ".txt"
    print("Membuat file.. "+str(name))
    f = open(str(name), "w+")
    i = 0
    while i < len(data1) :
        f.write(str(data1[i]))
        i = i+1
    f.close()
def createFile2(data1, data2, name, ke):
    name = "./data/" + name +  ke + ".txt"
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

def plotData2(data1, data2, time, name, ke):
    saveto = str("./image/"+name+ke+".png")
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
    plt.grid()
    plt.ylabel("ADC")
    plt.xlabel("Waktu (s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.title(ket2)
    plt.ylabel("ADC")
    plt.grid()
    plt.xlabel("Waktu (s)")
    plt.xticks(o1, oi)
    plt.savefig(saveto)
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

def recrification(a):
    mA = []
    A = ave(a)
    for element in a:
        c = element-A
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
    nyq = 0.5 * fs
    taps = firwin(ntaps, [lowcut, highcut], nyq=nyq, pass_zero=False,
                  window=window)
    return taps

def bandpass_firwin_filter(data, ntaps, lowcut, highcut, fs):
    taps = bandpass_firwin(ntaps, lowcut, highcut, fs)
    # w,h = freqz(taps, 1, worN=2000)
    y = lfilter(taps,1.0, data)
    return y

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

def signalProcessingButter (signal, t, lowcut,highcut,ws, NilaiRMS, order):
    fs = len(signal)/t
    signal = bandpass_firwin_filter(data = signal, ntaps=1200, lowcut=lowcut, highcut=highcut,fs= int(len(signal)/t))
    # print(signal)
    print("filtering..")
    signal = recrification(signal)
    print("Recrificationing...")
    signal = movingAvarage(signal, ws)
    print("Moving avareging...")
    signal = RMS(signal, NilaiRMS)
    print("Processing RMS...")
    return signal

def fastFourierTransform(signal, time, name="TEST"):
    fs = len(signal)/time
    Signal = fftpack.fft(signal)
    freqs = fftpack.fftfreq(len(signal))*fs
    fig, ax = plt.subplots()
    plt.plot(freqs, abs(Signal))
    plt.xlabel('Frequency in Hz')
    plt.ylabel('Frequency Domain (spectrum) Magnitude')
    plt.grid(True)
    n = str("./image/"+ str(name) +"FFT")
    plt.savefig(n)
    plt.show()
    plt.close()

    
def welchFunction(data, time):
    fs = data/time
    f , Pxx_den = welch(data, fs)
    plt.semilogy(f, Pxx_den)
    # plt.ylim([0.5e-3, 1])
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()
    plt.close()




