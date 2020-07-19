import matplotlib.pyplot as plt
import numpy as np



# Some example data to display
x = np.linspace(0, 10)
x = np.cos(x)
y = np.sin(x)

def addData(data1, data2):
    data=[]
    i=0
    j=0
    jumlah=len(data1)
    jumlahAll = (len(data1)+len(data2))
    print(jumlah, jumlahAll)
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


j = addData(x,x)

print(len(j))

    
    
def plotFigure3(a, b, c,d,e,f,FullA, FullB, time, ke, name):
    name = "./data/"+ name +"/" + name +  ke + ".png"
    j = []
    x = np.linspace(0, 10)
    x = np.cos(x)
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
    plt.ylim(0,6)
    plt.subplot(grid[0,1])
    plt.plot(b)
    plt.ylim(0,6)
    plt.title("B")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(c)
    plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.title("C")
    plt.ylabel("Volt")
    plt.xticks(o, oi)
    plt.subplot(grid[1,1])
    plt.plot(d)
    plt.ylim(0,6)
    plt.title("D")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[2,0])
    plt.plot(e)
    plt.ylim(0,6)
    plt.title("E")
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.xticks(o, oi)
    plt.subplot(grid[2,1])
    plt.plot(f)
    plt.xlabel("time(s)")
    plt.ylim(0,6)
    plt.title("F")
    plt.xticks(o, oi)
    plt.subplot(grid[3,:2])
    plt.plot(FullA)
    plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaA")
    plt.subplot(grid[4,:2])
    plt.plot(FullB)
    plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaB")
    plt.savefig(name)
    plt.show()





def plotFigure(a, b, c,d,e,f,FullA, FullB):
    j = []
    x = np.linspace(0, 10)
    x = np.cos(x)
    j.append(x)
    j.append(a)
    j.append(b)
    j.append(c)
    j.append(d)
    j.append(e)
    j.append(f)
    j.append(FullA)
    j.append(FullB)
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.5, wspace=0.3)
    for i in range(1,9):
        ax = fig.add_subplot(4, 2, i)
        ax.plot(j[i])
    plt.show()


def plotFigure2(a, b, c,d,e,f,FullA, FullB, time):
    j = []
    x = np.linspace(0, 10)
    x = np.cos(x)
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
    plt.ylim(0,6)
    plt.subplot(grid[0,1])
    plt.plot(b)
    plt.ylim(0,6)
    plt.title("B")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[1,0])
    plt.plot(c)
    plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.title("C")
    plt.ylabel("Volt")
    plt.xticks(o, oi)
    plt.subplot(grid[1,1])
    plt.plot(d)
    plt.ylim(0,6)
    plt.title("D")
    plt.xlabel("time(s)")
    plt.xticks(o, oi)
    plt.subplot(grid[2,0])
    plt.plot(e)
    plt.ylim(0,6)
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
    plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaA")
    plt.subplot(grid[4,:2])
    plt.plot(FullB)
    # plt.ylim(0,6)
    plt.xlabel("time(s)")
    plt.ylabel("Volt")
    plt.title("FullaB")
    plt.show()

time = 30
plotFigure3(x,y,x,y,x,y,FullA=j,FullB=j, time=time, ke="hehe",name="Ilham")