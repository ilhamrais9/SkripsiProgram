from builtins import input
import os
from time import sleep
from pathlib import Path
from FunctionOnlyone import activeteAccusition, createFile, plotData, accusition, saveData
print("Memulai Akusisi data")

def runAkusisi():
    subjek = input("Masukan Nama subjek.. ")
    ke = input("Percobaan ke.. ")
    time =int(input("Pengambilan data per ... "))
    x,time, freq = accusition(time)
    saveData(x, subjek, ke, time)

runAkusisi()
# time = int(input("Masukan waktu pengambilan data.. "))









    



