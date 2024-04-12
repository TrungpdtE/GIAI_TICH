#cau4
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

x = sp.symbols('x')
#a
f = abs(x*x*sp.cos(x))
fin = sp.integrate(f,(x,-4, 9))
print('Definitive Integral of f(x) = ',fin.evalf())
x1 = np.arange(-4,9.1,0.1)
f1= lambda x: abs(x**2*sp.cos(x))
y = list(map(f1,x1))
plt.plot(x1, y)
plt.title('cau 4a')
plt.show()
#b
a,x=sp.symbols('a,x')
fxx=abs(sp.exp((-(1/2)*x*x)))
fin = sp.integrate(f,(x,-sp.oo, sp.oo))
print('Definitive Integral of f(x) = ',fin.evalf())
x2 = np.arange(-100,100,1)
f2= lambda x: abs(sp.exp((-(1/2)*x*x)))
y1 = list(map(f2,x2))
plt.plot(x2, y1)
plt.title('cau 4b')
plt.show()
#cau5
import sympy as sp
t= sp.symbols('t')
ft = 160-32*t
fin = sp.integrate(ft ,(t,0, 8))
print('d=',fin.evalf())

#cau6
import sympy as sp
import numpy as np
import math

x = sp.symbols('x')
fx = 1/2*(x**1/2)
dh= sp.diff(fx,x)
fin = sp.integrate(dh,x)
fin12 = sp.integrate(dh,(x, 1, 101))
print('c(100)-c(1) =',fin12.evalf())
#cau7
import sympy as sp
import numpy as np
import math
x,z,y= sp.symbols('x,z,y')
h = (x+1)**(1/2) + 5*x*(1/3)
#a
cao1 = h.subs(t,0)
print("t = 0 thi h=",cao1)
cao2 = h.subs(t,4)
print("t = 4 thi h =",cao2)
cao3 = h.subs(t,8)
print("t = 8 thi h =",cao3)
#b
a= 0
b= 8
z= 1/(b-a)
fin23 = sp.integrate(h,(t, 0, 8))
y = z*fin23
print("average height for 0<=t<=8 is ",y)