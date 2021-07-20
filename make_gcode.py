from combine import slice
import time

File=input("enter File name: ")
DL=float(input("enter layer thickness: "))
dl=float(input("enter extrusion Width: "))

tic = time.time()
S,O = slice(DL,dl,"stl/"+File+".stl")
toc=time.time()
print("Slicing and path calculaton done in ",toc-tic, "seconds")
tic=time.time()
f0=500
e0=0.02
file = open("gcode.txt","w")
for temp in O:
	for t in temp:
		for i in range(len(t)):
			if i==0:
				file.write("G1 X"+str(t[i][0])+" Y"+str(t[i][1])+" Z"+str(t[i][2])+" F"+str(f0)+" E"+str(e0)+"\n")
			elif i%2==0:
				file.write("G0 X"+str(t[i][0])+" Y"+str(t[i][1])+" Z"+str(t[i][2])+"\n")
			else:
				file.write("G1 X"+str(t[i][0])+" Y"+str(t[i][1])+" Z"+str(t[i][2])+" F"+str(f0)+" E"+str(e0)+"\n")
toc=time.time()
print("G-code Generation completed in ",toc-tic, "seconds")
print("Now Plotting contours and 3d printed product .... ")

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
'''X = []
Y = []
Z = []
for ss in S:
    for s in ss:
        for p in s:
            X.append(p[0])
            Y.append(p[1])
            Z.append(p[2])
ax.plot(X,Y,Z)'''
for ss in S:
    #print(ss)
    for s in ss:     
        ax.plot([s[0][0],s[1][0]] , [s[0][1],s[1][1]] , [s[0][2],s[1][2]],color='C0')
 


fig1 = plt.figure(2)
ax1 = fig1.add_subplot(111, projection='3d')
prev=None
for temp in O:
    for t in temp:
        for i in range(len(t)):
            if prev == None:
                prev=t[i]
            elif ( i%2==0):
                prev=t[i]
            else:
                ax1.plot([prev[0],t[i][0]] , [prev[1],t[i][1]] , [prev[2],t[i][2]],color='gray')
                prev=t[i]
    prev=None
'''
fig1 = plt.figure(2)
ax1 = fig1.add_subplot(111, projection='3d')
for i in range(len(O)):
	X = []
	Y = []
	Z = []
	for t in O[i]:
	    for p in t:
	        X.append(p[0])
	        Y.append(p[1])
	        Z.append(p[2])
	ax1.plot(X,Y,Z,color='gray')

'''
plt.show()
