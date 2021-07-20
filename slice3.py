# n no of triangles
# k no of slicing planes
# T list of tringle objects
# P list of z coordinate of plane in increasing order
# dl dist bw slice plane
# srt true if T is sorted by zmin
# 
# 
# 

import math 

class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3
        self.zmin=min(v1[2], v2[2], v3[2])
        self.zmax=max(v1[2], v2[2], v3[2])

def computeIntersection(t,z):
    #print(t.v1,t.v2,t.v3)
    if t.v1[2]==t.v2[2] and t.v2[2] ==t.v3[2]:
        return [None, None]
    q=[]
    y1=t.v1[1]
    y2=t.v2[1]
    z1=t.v1[2]
    z2=t.v2[2]
    #print(y1,y2,z1,z2)
    if(z2-z1!=0):    
        y=y1+ (z-z1)/(z2-z1)*(y2-y1)
        #print(y)
        if y<=max(y1,y2) and y>=min(y1,y2):
            x=t.v1[0]+ (z-z1)/(z2-z1)*(t.v2[0]-t.v1[0])
            q.append([x,y,z])
        
    y1=t.v2[1]
    y2=t.v3[1]
    z1=t.v2[2]
    z2=t.v3[2]
    #print(y1,y2,z1,z2)
    if(z2-z1!=0):
        y=y1+ (z-z1)/(z2-z1)*(y2-y1)
        #print(y)
        if y<=max(y1,y2) and y>=min(y1,y2):
            x=t.v2[0]+ (z-z1)/(z2-z1)*(t.v3[0]-t.v2[0])
            q.append([x,y,z])

    y1=t.v3[1]
    y2=t.v1[1]
    z1=t.v3[2]
    z2=t.v1[2]
    #print(y1,y2,z1,z2)
    if(z2-z1!=0):
        y=y1+ (z-z1)/(z2-z1)*(y2-y1)
        #print(y)
        if y<=max(y1,y2) and y>=min(y1,y2):
            x=t.v3[0]+ (z-z1)/(z2-z1)*(t.v1[0]-t.v3[0])
            if len(q)<2:
                q.append([x,y,z])
    #print("THis is ",q)
    return q[0],q[1]



def bulidTriangleList(n,T,k,P,dl, srt):
    L=[set() for i in range(k+2)]
    for t in T:
        i=math.floor((t.zmin-P[0]+0.005)/dl)+1
        #print(i)
        L[i].add(t)
    return L

def incrementalSlicing(n,T,k,P,dl,srt):
    L=bulidTriangleList(n,T,k,P,dl, srt)
    #print(L)
    S=[[] for i in range(k)]
    A=set()
    for i in range(k):
        A= A | set(L[i])
        Acp=set(A)
        for t in Acp:
            if t.zmax<P[i]:
                A.remove(t)
            else:
                #print("z coord",P[i])
                q1,q2=computeIntersection(t,P[i])
                S[i].append((q1,q2))
    return S





    
        

        







