import FunctionOnlyone
import numpy as np
from matplotlib import pyplot  as plt
from scipy.signal import welch


"""
Program Database untuk memproses hasil data
"""

filtered = False
show = True
save = True
subjek,folder,f = FunctionOnlyone.GetSubjek()
print(f)
print("Jumlah data : " + str(len(subjek)))
i = 0
# read database data
data = {}
while i < len(subjek) and i < len(folder):
    dataSubjek = {}
    k=0
    j = 1
    while j <= 20 :
        dataS = {}
        if f[i]=='0':
            dataName = str("Filtered"+str(subjek[i])+str(j))
            c,d = FunctionOnlyone.ReadFile(dataName, folder[i])
            a = FunctionOnlyone.signalProcessingFirwin(c, 15, 20, 500, 500,Ave=True, save=save,show=show)
            b = FunctionOnlyone.signalProcessingFirwin(d,15,20,500,500,Ave=True, save=save, show=show)
            name = str("Filtered"+str(subjek[i]))
            FunctionOnlyone.createFile2(a,b,name,str(j),subjek=folder[i])
        else:
            dataName = str(str(subjek[i])+str(j))
            c,d = FunctionOnlyone.ReadFile(dataName, folder[i])
            dataName2 = str("Filtered"+str(subjek[i])+str(j))
            a,b = FunctionOnlyone.ReadFile(dataName2, folder[i])
        dataS = {
            'name' : dataName,
            'kanan' : c,
            'kiri' : d,
            'fkanan': a,
            'fkiri': b
        }
        dataSubjek[k] = dataS
        # print("Processing data..", dataName)
        j += 1
        k +=1
    data[i] = dataSubjek
    f[i]=1
    i+=1

FunctionOnlyone.recreateDatabaseid(subjek, folder, f)

i = 0
for y in range(len(folder)):
    print("Processing..", folder[i])
    for x in range(20):
        print("file..", subjek[i], x+1)
        a = data.get(i).get(x).get('kanan')
        b = data.get(i).get(x).get('kiri')
        ke = FunctionOnlyone.plotData2VOLT(a,b,t,subjek[i], ke = str(x+1), subjek=folder[i], show=False, save=True)
        c = data.get(i).get(x).get('fkanan')
        d = data.get(i).get(x).get('fkiri')
        name = str("Processed" + str(subjek[i]))
        FunctionOnlyone.plotData2VOLT(c,d, t, name, str(x+1), subjek=str(folder[i]) ,limy=FunctionOnlyone.findplotlim(c,d, low=True, i=10), fillb=True, show=False, save=True, printInfo=False)

    i += 1



# f = FunctionOnlyone.bandpass_firwin_filter(f, 1400, 20, 500, len(f)/15)
# q, Freqs = FunctionOnlyone.fastFourierTransform(f, 15, plot=False, save=False)
# plt.plot(f)
# plt.show()
# plt.close()

# welch function
# awal = f[0:int(len(f)/3)]
# akhir = f[int(len(f)*2/3):-1]
# tengah = f[int(len(f)/3):int(len(f)*2/3)]
# awal, Pxxw = welch(awal, fs = len(f)/14, window='hann', nperseg=int(len(awal)/5)-10)
# akhir, Pxxk = welch(akhir, fs = len(f)/14, window='hann', nperseg=int(len(akhir)/5)-10)
# tengah, Pxxt = welch(tengah, fs = len(f)/14, window='hann', nperseg=int(len(tengah)/5)-10)

# k = ((max(awal[])),())
# print(e)
# print(f)
# plt.plot(Freqs, abs(q))
# plt.semilogy(awal, np.sqrt(Pxxw))
# plt.semilogy(tengah, np.sqrt(Pxxt))
# plt.semilogy(akhir, np.sqrt(Pxxk))
# print(len(awal), len(np.sqrt(Pxxw)))
# print(max(np.sqrt(Pxxw)[20:500]))
# plt.legend(("FFT tanpa Welch Function","awal", "tengah", "akhir"))
# plt.grid(True)
# # plt.ylim(ylimit)
# plt.xlim(0, 520)
# plt.show()
# plt.close()



