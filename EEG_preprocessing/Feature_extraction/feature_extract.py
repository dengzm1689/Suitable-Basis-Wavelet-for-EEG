""" BEFORE EXTRACTING FEATURES FROM WAVELET COEFFECIENTS CHECK THE SHAPE OF INPUT DATASET!!!"""

from numpy import genfromtxt
from pyentrp import entropy
import numpy as np
import math

def renyi_entropy(d1,d2,d3,d4,d5):

    d1=np.rint(d1)
    d2=np.rint(d2)
    d3=np.rint(d3)
    d4=np.rint(d4)
    d5=np.rint(d5)
    
    rend1=[];rend2=[];rend3=[];rend4=[];rend5=[]
    alpha=2    
    for i in range(0,500):
        print(i)
        X=d1[i]
        data_set = list(set(X))
        freq_list = []
        for entry in data_set:
            counter = 0.
            for i in X:
                if i == entry:
                    counter += 1
            freq_list.append(float(counter)/len(X))
        summation=0
        for freq in freq_list:
            summation+=math.pow(freq,alpha)
        Renyi_En=(1/float(1-alpha))*(math.log(summation,2))
        rend1.append(Renyi_En)

    for i in range(0,500):
        X=d2[i]
        print(i)
        data_set = list(set(X))
        freq_list = []
        for entry in data_set:
            counter = 0.
            for i in X:
                if i == entry:
                    counter += 1
            freq_list.append(float(counter)/len(X))
        summation=0
        for freq in freq_list:
            summation+=math.pow(freq,alpha)
        Renyi_En=(1/float(1-alpha))*(math.log(summation,2))
        rend2.append(Renyi_En)

    for i in range(0,500):
        X=d3[i]
        print(i)
        data_set = list(set(X))
        freq_list = []
        for entry in data_set:
            counter = 0.
            for i in X:
                if i == entry:
                    counter += 1
            freq_list.append(float(counter)/len(X))
        summation=0
        for freq in freq_list:
            summation+=math.pow(freq,alpha)
        Renyi_En=(1/float(1-alpha))*(math.log(summation,2))
        rend3.append(Renyi_En)

    for i in range(0,500):
        X=d4[i]
        print(i)
        data_set = list(set(X))
        freq_list = []
        for entry in data_set:
            counter = 0.
            for i in X:
                if i == entry:
                    counter += 1
            freq_list.append(float(counter)/len(X))
        summation=0
        for freq in freq_list:
            summation+=math.pow(freq,alpha)
        Renyi_En=(1/float(1-alpha))*(math.log(summation,2))
        rend4.append(Renyi_En)

    for i in range(0,500):
        X=d5[i]
        print(i)
        data_set = list(set(X))
        freq_list = []
        for entry in data_set:
            counter = 0.
            for i in X:
                if i == entry:
                    counter += 1
            freq_list.append(float(counter)/len(X))
        summation=0
        for freq in freq_list:
            summation+=math.pow(freq,alpha)
        Renyi_En=(1/float(1-alpha))*(math.log(summation,2))
        rend5.append(Renyi_En)
    return(rend1,rend2,rend3,rend4,rend5)

def permu(d1,d2,d3,d4,d5):
    
    pd1=[];pd2=[];pd3=[];pd4=[];pd5=[]
    
    for i in range(0,500):
        X=d1[i]
        print(i)
        pd1.append(entropy.permutation_entropy(X,3,1))
    for i in range(0,500):
        X=d2[i]
        print(i)
        pd2.append(entropy.permutation_entropy(X,3,1))
    for i in range(0,500):
        X=d3[i]
        print(i)
        pd3.append(entropy.permutation_entropy(X,3,1))
    for i in range(0,500):
        X=d4[i]
        print(i)
        pd4.append(entropy.permutation_entropy(X,3,1))
    for i in range(0,500):
        X=d5[i]
        print(i)
        pd5.append(entropy.permutation_entropy(X,3,1))

    return(pd1,pd2,pd3,pd4,pd5)
    
def sampl(d1,d2,d3,d4,d5):

    sa1=[];sa2=[];sa3=[];sa4=[];sa5=[]

    for i in range(0,500):
        X=d1[i]
        std_X = np.std(X)
        ee=entropy.sample_entropy(X,2,0.2*std_X)
        sa1.append(ee[0])

    for i in range(0,500):
        X=d2[i]
        std_X = np.std(X)
        ee=entropy.sample_entropy(X,2,0.2*std_X)
        sa2.append(ee[0])

    for i in range(0,500):
        X=d3[i]
        std_X = np.std(X)
        ee=entropy.sample_entropy(X,2,0.2*std_X)
        sa3.append(ee[0])

    for i in range(0,500):
        X=d4[i]
        std_X = np.std(X)
        ee=entropy.sample_entropy(X,2,0.2*std_X)
        sa4.append(ee[0])

    for i in range(0,500):
        X=d5[i]
        std_X = np.std(X)
        ee=entropy.sample_entropy(X,2,0.2*std_X)
        sa5.append(ee[0])

    return(sa1,sa2,sa3,sa4,sa5)

def shan(d1,d2,d3,d4,d5):

    sh1=[];sh2=[];sh3=[];sh4=[];sh5=[]
    d1=np.rint(d1)
    d2=np.rint(d2)
    d3=np.rint(d3)
    d4=np.rint(d4)
    d5=np.rint(d5)
    for i in range(0,500):
        X=d1[i]
        print(i)
        sh1.append(entropy.shannon_entropy(X))
    for i in range(0,500):
        X=d2[i]
        print(i)
        sh2.append(entropy.shannon_entropy(X))
    for i in range(0,500):
        X=d3[i]
        print(i)
        sh3.append(entropy.shannon_entropy(X))
    for i in range(0,500):
        X=d4[i]
        print(i)
        sh4.append(entropy.shannon_entropy(X))
    for i in range(0,500):
        X=d5[i]
        print(i)
        sh5.append(entropy.shannon_entropy(X))
    return(sh1,sh2,sh3,sh4,sh5)

d1= genfromtxt('Data/db10D1.csv', delimiter=',', skip_header=0)
d2= genfromtxt('Data/db10D2.csv', delimiter=',', skip_header=0)
d3= genfromtxt('Data/db10D3.csv', delimiter=',', skip_header=0)
d4= genfromtxt('Data/db10D4.csv', delimiter=',', skip_header=0)
d5= genfromtxt('Data/db10A4.csv', delimiter=',', skip_header=0)

sa1,sa2,sa3,sa4,sa5=sampl(d1,d2,d3,d4,d5)
r1,r2,r3,r4,r5=renyi_entropy(d1,d2,d3,d4,d5)
p1,p2,p3,p4,p5=permu(d1,d2,d3,d4,d5)
sh1,sh2,sh3,sh4,sh5=shan(d1,d2,d3,d4,d5)

X=[r1,r2,r3,r4,r5,p1,p2,p3,p4,p5,sh1,sh2,sh3,sh4,sh5,sa1,sa2,sa3,sa4,sa5]

def energy(d1,d2,d3,d4,d5):

    en1=[];en2=[];en3=[];en4=[];en5=[]
    for i in range(0,500):
        X=d1[i]
        summ=0
        for i in X:
            summ+=(i**2)
        en1.append(summ)
    for i in range(0,500):
        X=d2[i]
        summ=0
        for i in X:
            summ+=(i**2)
        en2.append(summ)
    for i in range(0,500):
        X=d3[i]
        summ=0
        for i in X:
            summ+=(i**2)
        en3.append(summ)
    for i in range(0,500):
        X=d4[i]
        summ=0
        for i in X:
            summ+=(i**2)
        en4.append(summ)
    for i in range(0,500):
        X=d5[i]
        summ=0
        for i in X:
            summ+=(i**2)
        en5.append(summ)

    return(en1,en2,en3,en4,en5)

d1= genfromtxt('Data/db14D1.csv', delimiter=',', skip_header=0)
d2= genfromtxt('Data/db14D2.csv', delimiter=',', skip_header=0)
d3= genfromtxt('Data/db14D3.csv', delimiter=',', skip_header=0)
d4= genfromtxt('Data/db14D4.csv', delimiter=',', skip_header=0)
d5= genfromtxt('Data/db14A4.csv', delimiter=',', skip_header=0)

e1,e2,e3,e4,e5=energy(d1,d2,d3,d4,d5)
X=[e1,e2,e3,e4,e5]

X=np.array(X)
X=X.T
a = np.asarray(X)
np.savetxt("Db30_features.csv", a, delimiter=",")