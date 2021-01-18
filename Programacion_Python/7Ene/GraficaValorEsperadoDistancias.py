#!/usr/bin/env python
# coding: utf-8


import numpy as np
import random as rnd
import matplotlib.pyplot as plt

def dist(A,B):
    
    x1 = A[0]
    x2 = B[0]
    y1 = A[1]
    y2 = B[1]    
    
    d = np.sqrt((x1-x2)**2 + (y1-y2)**2)  
    
    return d



Ns =  []
MUs = []

for N in range(1,6000):
    
    puntos = []


    for i in range(N):
        t = rnd.uniform(0,2*(np.pi))
        puntos.append((np.cos(t),np.sin(t)))  

    A = (1,0)
    mu = 0

    for Bk in puntos:
        mu = mu + dist(A,Bk)  # asi calculamos la suma de todas lpltas distancias

    Ns.append(N)
    MUs.append(mu/N)




plt.plot(Ns,MUs,'.')
plt.axhline(4/(np.pi),color='orange')
plt.title("Grafica de $\mu$ vs $N$")
plt.xlabel("$N$")
plt.ylabel("$\mu$")
plt.show()


# #################################
# ##########################


   
puntos = []

for i in [0.1,0.01,0.001,0.0001,.00001]:

    for t in np.arange(0,2*(np.pi),i):
        puntos.append((np.cos(t),np.sin(t)))   

    A = (1,0)  
    mu = 0
    N = len(puntos) 

    for Bk in puntos:
        mu = mu + dist(A,Bk)  # asi calculamos la suma de todas lpltas distancias

    Ns.append(N)
    MUs.append(mu/N)




plt.plot(Ns,MUs,'o')
plt.axhline(4/(np.pi),color='orange')
plt.title("Grafica de $\mu$ vs $N$")
plt.xlabel("$N$")
plt.ylabel("$\mu$")
plt.show()








