import numpy as np
import matplotlib.pyplot as plt
import time
import math
#-----------------------------------------------------------------------------------------------------------------------
xs=[]#그래프xs
ys=[]#그래프ys
B=10#자기장세기
A=5#코일의 면적
T=10#회전주기
θ=0#각도
N=1#코일 감은수
dt=0.01#단위시간
timelist=[]
for i in range(0,1000000):
  timelist.append(i/(1/dt))
ST=time.time()
#-----------------------------------------------------------------------------------------------------------------------
for k in range(0,1000000): #한번 반복하는데 걸리는 시간 dt
  print((time.time()-ST))
  if timelist[k]<=(time.time()-ST)<=timelist[k+100]:
    t=timelist[k]
    θ=t/(T/2*math.pi)
    xs.append(t)
    ys.append(-N*B*A*(2*math.pi/T)*np.cos((2*math.pi/T)*t))
    plt.plot(xs,ys,c="b",linewidth=1)
    plt.xlim([0, 30])
    plt.ylim([-(N*B*A*2*math.pi/T)-5,(N*B*A*2*math.pi/T)+5])
    plt.title("Alternator")
    plt.xlabel('time')
    plt.ylabel('induced electromotive force')
    plt.pause(0.001)
plt.show()
#-----------------------------------------------------------------------------------------------------------------------
#보고서(수식유도과정)
#디자인
#전류방향
#-----------------------------------------------------------------------------------------------------------------------
#Φs=[0]
#Ar=5#통과면적
# Ar=5*np.sin(θ)
# Φ=B*Ar
# Φs.append(Φ)
# print(Φs)
# dΦ=Φs[-1]-Φs[-2]
