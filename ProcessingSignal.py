import FunctionOnlyone
from ReadFile import ReadFile
from scipy.signal import butter, lfilter,freqz,find_peaks, welch
from scipy import signal, fftpack
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.fft import fft

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

def plotData2(data1, data2, time, name, ke):
    saveto = str("./image/"+name+ke+".png")
    # time = time*20
    # j= 15
    # i = 0
    # h = (time/(time/j)/3)
    # oi = []
    # o = []
    # o1 = []
    # q = 1
    # o.append(0)
    # o1.append(0)
    # while i <= time:
    #     oi.append(str(i))
    #     o.append(int((len(data1)*q)/20))
    #     o1.append(int((len(data2)*q)/20))
    #     i = i + j
    #     q = q + 1 
    o = [0, len(data1)/3, (len(data1)*2)/3, len(data1)]
    o1 = [0, len(data2)/3, (len(data2)*2)/3, len(data2)]
    oi =["0", str(time/3), str((time*2)/3), str(time)]
    peak = []
    # peak1 = max(data1)
    # peak2 = max(data2)
    # peakt1 = (data1.index(max(data1))/len(data1))*time
    # peakt2 = (data2.index(max(data2))/len(data2))*time
    ave1 = FunctionOnlyone.ave(data1)
    ave2 = FunctionOnlyone.ave(data2)
    i = 0
    P = []
    while i<len(data1):
        P.append(i)
        i=i+1
    # print(peak1, peakt1, ave1)
    # print(peak2, peakt2, ave2)
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
    # plt.ylim(2.30,2.60)
    # plt.ylim(0,0.5)
    # plt.ylim(0,0.0022)
    plt.xlabel(ket1)
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(data2)
    plt.plot(data2.index(max(data2[int(len(data2)/3):int(len(data2)*2/3)])), max(data2[int(len(data2)/3):int(len(data2)*2/3)]), 'x', color='red', linewidth=2)
    plt.fill_between(P[int(len(P)/3):int(len(P)*2/3)], data2[int(len(P)/3):int(len(P)*2/3)], 0,color='aqua')
    plt.title("Tangan Kiri")
    plt.ylabel("Volt")
    plt.ylim(0,0.0025)
    # plt.ylim(2.30,2.60)
    # plt.ylim(0,0.0022)
    plt.xlabel(ket2)
    plt.grid()
    plt.xticks(o1, oi)
    plt.savefig(saveto)
    plt.show()
    # plt.close
    return (saveto)


def signalProcessing(signal,t, lowcut, highcut):
    fs = len(signal)/t
    y = butter_bandpass_filter(signal,lowcut, highcut,fs,order=5)
    mA = []
    A = FunctionOnlyone.ave(y)
    for element in y:
        c = element-A
        mA.append((c*c))
    # FunctionOnlyone.plotData(y,t,"ilham", "")
    i = 0
    ws = 500
    r = []
    while i < len(mA) - ws + 1:
        tW = mA[i:i+ws]
        wA = sum(tW) / ws
        r.append(wA)
        i += 1
    return r[200:]

# c = 1
# while c < 21:
#     u = str("rafliA" + str(c))
#     print("Processing... ", u)
#     a,b = ReadFile(u)
#     # print(len(a))
#     a = signalProcessing(a, 15, 20, 500)
#     b = signalProcessing(b, 15, 20, 500)
#     plotData2(a,b,15, str(str(u)+"Filter"), "")
#     c = c + 1

a,b = ReadFile("/ilham/data/ilham20keC1")
print("Processing..")
ap = int(len(a)/15)
bp = int(len(b)/15)
a = FunctionOnlyone.bandpass_firwin_filter(a,1200,20,500,len(a)/15)
b = FunctionOnlyone.bandpass_firwin_filter(b,1200,20,500,len(b)/15)
a = FunctionOnlyone.fastFourierTransform(a,15,name="FFTilhamke20C1A", fs=len(a)/15)
b = FunctionOnlyone.fastFourierTransform(b,15,name="FFTilhamke20C1B", fs=len(b)/15)
# a = FunctionOnlyone.welchFunction(a, 15)
# b = FunctionOnlyone.welchFunction(a, 15)
# a = FunctionOnlyone.signalProcessingFirwin(a,15,20,500,500,500,5, show=True)
# b = FunctionOnlyone.signalProcessingFirwin(b,15,20,500,500,500,5, show=True)

# 
# lowcut = 10
# highcut = 50


# y1 = butter_bandpass_filter(a, lowcut,highcut,fs, order=2)

# lowcut = 48
# highcut = 52

# y = butter_bandstop_filter(a,lowcut,highcut,fs,order=5)

# af = y1[200:]
# ave = FunctionOnlyone.ave(a)
# ai = []
# for element in  a:
#     s = element-ave
#     ai.append(s)

# i = 0
# ws = 1000
# mA = []
# while i < len(sf) - ws + 1:
#     tW = sf[i:i+ws]
#     wA = sum(tW) / ws
#     mA.append(wA)

