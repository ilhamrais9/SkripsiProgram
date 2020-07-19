from builtins import input
from time import Sleep
import FunctionOnlyone


def I(subjek):
    print ("Pengambilan untuk mengetahui perbedaan data lengan kanan dan kiri \n Pengambilan pertama adalah pergerakan bersama.")
    # FunctionOnlyone.check()
    print ("Pengambilan data akan dilakukan dalam 5 detik.")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    a = []
    b = []
    t = 30
    print("\n Pengambilan data dimmulai! \n")
    a,b = FunctionOnlyone.activeteAccusition(a, b, t)
    ke = FunctionOnlyone.plotData2(a,b,t,subjek,ke="ProgramI11")
    freqA = str((len(a)/2)/t)
    freqB = str((len(b)/2)/t)
    ai = FunctionOnlyone.ave(a)
    bi =  FunctionOnlyone.ave(b)
    ketA = "Pengambilan Program I11 Tangan Kanan data A"
    ketB =  "Pengambilan Program I11 Tangan Kiri data B"
    FunctionOnlyone.create_readme(subjek, t, freqA, ave= ai, ket = ketA,  ke=ke)
    FunctionOnlyone.create_readme(subjek, t, freqB, ave= bi, ket = ketB,  ke=ke)
    print("Pengambilan data untuk gerakan yang sama.. \n siap siap dalam 5 detik.. ")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    c = []
    d = []
    print("\n Pengambilan data dimmulai! \n")
    c,d = FunctionOnlyone.activeteAccusition(c, d, t)
    ke = FunctionOnlyone.plotData2(c,d,t,subjek,ke="ProgramI12")
    freqC = str((len(c)/2)/t)
    freqD = str((len(d)/2)/t)
    ci =  FunctionOnlyone.ave(c)
    di = FunctionOnlyone.ave(d)
    ketC = "Pengambilan Program I11 Tangan Kanan data C"
    ketD = "Pengambilan Program I11 Tangan Kanan data D"
    FunctionOnlyone.create_readme(subjek, t, freqC, ci,ketC, ke)
    FunctionOnlyone.create_readme(subjek, t, freqD, di, ketD, ke)
    print("Pengambilan data untuk gerakan yang sama.. \n siap siap dalam 5 detik.. ")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    e = []
    f = []
    print("\n Pengambilan data dimmulai! \n")
    e,f = FunctionOnlyone.activeteAccusition(e, f, t)
    ke = FunctionOnlyone.plotData2(e,f,t,subjek,ke="ProgramI13")
    freqE = str((len(e)/2)/t)
    freqF = str((len(f)/2)/t)
    ei =  FunctionOnlyone.ave(e)
    fi = FunctionOnlyone.ave(f)
    ketE = "Pengambilan Program I11 Tangan Kanan data E"
    ketF = "Pengambilan Program I11 Tangan Kanan data F"
    FunctionOnlyone.create_readme(subjek, t, freqE, ei,ketE, ke)
    FunctionOnlyone.create_readme(subjek, t, freqF, fi, ketF, ke)
    print ("\n pengambilan data seluruhnya selesai. memproses hasil..")

    FullA = FunctionOnlyone.addData(a,c)
    FullA = FunctionOnlyone.addData(FullA,e)
    FullB = FunctionOnlyone.addData(b,d)
    FullB = FunctionOnlyone.addData(FullB,f)

    print("pemrosesan data berhasil! \n Menyimpan data..")
    name = subjek
    FunctionOnlyone.createFile2(a, b, name, ke="ProgramIke1A")
    FunctionOnlyone.createFile2(c, d, name, ke="ProgramIke2A")
    FunctionOnlyone.createFile2(e, f, name, ke="ProgramIke3B")
    FunctionOnlyone.createFile2(FullA, FullB, name, ke="ProgramIFull1")
    FunctionOnlyone.plotFigure2(a,b,c,d,e,f,FullA, FullB, time=t, ke="Berbarengan", name=name)
    print("Program Pengambilan data A selesai!")
    
    print ("\n\nPengambilan untuk mengetahui perbedaan data lengan kanan dan kiri \n Pengambilan pertama adalah pergerakan berbeda.")
    print ("Pengambilan data akan dilakukan dalam 5 detik. \n Dimualai dari tangan kanan!")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    a = []
    b = []
    t = 15
    print("\n Pengambilan data dimmulai! \n")
    a = FunctionOnlyone.activeteAccusition1(a,t)
    print("Pengambilan data tangan kiri akan dimulai dalam 3 detik...")
    Sleep(3)
    print("pengambilan data dimulai!")
    b = FunctionOnlyone.activeteAccusition2(b,t)
    FunctionOnlyone.plotData2(a,b,t,subjek,ke="ProgramI21")
    print("Pengambilan data kedua.. \n siap siap dalam 5 detik.. ")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    c = []
    d = []
    print("\n Pengambilan data dimmulai! \n")
    c = FunctionOnlyone.activeteAccusition1(c,t)
    print("Pengambilan data tangan kiri akan dimulai dalam 3 detik...")
    Sleep(3)
    print("pengambilan data dimulai!")
    d = FunctionOnlyone.activeteAccusition2(d,t)
    FunctionOnlyone.plotData2(c,d,t,subjek,ke="ProgramI22")
    print("Pengambilan data ketiga.. \n siap siap dalam 5 detik.. ")
    Sleep(2)
    print ("3 Detik...")
    Sleep(3)
    e = []
    f = []
    print("\n Pengambilan data dimmulai! \n")
    e = FunctionOnlyone.activeteAccusition1(e,t)
    print("Pengambilan data tangan kiri akan dimulai dalam 3 detik...")
    Sleep(3)
    print("pengambilan data dimulai!")
    f = FunctionOnlyone.activeteAccusition2(f,t)
    FunctionOnlyone.plotData2(e,f,t,subjek,ke="ProgramI23")
    FullA = FunctionOnlyone.addData(a,c)
    FullA = FunctionOnlyone.addData(FullA,e)
    FullB = FunctionOnlyone.addData(b,d)
    FullB = FunctionOnlyone.addData(FullB,f)

    print("pemrosesan data berhasil! \n Menyimpan data..")
    name = subjek
    FunctionOnlyone.createFile2(a, b, name, ke="ProgramIke1B")
    FunctionOnlyone.createFile2(c, d, name, ke="ProgramIke2B")
    FunctionOnlyone.createFile2(e, f, name, ke="ProgramIke3B")
    FunctionOnlyone.createFile2(FullA, FullB, name, ke="ProgramIFull2")
    FunctionOnlyone.plotFigure2(a,b,c,d,e,f,FullA, FullB, time=t, ke="IBerbeda", name=name)
    print("Program Pengambilan data B selesai!")
    jenisProgram=int(input("Akhiri program masukan 5 ...."))
    return jenisProgram

def II(subjek):
    print("Pengambilan data II, Kontraksi dengan beban 5kg dan melihat kondisi sinyal otot.\n pasang sensor di bisep kanan(sensor1) dan bisep kiri(sensor2)\n Pengambilan data akan dilakukan dalam 5 Detik!! \n")
    Sleep(2)
    print("3 Detik... siap siap untuk pergerakan pertama yaitu tangan kanan!")
    Sleep(3)
    a = []
    b = []
    c = []
    t = 15
    print("Pengambilan data dimulai!")
    a = FunctionOnlyone.activeteAccusition1(a,t)
    input("Silahkan melakukan kontraksi mengangkat barbel 5kg sebanyak 10x dan masukan input apapun untuk melanjutkan.")
    print("Pengambilan data selanjutnya akan dimulai dalam 5 detik. masih pada tangan kanan.")
    Sleep(2)
    print("3 detik...")
    Sleep(3)
    b = FunctionOnlyone.activeteAccusition1(b,t)
    input("Silahkan melakukan kontraksi mengangkat barbel 5kg sebanyak 10x dan masukan input apapun untuk melanjutkan.")
    print("Pengambilan data selanjutnya akan dimulai dalam 5 detik. masih pada tangan kanan.")
    Sleep(2)
    print("3 detik...")
    Sleep(3)
    c = FunctionOnlyone.activeteAccusition1(c,t)
    print("Pengambilan data pada tangan kanan selesai! silahkan persiapkan tangan kiri")
    FunctionOnlyone.plotData3(a,b,c,t,subjek,ke="ProgramII1")
    d = []
    e = []
    f = []
    input("Masukan input apa saja untuk memulai..")
    print("Pengambilan data selanjutnya akan dimulai dalam 5 detik. Pengambilan data pada tangan kiri.")
    Sleep(2)
    print("3 detik...")
    Sleep(3)
    d = FunctionOnlyone.activeteAccusition2(d,t)
    input("Silahkan melakukan kontraksi mengangkat barbel 5kg sebanyak 10x dan masukan input apapun untuk melanjutkan.")
    print("Pengambilan data selanjutnya akan dimulai dalam 5 detik. Pengambilan data pada tangan kiri.")
    Sleep(2)
    print("3 detik...")
    Sleep(3)
    e = FunctionOnlyone.activeteAccusition2(e,t)
    input("Silahkan melakukan kontraksi mengangkat barbel 5kg sebanyak 10x dan masukan input apapun untuk melanjutkan.")
    print("Pengambilan data selanjutnya akan dimulai dalam 5 detik. Pengambilan data pada tangan kiri.")
    Sleep(2)
    print("3 detik...")
    Sleep(3)
    f = FunctionOnlyone.activeteAccusition2(f,t)
    print("Pengambilan data pada tangan kiri selesai! memproses data..")
    FunctionOnlyone.plotData3(d,e,f,t,subjek,ke="ProgramII2")
    FullA = FunctionOnlyone.addData(a,b)
    FullA = FunctionOnlyone.addData(FullA,c)
    FullB = FunctionOnlyone.addData(d,e)
    FullB = FunctionOnlyone.addData(FullB,f)
    FunctionOnlyone.saveData(a, subjek, ke="DataIIA", time=t)
    FunctionOnlyone.saveData(b, subjek, ke="DataIIB", time=t)
    FunctionOnlyone.saveData(c, subjek, ke="DataIIC", time=t)
    FunctionOnlyone.saveData(d, subjek, ke="DataIID", time=t)
    FunctionOnlyone.saveData(e, subjek, ke="DataIIE", time=t)
    FunctionOnlyone.saveData(f, subjek, ke="DataIIF", time=t)
    FunctionOnlyone.saveData(FullA, subjek, ke="DataIIFULLA", time=t)
    FunctionOnlyone.saveData(FullB, subjek, ke="DataIIFULLB", time=t)
    FunctionOnlyone.plotFigure2(a,b,c,d,e,f,FullA,FullB,t, ke="II", name=subjek)
    jenisProgram=int(input("Akhiri program masukan 5 ...."))
    return jenisProgram

def III():
    
    return


def IV():
    return

def programSelesai():
    print ("Program selesai!")

print("Memulai Akusisi data")
print("Selamat Datang diprogram simulasi pengambilan data \n Data ini akan diambil sesuai dari file Targer pengambilan data \n")


subjek = input("Nama subjek : ")
jenisProgram =  int(input(" Masukan Definisi program yang ingin dilakukan : (1-4 program, 0 = info\n"))


while True:
    if jenisProgram == 0:
        print ("Info program :\n I. Pengambilan data perbedaan lengan kanan dan kiri")
        print (" II. Pengambilan data setelah malekukan kontraksi")
        print (" III. Perbedaan dari siku dan bahu")
        print (" IV. Perbedaan orang sehat dan sakit")

    elif jenisProgram == 1: 
        I(subjek)
        programSelesai()
        jenisProgram = int(input("Mohon masukan data yang benar."))
    elif jenisProgram == 2: 
        II(subjek)
        programSelesai()
    elif jenisProgram == 3: 
        III(subjek)
        programSelesai()
    elif jenisProgram == 4: 
        IV(subjek)
        programSelesai()
    elif jenisProgram == 5:
        break
    
    jenisProgram = int(input("Mohon masukan data yang benar."))