from time import sleep
import FunctionOnlyone


def akusisi():
    dataA = []
    dataB = []
    temp = []
    subjek = input("Masukan nama raflisubjek... ")
    i = 1
    print("Akusisi data akan dimulai 20x selama 15 detik tiap gerakan nya secara bersamaan")
    while i < 21:
        a = []
        b = []
        t = 15
        print("Pengambilan data akan dimulai dalam 5 detik..")
        sleep(2)
        print("3 Detik...")
        sleep(3)
        print("Pengambilan data dimulai!")
        a,b = FunctionOnlyone.activeteAccusition(a, b, t)
        ke = FunctionOnlyone.plotData2(a,b,t,subjek, ke = str(i))
        r = input("Masukan data? y/n")
        if r == 'y':
            freqA = str(len(a)/t)
            freqB = str(len(b)/t)
            ai = FunctionOnlyone.ave(a)
            bi = FunctionOnlyone.ave(b)
            ketA = str("Data Sensor 1 (Kanan) untuk pengambilan ke " + str(i))
            ketB = str("Data Sensor 2 (Kiri) untuk pengambilan ke " + str(i))
            FunctionOnlyone.createFile2(a,b,subjek,str(i))
            FunctionOnlyone.create_readme(subjek, str(t), str(freqA), str(ai), str(ketA), str(ke))
            FunctionOnlyone.create_readme(subjek, str(t), str(freqB), str(bi), str(ketB), str(ke))
            print("Pemrosesan data selesai!")
            i = i + 1
            dataA = FunctionOnlyone.addData(dataA,a) 
            dataB = FunctionOnlyone.addData(dataB,b)
        # except:
        #     input("Continue?")
        #     print("Pengambilan Error, mengulang untuk yang ke.. ", i)
        #     pass
    print("Pengamilan data 20x selesai!")
    ke = "PengambilanData20x"
    t = t*20
    freqA = str(len(dataA)/t)
    freqB = str(len(dataB)/t)
    ai = FunctionOnlyone.ave(dataA)
    bi = FunctionOnlyone.ave(dataB)
    FunctionOnlyone.createFile2(dataA,dataB, subjek, ke)
    FunctionOnlyone.create_readme(subjek, str(t), str(freqA), str(ai), str(ketA), str(ke))
    FunctionOnlyone.create_readme(str(subjek), str(t), str(freqB), str(bi), str(ketB), str(ke))
    ke = FunctionOnlyone.plotData20( dataA , dataB , t , 15,subjek, ke=ke)

akusisi()




        




        