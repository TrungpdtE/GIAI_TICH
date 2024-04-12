#Baitap1

import math

#caua

def f1_sqrt(x):
    math.sqrt(10) 
    return math.sqrt(x) 

#caub

def f2(x):

    f2=pow(x,1/3)

    return f2

#cauc

def f3(x):

    f3=x**(2/3)

    return f3

#caud 

def f4(x):

    f4=(x**3)/3 - (x**2)/2 - 2*x + 1/3

    return f4

#caue

def f5(x):

    f5=((2*(x**2))-3)/(7*x+4)

    return f5

#cauf

def f6(x):

    f6=((5*(x**2))+8*x-3)/((3*(x**2))+2)

    return f6

#caug

def f7(x):

    f7=math.sin(x)

    return f7

#cauh

def f8(x):

    f8=math.cos(x)

    return f8

#caui

def f9(x):

    f9=pow(3,x)

    return f9

#cauj

def f10(x):

    f10=pow(10,-x)

    return f10

#cauk

def f11(x):

    f11=pow(math.e,x)

    return f11

#caul

def f12(x):

    f12=math.log2(x)

    return f12

#caum

def f13(x):

    f13=math.log10(x)

    return f13

#caun

def f14(x):

    f14=math.loge(x)

    return f14

#main 

print(f1_sqrt(4))

#caua

print(f2(8))

#caub

print(f3(32))

#cauc

print(f4(10))

#caud

print(f5(10))

#caue

print(f6(9))

#cauf

print(f7(55))

#caug

print(f8(223))

#cauh

print(f9(445))

#cauj

print(f10(46))

#cauk

print(f11(55))

#caul

print(f12(4))

#caum

print(f13(9))

#caun

#bai3
import numpy as np
f1b3= lambda x: x+5
f2b3= lambda x: x**2-3
#caua
print("f1b3(f2b3(0)=", f1b3(f2b3(0)))
#caub
print("f1b3(f2b3(0))=", f2b3(f1b3(0)))
#cauc
print("f1b3(f1b3(-5))=", f1b3(f1b3(-5)))
#caud
print("f2b3(f2b3(2))=",f2b3(f2b3(2)))

#Bai4
import matplotlib.pyplot as plt
import numpy as np
#caua
fx_4i = lambda x:(-x**3)
x_array= np.arange(-15,15.1,0.1)
y_array= list(map(fx_4i,x_array))
plt.plot (x_array, y_array, color='red')
plt.grid()
plt.show()
print("4i, f(x) is decreasing as x-values belong to (-oo, +oo)")
#caub 
import matplotlib.pyplot as plt
import numpy as np
fx_4k = lambda x: -1/x
xk_array= np.arange(-100,150,1)
yk_array=list(map(fx_4k,xk_array))
plt.plot (xk_array, yk_array, color='yellow')
plt.grid()
plt.show()
print("4k, f(x) is decreasing as x-values belong to (-oo; +oo)")
#cauj
import matplotlib.pyplot as plt
import numpy as np
fx_4j = lambda x: -1/(x**2)
xj_array= np.arange(-100,150,1)
yj_array=list(map(fx_4j,xj_array))
plt.plot (xj_array, yj_array, color='blue')
plt.grid()
plt.show()
print("4j, f(x) is decreasing as x-values belong to (-oo; +oo)")
#caum
import matplotlib.pyplot as plt
import numpy as np
fx_4m = lambda x: math.sqrt(abs(x))
xm_array= np.arange(-10,10,1)
ym_array=list(map(fx_4m,xm_array))
plt.plot (xm_array, ym_array, color='black')
plt.grid()
plt.show()
print("4m, f(x) is decreasing as x-values belong to (-oo; +oo)")
#caul
import matplotlib.pyplot as plt
import numpy as np
fx_4l = lambda x: 1/abs(x)
xl_array= np.arange(-100,100,1)
yl_array=list(map(fx_4l,xl_array))
plt.plot (xl_array, yl_array, color='pink')
plt.grid()
plt.show()
print("4l, f(x) is decreasing as x-values belong to (-oo; +oo)")
#caun
import matplotlib.pyplot as plt
import numpy as np
fx_4n = lambda x: math.sqrt(abs(-x))
xn_array= np.arange(-106,106,1)
yn_array=list(map(fx_4n,xn_array))
plt.plot (xn_array, yn_array, color='orange')
plt.grid()
plt.show()
print("4n, f(x) is decreasing as x-values belong to (-oo; +oo)")

#cau5 
import matplotlib.pyplot as plt
import numpy as np
fx_15 = lambda x : (math.sqrt(1 - (abs(x)-1)**2))
fx_25= lambda x : ((-3) * math.sqrt(1 - math.sqrt(abs(x)/2)))
x5_array = np.arange(-2, 2, 0.001)
y15_array = list(map(fx_15,x5_array))
y25_array = list(map(fx_25, x5_array))
plt.plot (x5_array, y15_array, color='magenta')
plt.plot (x5_array, y25_array, color='red')
plt.grid()
plt.show()
#baitap7
#caua
import matplotlib.pyplot as plt
import numpy as np

def test(x,fx):
    y= []
    for i in x:
        y.append(round(fx(i), 1))
    print(y)
    if len(y) == len(set(y)):
        plt.plot(x,y,color='blue',label = "day la ham anh xa 1 1")
    else :
        plt.plot(x,y,color='red',label = "day khong phai la ham anh xa 1 1")

fa = lambda x: x** 3 - x / 2
x = np.arange(-20, 21, 1)
test(x,fa)
plt.legend()
plt.show()

fb = lambda x: x * x + x / 2
x = np.arange(-20, 21, 0.1)
test(x,fb)
plt.legend()
plt.show()
#baitap6
#cau6 
import matplotlib.pyplot as plt
import numpy as np
import math

#cau6a():
f6_a = lambda x, k: x**2+k
x = np.arange(-10, 10.1, 0.1)
for ki in np.arange(2, 13, 2):
    y = []
    for xi in x:
        y.append(f6_a(xi,ki))
    plt.plot(x,y,label = "k = " + str(ki))
plt.title("Bai 6a")
plt.legend()
plt.show()
plt.show()


#cau 6b
f6_b = lambda x, k: (x + k)**2
x = np.arange(-10, 10.1, 0.1)
for ki in np.arange(2, 13, 2):
    y = []
    for xi in x:
        y.append(f6_b(xi,ki))
    plt.plot(x,y,label = "k = " + str(ki))
plt.title("Bai 6b")
plt.legend()
plt.show()
#cau 6c
f6_c = lambda x,k : k * math.sqrt(x)
x = np.arange(1, 50.1, 0.1)
k = np.array([1/3, 1, 3, 6])

for ki in k:
    y=[]
    for xi in x:
        y.append(f6_c(xi,ki))
    plt.plot(x,y,label = "k = " + str(ki))
plt.title("Bai 6c")
plt.legend()
plt.show()

#cau 6d
f6_d = lambda x: (x + 1) ** 3 - 1

x = np.arange(-10, 10.1, .1)
y = np.array(list(map(f6_d,x)))

plt.plot(x,y, label='yellow')
plt.plot(x-1,y-1, label='red')

plt.title("Bai 6d")
plt.legend()
plt.show()

#Cau 6e :
f6_e = lambda x:( x - 1)** (2/3) - 1

x = np.arange(-10, 10.1, .1)
y = np.array(list(map(f6_e,x)))

plt. plot (x,y, label='blue')
plt. plot (x+1,y-1, label='red')

plt.title("Bai 6e")
plt.legend()
plt.show()


#cau 6f 
f6_f = lambda x: 1/2*(x+1)+5

x = np.arange(-10, 10.1, 0.1)
y = np.array(list(map(f6_f, x)))

plt.plot(x,y,  label='black')
plt.plot(x+1,y-5,  label='red')

plt.title("Bai 6f")
plt.legend()
plt.show()

# Cau 6g
f6_g = lambda x: 1/(x*x)

x = np.arange(-10, 10.1, 1)
y = np.array(list(map(f6_g,x)))

plt.plot(x,y,label='brown')
plt.plot(x-2,y-1,label='brown')

plt.title("Bai 6g")
plt.legend()
plt.show()

# Cau 6h 
g6_h = lambda x : 1 - (x)**3

x = np.arange(-10, 10.1, 0.1)

y = np.array(list(map(g6_h,x)))
y_stretched = np.array(list(map(g6_h,x/2)))

plt.plot(x,y,label='violet')
plt.plot(x,y_stretched,label='red')

plt.title("Bai 6h")
plt.legend()
plt.show()

# Cau 6i
g6_i = lambda x : math.sqrt(x + 1)
x = np.arange(-1 / 4, 10.1, 0.1)

y = np.array(list(map(g6_i,x)))
y_compressed = np.array(list(map(g6_i,x*4)))

plt.plot(x,y,label='Pink')
plt.plot(x,y_compressed,label='red')

plt.title("Bai 6i")
plt.legend()
plt.show()


