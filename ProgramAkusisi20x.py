from time import sleep
import FunctionOnlyone

def akusisi():
    dataA = []
    dataB = []
    temp = []
    folder = input("masukan nama folder.. /pastikan sudah dibuat : ")
    subjek = input("Masukan nama subjek... ")
    i = 1
    print("Akusisi data akan dimulai 20x selama 15 detik tiap gerakan nya secara bersamaan")
    while i < 22:
        a = []
        b = []
        t = 15
        print("Pengambilan data akan dimulai dalam 5 detik..")
        sleep(2)
        print("3 Detik...")
        sleep(3)
        print("Pengambilan data dimulai!")
        a,b = FunctionOnlyone.activeteAccusition(a, b, t)
        a = FunctionOnlyone.CheckData(a)
        b = FunctionOnlyone.CheckData(b)
        ke = FunctionOnlyone.plotData2ADC(a,b,t,subjek, ke = str(i), subjek=folder, show=True, save=True)
        r = input("Masukan data? y/n")
        if r == 'y':
            freqA = str(len(a)/t)
            freqB = str(len(b)/t)
            ai = FunctionOnlyone.ave(a)
            bi = FunctionOnlyone.ave(b)
            ketA = str("Data Sensor 1 (Kanan) untuk pengambilan ke " + str(i))
            ketB = str("Data Sensor 2 (Kiri) untuk pengambilan ke " + str(i))
            FunctionOnlyone.createFile2(a,b,subjek,str(i), subjek=folder)
            FunctionOnlyone.create_readme(subjek,folder, str(t), str(freqA), str(ai), str(ketA), str(ke))
            FunctionOnlyone.create_readme(subjek,folder, str(t), str(freqB), str(bi), str(ketB), str(ke))
            print("Pemrosesan data selesai!")
            i = i + 1
        
        # except:
        #     input("Continue?")
        #     print("Pengambilan Error, mengulang untuk yang ke.. ", i)
        #     pass
    print("Creating database...")
    FunctionOnlyone.createDatabaseid(subjek, folder)
    i = 1
    save = True
    show = False
    while i <= 20:
        dataName = str(str(subjek)+str(i))
        c,d = FunctionOnlyone.ReadFile(dataName, folder)
        c = FunctionOnlyone.signalProcessingFirwin(c, 15, 20, 500, 500,Ave=False, save=save,show=show)
        d = FunctionOnlyone.signalProcessingFirwin(d,15,20,500,500,Ave=False, save=save, show=show)
        name = str("Filtered"+str(subjek[i]))
        FunctionOnlyone.createFile2(c,d,name,str(i),subjek=folder)
        i += 1
    print("Pengamilan data 20x selesai!")
    print("Menampilkan hasil data..")

    # ke = FunctionOnlyone.plotData20( dataA , dataB , t , 15,subjek, ke=ke)

akusisi()




        




        