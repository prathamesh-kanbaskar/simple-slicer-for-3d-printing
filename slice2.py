import math 

class Segment:
    def __init__(self, v1, v2):
        self.v1=v1
        self.v2=v2
        self.ymin=min(v1[1], v2[1])
        self.ymax=max(v1[1], v2[1])
        self.xmin=min(v1[0], v2[0])
        self.xmax=max(v1[0], v2[0])

def computeIntersection_y(t,y):
    x1=t.v1[0]
    y1=t.v1[1]
    x2=t.v2[0]
    y2=t.v2[1]
    z=t.v1[2]
    if x1==x2:
        return [x1,y,z]
    else:
        m=(y2-y1)/(x2-x1)
        c=(x2*y1-x1*y2)/(x2-x1)
        if m==0:
            return [x1,y,z]
        else:
            x=(y-c)/m
            return [x,y,z]
def bulidSegmentList_y(n,T,k,P,dl):
    L=[set() for i in range(k+2)]
    for t in T:
        i=math.floor((t.ymin-P[0]+0.005)/dl)+1
        L[i].add(t)
    return L
def incrementalSlicing_y(n,T,dl):
    low=None
    high=None
    for t in T:
        if low == None:
            low=t.ymin
            high=t.ymax
        if t.ymin<low:
            low=t.ymin
        if t.ymax>high:
            high=t.ymax
    if low==None:
        return []
    P=[]
    ll=low
    while not ll>high:
        P.append(ll+0.005)
        ll+=dl
    k = len(P)
    L=bulidSegmentList_y(n,T,k,P,dl)
    S=[[] for i in range(k)]
    A=set()
    for i in range(k):
        A= A | set(L[i])
        Acp=set(A)
        for t in Acp:
            if t.ymax<P[i]:
                A.remove(t)
            else:
                #print("z coord",P[i])
                q=computeIntersection_y(t,P[i])
                S[i].append(q)
    for i in range(len(S)):
        if i%2:
            S[i].sort()
        else:
            S[i].sort(reverse=True)
    return S


def computeIntersection_x(t,x):
    x1=t.v1[0]
    y1=t.v1[1]
    x2=t.v2[0]
    y2=t.v2[1]
    z=t.v1[2]
    if y1==y2:
        return [x,y1,z]
    else:
        m=(x2-x1)/(y2-y1)
        c=(y2*x1-y1*x2)/(y2-y1)
        if m==0:
            return [x,y1,z]
        else:
            y=(x-c)/m
            return [x,y,z]
def bulidSegmentList_x(n,T,k,P,dl):
    L=[set() for i in range(k+2)]
    for t in T:
        i=math.floor((t.xmin-P[0]+0.005)/dl)+1
        L[i].add(t)
    return L
def incrementalSlicing_x(n,T,dl):
    low=None
    high=None
    for t in T:
        if low == None:
            low=t.xmin
            high=t.xmax
        if t.xmin<low:
            low=t.xmin
        if t.xmax>high:
            high=t.xmax
    if low==None:
        return []
    P=[]
    ll=low
    while not ll>high:
        P.append(ll+0.005)
        ll+=dl
    k = len(P)
    L=bulidSegmentList_x(n,T,k,P,dl)
    S=[[] for i in range(k)]
    A=set()
    for i in range(k):
        A= A | set(L[i])
        Acp=set(A)
        for t in Acp:
            if t.xmax<P[i]:
                A.remove(t)
            else:
                #print("z coord",P[i])
                q=computeIntersection_x(t,P[i])
                S[i].append(q)
    for i in range(len(S)):
        if i%2:
            S[i].sort(key=lambda x:x[1])
        else:
            S[i].sort(key=lambda x:x[1],reverse=True)
    return S





"""
n = 4
t1 = Segment([0,0,0],[100,0,0])
t3 = Segment([100,0,0],[100,100,0])
t2 = Segment([100,100,0],[0,100,0])
t4 = Segment([0,100,0],[0,0,0])
T = [t1,t2,t3,t4]

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import collections as mc
fig = plt.figure()
ax = fig.add_subplot(111)
X=[0,100,100,0]
Y=[0,0,100,100]
ax.scatter(X,Y)
"""


"""
low=None
high=None
for t in T:
    if low == None:
        low=t.ymin
        high=t.ymax
    if t.ymin<low:
        low=t.ymin
    if t.ymax>high:
        high=t.ymax
P=[]
ll=low
while not ll>high:
    P.append(ll+0.005)
    ll+=dl
k = len(P)
"""
"""
dl=1
S = incrementalSlicing_y(n,T,dl)
X=[]
Y=[]
for ss in S:
    for s in ss:
        X.append(s[0])
        Y.append(s[1])
ax.scatter(X,Y)
"""
"""
for ss in S:
    xs=[]
    ys=[]
    for s in ss:
        xs.append(s[0])
        ys.append(s[1])
    l = Line2D(xs,ys)
    ax.add_line(l)
"""
#plt.show()
