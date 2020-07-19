import FunctionOnlyone
import numpy as np
from scipy.fft import fft
from scipy.signal import butter, lfilter,freqz,find_peaks
from scipy import signal, fftpack


def ReadFile(dataName):
    path = str("./data/" + dataName + ".txt")
    with open(path) as f:
        content =f.readlines()
    i = 0
    c = []
    d = []
    while i < len(content):
        a,b = content[i].split(',')
        a = (5*float(a))/1024
        b = (5*float(b.strip()))/1024
        # a = float(a)
        # b = float(b.strip())
        c.append(a)
        d.append(b)
        i = i + 1
    # bi = []
    # for element in b:
    #     bi.append(element.strip())
    # print (bi)
    # b = bi
    return c,d 

def WriteInfo(name, data1, time):
    f = open("./data/INFODATA.txt", "a+")
    ave1 = FunctionOnlyone.ave(data1)
    peak1 = max(data1)
    peakt1 = (data1.index(max(data1))/len(data1))*time
    info = str("\nData " + name + " Dengan Rata-rata : " + ave1 + " PeakTime : " + peakt1 + " Pada peak : " + peak1)
    f.write(info)
    f.close()

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandstop(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandstop')
    return b, a

def butter_bandstop_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandstop(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def signalProcessing(signal,t, lowcut, highcut):
    fs = len(signal)/t
    y = butter_bandpass_filter(signal,lowcut, highcut,fs,order=5)
    ave = FunctionOnlyone.ave(signal)
    ai = []
    for element in  signal:
        s = element-ave
        ai.append(s*s)
    i = 0
    ws = 500
    mA = []
    while i < len(ai) - ws + 1:
        tW = ai[i:i+ws]
        wA = sum(tW) / ws
        mA.append(wA)
        i += 1
    return mA


def GetInfo(name1, j, time):
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

        name = str(name1 + str(k))
        print("Processing Data.. ", name)
        a,b = ReadFile(name)
        ai = signalProcessing(a, 15, 20,500)
        bi = signalProcessing(b, 15, 20,500)
        peak1 = max(ai)
        peak2 = max(bi)
        peakt1 = (ai.index(max(ai))/len(ai))*time
        peakt2 = (bi.index(max(bi))/len(bi))*time
        ave1 = FunctionOnlyone.ave(ai)
        ave2 = FunctionOnlyone.ave(bi)
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
    FunctionOnlyone.createFile2(Ai,Bi, "RataRataDataC", "0")
    FunctionOnlyone.createFile2(Ap,Bp, "PeakTimeDataC", "0")
    FunctionOnlyone.createFile2(At, Bt, "WaktuPeakDataC", "0")
    FunctionOnlyone.createFile2(Pa, Pb, "LuasData", "0")
    print("Rata Rata data A : ", Ai)
    print("Rata Rata data B : ", Bi)
    print("Peak Data A : ", Ap)
    print("Peak Data B : ", Bp)
    print("Time Peak Data A : ", At)
    print("Time Peak Data B : ", Bt)
    print("Luas Data A : ", Pa)
    print("Luas Data B : ", Pb)
# GetInfo("ilham20keC",20, 15)





    


# FunctionOnlyone.plotData20(c,d, 300, 15, "ilham","ilham")