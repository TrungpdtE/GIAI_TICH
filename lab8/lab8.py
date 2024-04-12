import math
import numpy as np 
import matplotlib.pyplot as plt
#cau 1
#a
f_a_xy= lambda x, y: x*x + y*y**3
print(f_a_xy(1,1))
print(f_a_xy(-1,1))
print(f_a_xy(2,3))
print(f_a_xy(-3,-2))
#b
f_b_xyz= lambda x, y, z:(x-y)/(y**2+z**2)
print(f_b_xyz(3,-1,2))
print(f_b_xyz(1,1/2,1/4))
print(f_b_xyz(0,-1/3,0))
print(f_b_xyz(2,2,100))

#cau 2
#a
import math
import numpy as np 
import matplotlib.pyplot as plt
z_funz= lambda x,y: x*x + y*y
z_funz= lambda x,y: np.cos(x)*np.cos(y)*math.e**(-np.sqrt(x*x+y*y)/4)

x=np.arange(-6,6.1,0.1)
y=x.copy()
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
Z=z_funz(X,Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z,cmap = 'hot',linewidth=0)
ax.set_title('surface plot')
plt.show()



#b
import math
import numpy as np 
import matplotlib.pyplot as plt
z_funb= lambda x,y: x*x + y*y
z_funb= lambda x,y:-((x*y*y)/(x*x+y*y))

x=np.arange(-6,6.1,0.1)
y=x.copy()
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
Z=z_funb(X,Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z,cmap = 'hot',linewidth=0)
ax.set_title('surface plot')
plt.show()
#c
import math
import numpy as np 
import matplotlib.pyplot as plt
z_func= lambda x,y: x*x + y*y
z_func= lambda x,y: (x*y*(x*x-y*y)/(x*x+y*y))

x=np.arange(-6,6.1,0.1)
y=x.copy()
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
Z=z_func(X,Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z,cmap = 'hot',linewidth=0)
ax.set_title('surface plot')
plt.show()


#d
import math
import numpy as np 
import matplotlib.pyplot as plt
z_fund= lambda x,y: x*x + y*y
z_fund= lambda x,y: y*y - y*y*y*y - x*x

x=np.arange(-6,6.1,0.1)
y=x.copy()
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
Z=z_fund(X,Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z,cmap = 'hot',linewidth=0)
ax.set_title('surface plot')
plt.show()
#cau 3
#a
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= 2*x*x - 3*y -4
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#b
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x*x-1)*(y+2)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#c
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x*x-x*y+y*y
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#d
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= 5*x*y - 7*x*x -y*y +3*x - 6*y+2
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#e
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x*y-1)*(x*y-1)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#f
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (2*x-3*y)*(2*x-3*y)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#g
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x*x+y*y)**(1/2)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#h
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x*x*x+(y/2))**(2/3)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#i
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= 1/(x+y)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#j
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x/(x*x+y*y)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#k
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x+y)/(x*y-1)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#l
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (sp.tan(y/x))**(-1)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#m
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (math.e)**(x+y+1)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#n
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (math.e)**(-x)*(sp.sin(x+y))
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#o
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= sp.ln(x+y)
dfx=sp.diff(f_a,x,1)
dfy=sp.diff(f_a,y,1)
print("Find the first-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the first-order partial derivatives of the function f(x, y) with ragard to y=",dfy)

#cau4
#caua
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x+y+x*y
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#b
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= sp.sin(x*y)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#c
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x*x*y +sp.cos(y)+y*sp.sin(x)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#d
import sympy as sp 
x,y = sp.symbols('x,y')
f_a=x*(math.e)**y +y+1
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#e
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= sp.ln(x+y)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#f
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= sp.tan(y/x)**(-1)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#g
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x*x*sp.tan(x*y)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#h
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= y*(math.e**(x*x-y))
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#i
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= x*sp.sin(x*x*y)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#j
import sympy as sp 
x,y = sp.symbols('x,y')
f_a= (x-y)/(x*x+y)
dfx=sp.diff(f_a,x,2)
dfy=sp.diff(f_a,y,2)
print("Find the 2-order partial derivatives of the function f(x, y) with regard to x=",dfx)
print("Find the 2-order partial derivatives of the function f(x, y) with ragard to y=",dfy)
#cau 5
#a
x,y = sp.symbols('x,y')
f=x*sp.sin(y)+y*sp.sin(x)+x*y
dfx= sp.diff(f,x,1)
dfxy=sp.diff(dfx,y)
print(dfxy)
dfyx= sp.diff(sp.diff(f,y),x)
print(dfyx)
#b
x,y = sp.symbols('x,y')
f=x*y*y + x*x*y*y*y + x*x*x*y*y*y*y
dfx= sp.diff(f,x,1)
dfxy=sp.diff(dfx,y)
print(dfxy)
dfyx= sp.diff(sp.diff(f,y),x)
print(dfyx)
#c
x,y = sp.symbols('x,y')
f=sp.ln(x*2+3*y)
dfx= sp.diff(f,x,1)
dfxy=sp.diff(dfx,y)
print(dfxy)
dfyx= sp.diff(sp.diff(f,y),x)
print(dfyx)
#d
x,y = sp.symbols('x,y')
f=math.e**x + x*sp.ln(y)+y * sp.ln(x)
dfx= sp.diff(f,x,1)
dfxy=sp.diff(dfx,y)
print(dfxy)
dfyx= sp.diff(sp.diff(f,y),x)
print(dfyx)

#cau6
#cau6
#a
print("Cau a")
x,y = sp.symbols ('x,y')
f1 = y*y*x*x*x*x*math.e**x +2
d5f = sp.diff(sp.diff(f1,y,3),x,2)
print(d5f)
#b
print("Cau b")
x,y = sp.symbols ('x,y')
f2 = y*y*y*y +y*(sp.sin(x)-x**4)
d5f = sp.diff(sp.diff(f2,y,3),x,2)
print(d5f)
#c
print("Cau c")
x,y = sp.symbols ('x,y')
f3 = x*x*x*x*x + 5*x*y +sp.sin(x) + 7*math.e**x
d5f = sp.diff(sp.diff(f3,y,3),x,2)
print(d5f)
#d
print("Cau d")
x,y = sp.symbols ('x,y')
f4 = math.e**x + x*sp.ln(y) + y*sp.ln(x)
d5f = sp.diff(sp.diff(f4,y,3),x,2)
print(d5f)

#cau7
#a
t=sp.symbols('t')
x=sp.cos(t)
y=sp.sin(t)
w=x*x+y*y
dwt=sp.diff(w,t)
print("derivate of w(t) with regard to t=",dwt)
print("derivate of w(t) with regard at t=pi",dwt.subs(t,math.pi))
print(y.subs(t,3).evalf())
#b
t=sp.symbols('t')
x=sp.cos(t)+sp.sin(t)
y=sp.cos(t)-sp.sin(t)
w=x*x+y*y
dwt=sp.diff(w,t)
print("derivate of w(t) with regard to t=",dwt)
print("derivate of w(t) with regard at t=pi",dwt.subs(t,math.pi))
print(y.subs(t,3).evalf())


#cau9
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x,y = sp.symbols ('x,y')
f = x*x - x*y + y*y/2 +3

dfx = sp.diff(f , x)
dfy = sp.diff(f , y)
x0 =3
y0 =2
z0 = f.subs(x,x0).subs(y,y0) #f(x0,y0)

z = z0 + dfx.subs(x , x0).subs(y,y0)*(x-x0) + dfy.subs(x , x0).subs(y,y0)*(y-y0)
print("z = ",z)
#draw
fxy = lambda x,y:x*x -x*y +y*y/2 +3
f_tangent = lambda x,y :4*x -y -2

x =np.arange(-10,10.1,0.1)
y = x.copy()
X,Y = np.meshgrid(x,y)
Z = fxy(X,Y)
Z_tangent = f_tangent(X,Y)

ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z, cmap = 'jet' , linewidth = 0)
ax.plot_surface(X ,Y,Z_tangent , cmap = 'ocean' ,linewidth = 0 )
plt.show()