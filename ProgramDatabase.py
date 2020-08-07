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
subjek,folder = FunctionOnlyone.GetSubjek()
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
        if filtered==True:
            dataName = str("Filtered"+str(subjek[i])+str(j))
        else:
            dataName = str(str(subjek[i])+str(j))
        c,d = FunctionOnlyone.ReadFile(dataName, folder[i])
        c = FunctionOnlyone.signalProcessingFirwin(c, 15, 20, 500, 500,Ave=False, save=save,show=show)
        d = FunctionOnlyone.signalProcessingFirwin(d,15,20,500,500,Ave=False, save=save, show=show)
        name = str("Filtered"+str(subjek[i]))
        FunctionOnlyone.createFile2(c,d,name,str(j),subjek=folder[i])
        dataS = {
            'name' : dataName,
            'kanan' : c,
            'kiri' : d,
        }
        dataSubjek[k] = dataS
        # print("Processing data..", dataName)
        j += 1
        k +=1
    data[i] = dataSubjek
    i+=1
e = data.get(0)
e = e.get(0)
e = e.get('name')
f = data.get(0).get(0).get('kanan')
f = FunctionOnlyone.bandpass_firwin_filter(f, 1400, 20, 500, len(f)/15)
q, Freqs = FunctionOnlyone.fastFourierTransform(f, 15, plot=False, save=False)
# plt.plot(f)
# plt.show()
# plt.close()
awal = f[0:int(len(f)/3)]
akhir = f[int(len(f)*2/3):-1]
tengah = f[int(len(f)/3):int(len(f)*2/3)]
awal, Pxxw = welch(awal, fs = len(f)/14, window='hann', nperseg=int(len(awal)/5)-10)
akhir, Pxxk = welch(akhir, fs = len(f)/14, window='hann', nperseg=int(len(akhir)/5)-10)
tengah, Pxxt = welch(tengah, fs = len(f)/14, window='hann', nperseg=int(len(tengah)/5)-10)

# k = ((max(awal[])),())
print(e)
# print(f)
plt.plot(Freqs, abs(q))
plt.semilogy(awal, np.sqrt(Pxxw))
plt.semilogy(tengah, np.sqrt(Pxxt))
plt.semilogy(akhir, np.sqrt(Pxxk))
print(len(awal), len(np.sqrt(Pxxw)))
print(max(np.sqrt(Pxxw)[20:500]))
plt.legend(("FFT tanpa Welch Function","awal", "tengah", "akhir"))
plt.grid(True)
# plt.ylim(ylimit)
plt.xlim(0, 520)
plt.show()
plt.close()



