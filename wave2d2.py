import time
from tkinter import *
from linspace import *
from math import *

root=Tk()
root.title("wave eq")
root.geometry("500x500")
graph=Canvas(root,width=300,height=200,bg="green")
graph.pack(fill="both",expand=True)

#f=k*d
n=100
a=0
b=100
x=linspace(a,b,n)
y=[]
for i in range(len(x)):
    y.append(50*sin(pi/10*x[i]))

vy=[]
for i in range(len(x)):
    vy.append(0)

AL=0 #get arclength
#for i in range(len(x)):
    

k=1
m=10
dt=.1


j=0
while True:
    j+=1
    for i in range(len(x)-1):
        graph.create_line(x[i]+100,y[i]+250,x[i+1]+100,y[i+1]+250,fill="blue",width=2)
        
    for i in range(1,len(x)-1): #update y positions
        d1=y[i]-y[i-1]
        d2=y[i]-y[i+1]
        F=-k*(d1+d2)
        a=F/m
        vy[i]+=a*dt
        y[i]+=vy[i]*dt
    #print(vy[50])
    
    root.update()
    #if j%1==0:
    graph.delete('all')

      

#show next: solve heat equation with cv2 lines making a video

