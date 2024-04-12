import sympy as sp 
#cau1
#a
x = sp.symbols('x')
f1 = x*x*x+2*x + 3
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,2))
print('Definite integral of f(x) from 1 to 2')
print('Definite in tegral of f(x) from 1 to 2 =',fy.evalf())
#b
x = sp.symbols('x')
f1 = 1/(x*x*x)+1/(x*x)+x*(x**(1/2))
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,4))
print('Definite integral of f(x) from 1 to 4')
print('Definite in tegral of f(x) from 1 to 4 =',fy.evalf())
#c
x = sp.symbols('x')
f1 = (x*x*x+x*(x**(1/2))*x+x)/(x*x)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,4))
print('Definite integral of f(x) from 1 to 4')
print('Definite in tegral of f(x) from 1 to 4 =',fy.evalf())
#d
x = sp.symbols('x')
f1 = (2/x + x*x*x)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,2))
print('Definite integral of f(x) from 1 to 2')
print('Definite in tegral of f(x) from 1 to 2=',fy.evalf())
#e
x = sp.symbols('x')
f1 = x*x*(1/(1/x+2*x))
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,2))
print('Definite integral of f(x) from 1 to 2')
print('Definite in tegral of f(x) from 1 to 2=',fy.evalf())
#f
x = sp.symbols('x')
f1 = (x**(1/2)-1)*(x+x**(1/2)+1)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,0,1))
print('Definite integral of f(x) from 0 to 1')
print('Definite in tegral of f(x) from 0 to 1 =',fy.evalf())
#g
x = sp.symbols('x')
f1 = 1-2/(sp.sin(x)*sp.sin(x))
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,math.pi/4,math.pi/2))
print('Definite integral of f(x) from pi/4 to pi/2')
print('Definite in tegral of f(x) from pi/4 to pi/2 =',fy.evalf())
#h
x = sp.symbols('x')
f1 = 1/(sp.sin(x)*sp.sin(x)*sp.cos(x)*sp.cos(x))
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,math.pi/6,math.pi/4))
print('Definite integral of f(x) from pi/6 to pi/4')
print('Definite in tegral of f(x) from pi/6 to pi/4 =',fy.evalf())
#k
x = sp.symbols('x')
f1 = 2**x +2/x
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,2))
print('Definite integral of f(x) from 1 to 2')
print('Definite in tegral of f(x) from 1 to 2 =',fy.evalf())
#l
x = sp.symbols('x')
f1 = x*x*(x-1)*(x-1)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,0,1))
print('Definite integral of f(x) from 0 to 1')
print('Definite in tegral of f(x) from 0 to 1 =',fy.evalf())
#m
x = sp.symbols('x')
f1 = 1/(x*(x+1))
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,1,2))
print('Definite integral of f(x) from 1 to 2')
print('Definite in tegral of f(x) from 1 to 2 =',fy.evalf())
#n
x = sp.symbols('x')
f1 = abs(1-x)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,0,2))
print('Definite integral of f(x) from 0 to 2')
print('Definite in tegral of f(x) from 0 to 2 =',fy.evalf())
#o
x = sp.symbols('x')
f1 = abs(2*x-x**2)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,0,3))
print('Definite integral of f(x) from 0 to 3')
print('Definite in tegral of f(x) from 0 to 3 =',fy.evalf())
#p
x = sp.symbols('x')
f1 = (x*x-3*x+2)**(1/2)
fi = sp.integrate(f1,x)
print('Antiderivate of f(x)=',fi)
fy=sp.integrate(f1,(x,2,4))
print('Definite integral of f(x) from 2 to 4')
print('Definite in tegral of f(x) from 2 to 4 =',fy.evalf())

#cau2
import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')
f = x**3 - 3*(sp.sin(x))*(sp.sin(x))
fin = sp.integrate(f,(x,0,sp.pi/2))
print('Definite integral of f(x) from 0 to pi/2 = ', fin.evalf())

x = sp.symbols('x')
f = sp.sin(x**2)**2
fin = sp.integrate(f,(x,0,1))
print('Definite integral of f(x) from 0 to 21= ', fin.evalf())

x = sp.symbols('x')
f = sp.sqrt(1+x**2+1+(x+1)**2)
fin = sp.integrate(f,(x,0,3))
print('Definite integral of f(x) from 0 to 3 = ', fin.evalf())

x,y  = sp.symbols('x,y')
f = (x**2)*y
fin = sp.integrate(f,(y,1,3),(x,0,2))
print('Definite integral of f(x) from 0 to 2 va 0 den 3= ', fin.evalf())


#cau3
import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')
f = x*x - 1
fin = sp.integrate(f, (x, 0, math.pow(3,1/2)))
a_avg = (1/(math.pow(3,1/2) - 0)) * fin.evalf()
print("average a =", a_avg.evalf())

x = sp.symbols('x')
f = -(x*x)/2
fin = sp.integrate(f, (x, 0,3))
a_avg = (1/(3 - 0)) * fin.evalf()
print("average a =", a_avg.evalf())

x = sp.symbols('x')
f = -3*(x*x) -1
fin = sp.integrate(f, (x, 0,1))
a_avg = (1/(1 - 0)) * fin.evalf()
print("average a =", a_avg.evalf())

x = sp.symbols('x')
f = (x*x) - x
fin = sp.integrate(f, (x, -2,1))
a_avg = (1/(1 + 2)) * fin.evalf()
print("average a =", a_avg.evalf())