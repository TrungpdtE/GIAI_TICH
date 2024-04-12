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
def test(x,fx):
    y= []
    for i in x:

        y.append(round(fx(i), 1))
    print(y)
    if len(y) == len(set(y)):

        plt.plot(x,y,color='blue',label = "đây là Là hàm số ánh xạ một một")
    else:

        plt.plot(x,y,color='red',label = "đây  không phải là Là hàm số ánh xạ một một")
fa = lambda x: pow(x,3) - x / 2
x = np.arange(-200, 210,1)
test(x,fa)
plt.legend()
plt.show()
fb = lambda x: pow(x,2) + x / 2
x = np.arange(-20,21,0.1)
test(x,fb)
plt.legend()
plt.show()
#baitap6