#-*- coding: UTF-8 -*-
import turtle as t

x1,y1 = input("左上角坐标:")
x2,y2 = input("右下角坐标:")
n = input("放大倍数:")
xav=x1+(x2-x1)/2
yav=y1+(y2-y1)/2
print xav
print yav
fp = open("gridt.dat", 'rb')
data = fp.readlines()
x = []
y = []
for num in data:
    x.append(float(num.split()[0]))
    y.append(float(num.split()[1]))
fp=open("nod.dat",'rb')
data = fp.readlines()
p_1 = []
p_2 = []
p_3 = []
for num in data:
    p_1.append(int(num.split()[0]))
    p_2.append(int(num.split()[1]))
    p_3.append(int(num.split()[2]))
fp.close()
t.screensize(2000,2000)
t.setup(width=2000, height=2000, startx=100, starty=100)
t.pensize(1)
t.hideturtle()
t.tracer(False)
for i in range(len(p_2)):
    if((x1<x[p_1[i]-1] and x[p_1[i]-1]<x2 and y2<y[p_1[i]-1] and y[p_1[i]-1]<y1) or (x1<x[p_2[i]-1] and x[p_2[i]-1]<x2 and y2<y[p_2[i]-1] and y[p_2[i]-1]<y1) or (x1<x[p_3[i]-1] and x[p_3[i]-1]<x2 and y2<y[p_3[i]-1] and y[p_3[i]-1]<y1)):
        t.penup()

        t.goto((x[p_1[i]-1]-xav)*n, (y[p_1[i]-1]-yav)*n)
        t.pendown()
        t.goto((x[p_2[i]-1]-xav)*n, (y[p_2[i]-1]-yav)*n)
        t.goto((x[p_3[i]-1]-xav)*n, (y[p_3[i]-1]-yav)*n)
        t.goto((x[p_1[i]-1]-xav)*n, (y[p_1[i]-1]-yav)*n)
t.hideturtle()
ts = t.getscreen()
ts.getcanvas().postscript(file="jsr3.eps")
t.done()