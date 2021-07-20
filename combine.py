import numpy
from stl import mesh
from slice3 import Triangle, incrementalSlicing 
from slice2 import Segment, incrementalSlicing_y, incrementalSlicing_x
import time
def slice(dl,dl1,filename='test3.stl'):
	m1 = mesh.Mesh.from_file(filename)
	for t in m1.vectors:
	    for i in range(3):
	        for j in range(3):
	            t[i][j]=round(t[i][j],2)
	T=[Triangle(*t) for t in m1.vectors]
	low=None
	high=None
	for t in T:
	    if low == None:
	        low=t.zmin
	        high=t.zmax
	    if t.zmin<low:
	        low=t.zmin
	    if t.zmax>high:
	        high=t.zmax
	P=[]
	ll=low
	while not ll>high:
	    P.append(ll+0.005)
	    ll+=dl
	S=incrementalSlicing(len(T),T,len(P),P,dl,False)

	O=[]
	for i in range(len(S)):
		Seg=[]
		for s in S[i]:
			Seg.append(Segment(s[0],s[1]))
		if i%2==0:
			temp = incrementalSlicing_y(len(Seg),Seg,dl1)
		else:
			temp = incrementalSlicing_x(len(Seg),Seg,dl1)
		O.append(temp)
	
	return S,O

if __name__ == "__main__":
    S,O = slice(5,5)
    import matplotlib.pyplot as plt
    import mpl_toolkits.mplot3d as plt3d
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    X = []
    Y = []
    Z = []
    for ss in S:
        for s in ss:
            for p in s:
                X.append(p[0])
                Y.append(p[1])
                Z.append(p[2])
    ax.plot(X,Y,Z)

    fig1 = plt.figure(2)
    ax1 = fig1.add_subplot(111, projection='3d')
    #plt.show()
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


    plt.show()
