from combine import slice

File=input("enter File name: ")
DL=float(input("enter layer thickness: "))
dl=float(input("enter extrusion Width: "))

S,O = slice(DL,dl,"stl/"+File+".stl")

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from itertools import count

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.style.use('fivethirtyeight')
#fig1 = plt.figure(2)
#ax1 = fig1.add_subplot(111, projection='3d')
prev=None
STIM=[]
for temp in O:
    for t in temp:
        for i in range(len(t)):
            if prev == None:
                prev=t[i]
            elif (i!=0 and i%2==0):
                prev=t[i]
            else:
                STIM.append(([prev[0],t[i][0]] , [prev[1],t[i][1]] , [prev[2],t[i][2]]))
                #ax1.plot([prev[0],t[i][0]] , [prev[1],t[i][1]] , [prev[2],t[i][2]],color='gray')
                prev=t[i]
    prev=None

index = count()

def animate(i):
    print(i)
    #ax.cla()
    ax.plot(STIM[i][0], STIM[i][1],STIM[i][2],color='green')
    #plt.plot(x_vals, y_vals)

ani=FuncAnimation(plt.gcf(), animate, interval= 100)


plt.show()
