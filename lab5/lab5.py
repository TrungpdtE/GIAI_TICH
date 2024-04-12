import sympy as sp
import math


#Ex1
x = sp.symbols('x')
#cau1a
f1a = abs( x**2 - x - 7)
lm = sp.limit(f1a, x, 3)
print("1a - The limit of f(x) at x = 3: " + str(lm) )
#cau1b
f1b = abs(x-1)/(x**2-1)
lm = sp.limit(f1b, x, 1)
print("1b - The limit of f(x) at x = 1: " + str(lm) )
#1c
f1c = math.e ** (1/x)
lm = sp.limit(f1c, x, 1)
print("1c - The limit of f(x) at x = 1: " + str(lm) )
#cau1d
f1d = (x**4-16)/(x-2)
lm = sp.limit(f1d, x, 2)
print("1d - The limit of f(x) at x = 2: " + str(lm) )
#1e
f1e = (x**3-x**2-5*x-3)/((x+1)**2)
lm = sp.limit(f1e, x, -1)
print("1e - The limit of f(x) at x = -1: " + str(lm) )
#cau1f
f1f = (x**2-9)/((x**2+7)**(1/2)-4)
lm = sp.limit(f1f, x, 3)
print("1f - The limit of f(x) at x = 3: " + str(lm) )
#1g
f1g = (abs(x))/(sp.sin(x))
lm = sp.limit(f1g, x, 1)
print("1g - The limit of f(x) at x = 1: " + str(lm) )
#cau1h
f1h = (1-sp.cos(x))/(x*sp.sin(x))
lm = sp.limit(f1h, x, 0)
print("1h - The limit of f(x) at x = 0: " + str(lm) )
#cau1i
f1i = (2*x*x) / ( 3 - 3*sp.cos(x) )
lm = sp.limit(f1i, x, 0)
print("1i - The limit of f(x) at x = 0: " + str(lm) )
#cau1j
f1j = ((3+x)/(x-1))**x
lm = sp.limit(f1j, x, sp.oo)
print("1j - The limit of f(x) at x = oo: " + str(lm) )
#cau1k
f1k = (1-(2/(3+x))**x)
lm = sp.limit(f1k, x, sp.oo)
print("1k - The limit of f(x) at x = oo: " + str(lm) )
#cau1l
f1l = (1/x)**(1/x)
lm = sp.limit(f1l, x, sp.oo)
print("1l - The limit of f(x) at x = oo: " + str(lm) )
#cau1m
f1m=(-(x)**(1/3)+(1+x)**(1/3))/(-(x)**(1/2)+(1+x)**(1/2))
lm = sp.limit(f1m,x,sp.oo)
print("1m - The limit of f(x) at x = oo: " + str(lm))
#cau1n
f1n=sp.factorial(x)/(x**x)
lm = sp.limit(f1n,x,sp.oo)
print("1n - The limit of f(x) at x = oo: " + str(lm))






#Ex3
#a
f3_1 = 1/( 1 + 2**(1/x) )
lmRight = sp.limit(f3_1, x, 0, '+')
print ("gioi han phai = " , lmRight )
lmLeft = sp.limit(f3_1, x, 0, '-')
print ("gioi han trai = " , lmLeft )
if lmRight == lmLeft:
    print("ham so lien tuc tai:",lmRight)
#b
f3_2=(x**2+x)/(abs(x**3+x**2))
lmRight2 = sp.limit(f3_2, x, 0, '+')
print ("gioi han phai = " , lmRight2 )
lmLeft2 = sp.limit(f3_2, x, 0, '-')
print ("gioi han trai = " , lmLeft2 )
if lmRight2 == lmLeft2:
    print("ham so lien tuc tai:",lmRight2)





#Ex4
#1.limx=>0+f(x)
f4_a=sp.sin(1/x)
lm = sp.limit(f4_a,x,0,'+')
print("limx=>0+f(x)="+str(lm))
#2.limx=>0-f(x)
f4b=0
print("limx=>0-f(x)=",0)
#3.limx=>0f(x)
if f4_a == f4b :
    print("limx=>0f(x)=",f4b)







#Ex5
f5a=x**2 - 7
lmRight3 = sp.limit(f5a, x, 1, '+')
lmLeft3 = sp.limit(f5a, x, 1, '-')
if lmRight3 == lmLeft3:
    print("ham so lien tuc tai:",lmRight3)

f5b=(2*x-3)**(1/2)
lmRight4 = sp.limit(f5b, x, 1, '+')
lmLeft4 = sp.limit(f5b, x, 1, '-')
if lmRight4 == lmLeft4:
    print("ham so lien tuc tai:",lmRight4)



#Ex6 
#caua
print("xxxxxxxx")
import numpy as np 
f6a = (x**x-x-6)/(x-3)
lm_x_0 = sp.limit(f6a, x, 0)
for cal in np.arange(-100, 100, 1):
    if cal != 0:
        lm_x_a = sp.limit(f6a, x, cal )
        if lm_x_a == 5:
            print("ham so lien tuc tai diem x=0")
        else:
            print("ham so khong lien tuc tai diem x=0")
            break 


#caub
f6b=(x**3-8)/(x**2-3)
lm_x_0 = sp.limit(f6a, x, 2)
for cal in np.arange(-100, 100, 1):
    if cal != 0:
        lm_x_b = sp.limit(f6b, x, cal )
        if lm_x_b == 3:
            if lm_x_b == 4:
                print("ham so lien tuc tai diem x=2")
        else:
            print("ham so khong lien tuc tai diem x=2")
            break 


#cauc
f6c=(x**2-x-2)/(x-2)
lm_x_0 = sp.limit(f6c, x, 2)
for cal in np.arange(-100, 100, 1):
    if cal != 0:
        lm_x_c = sp.limit(f6c, x, cal )
        if lm_x_c == 1:
             print("ham so lien tuc tai diem x=2")
        else:
            print("ham so khong lien tuc tai diem x=2")
            break 


#caud
f6d=1/(x**2)
lm_x_0 = sp.limit(f6d, x, 0)
for cal in np.arange(-100, 100, 1):
    if cal != 0:
        lm_x_d = sp.limit(f6d, x, cal )
        if lm_x_d == 1:
             print("ham so lien tuc tai diem x=0")
        else:
            print("ham so khong lien tuc tai diem x=0")
            break