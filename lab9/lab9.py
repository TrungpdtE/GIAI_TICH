import math
import sympy as sp 
import numpy as np 
#cau1
#a
x=sp.symbols('x')
f=3*(x**4)-16*(x**3)+18*(x**2)-9
da=sp.diff(f,x)
ct=sp.solve(da,x)
print('critical values a:',ct)
#b
x=sp.symbols('x')
f=(x**2)/(-3) +(x**2) +3*x+4
dc=sp.diff(f,x)
ct=sp.solve(dc,x)
print('critical values c:',ct)
#c
x=sp.symbols('x')
f=(x+2)/(2*(x**2))
db=sp.diff(f,x)
ct=sp.solve(db,x)
print('critical values b:',ct)
#d
x=sp.symbols('x')
f=(5*(x**2)+5)/x
dc=sp.diff(f,x)
ct=sp.solve(dc,x)
print('critical values d:',ct)
#cau2
#a
import sympy as sp
x = sp.symbols('x')
f=4*(x**4)-16*(x**3)+18*(x**2)-9
df=sp.diff(f,x)
cvals=sp.solve(df,x)
df2=sp.diff(f,x,2)
for v in cvals:
    z=[df2.subs(x,v)]
    if z[0]>0:
        print('local min 2a',v)
    if z[0]<0:
        print('local max 2a:',v)
    if(z[0]==0):
        print('khong the xac dinh 2a')
#b
import sympy as sp
x = sp.symbols('x')
f=(x+2)/(2*(x**2))
df=sp.diff(f,x)
cvals=sp.solve(df,x)
df2=sp.diff(f,x,2)
for v in cvals:
    z=[df2.subs(x,v)]
    if z[0]>0:
        print('local min 2b',v)
    if z[0]<0:
        print('local max 2b:',v)
    if(z[0]==0):
        print('khong the xac dinh 2b')
#c
import sympy as sp
x = sp.symbols('x')
f=(x**2)/(-3)+x**2+3*x+4
df=sp.diff(f,x)
cvals=sp.solve(df,x)
df2=sp.diff(f,x,2)
for v in cvals:
    z=[df2.subs(x,v)]
    if z[0]>0:
        print('local min 2c',v)
    if z[0]<0:
        print('local max 2c:',v)
    if(z[0]==0):
        print('khong the xac dinh 2c')
#d
import sympy as sp
x = sp.symbols('x')
f=(5*(x**2)+5)/x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
df2=sp.diff(f,x,2)
for v in cvals:
    z=[df2.subs(x,v)]
    if z[0]>0:
        print('local min 2d',v)
    if z[0]<0:
        print('local max 2d:',v)
    if(z[0]==0):
        print('khong the xac dinh 2d')
#cau3
#a
import sympy as sp 
x=sp.symbols('x')
f=x**3 -27*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
print('critical values 3a:',cvals)

for x_a in cvals:
    if x_a < 0 or x_a >5: cvals.remove(x_a)
cvals.extend([0,5])

yvals=[f.subs(x,v) for v in cvals]
print('The absoluate maximum 3a is ', max(yvals))
print('The absoluate minimum 3a is ', min(yvals))
#b
import sympy as sp 
x=sp.symbols('x')
f=(3/2)*(x**4)-4*(x**3)+4
df=sp.diff(f,x)
cvals=sp.solve(df,x)
print('critical values 3b:',cvals)

for x_a in cvals:
    if x_a < 0 or x_a >3: cvals.remove(x_a)
cvals.extend([0,3])

yvals=[f.subs(x,v) for v in cvals]
print('The absoluate maximum 3b is ', max(yvals))
print('The absoluate minimum 3b is ', min(yvals))
#c

import sympy as sp 
x=sp.symbols('x')
f=(1/2)*(x**4)-4*(x**2)+5
df=sp.diff(f,x)
cvals=sp.solve(df,x)
print('critical values 3c:',cvals)

for x_a in cvals:
    if x_a < 1 or x_a >3: cvals.remove(x_a)
cvals.extend([1,3])

yvals=[f.subs(x,v) for v in cvals]
print('The absoluate maximum 3c is ', max(yvals))
print('The absoluate minimum 3c is ', min(yvals))
#d

import sympy as sp 
x=sp.symbols('x')
f=(5/2)*(x**4)-(20/3)*(x**3)+6
df=sp.diff(f,x)
cvals=sp.solve(df,x)
print('critical values 3d:',cvals)

for x_a in cvals:
    if x_a < -1 or x_a >3: cvals.remove(x_a)
cvals.extend([-1,3])

yvals=[f.subs(x,v) for v in cvals]
print('The absoluate maximum 3d is ', max(yvals))
print('The absoluate minimum 3d is ', min(yvals))

#cau4
#a
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**2 -2*x -5
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>2: cvals.remove(x_v)
cvals.extend([0,2])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,2.1,0.1)
f1=lambda x: x**2 -2*x -5
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4a')
plt.show()
#d
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=math.e**(x**2)+3*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-1 or x_v>1: cvals.remove(x_v)
cvals.extend([-1,1])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-1,1.1,0.1)
f1=lambda x: math.e**(x**2)+3*x
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4d')
plt.show() 
#e
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**3-3*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-1 or x_v>1: cvals.remove(x_v)
cvals.extend([-3,0])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-3,0.1,0.1)
f1=lambda x: x**3-3*x
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'blue')
plt.title('cau 4e')
plt.show() 
#f
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**3-3*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v3: cvals.remove(x_v)
cvals.extend([-1,1])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,3.1,0.1)
f1=lambda x: x**3-3*x
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4f')
plt.show() 
#g
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=sp.sin(x)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>math.pi: cvals.remove(x_v)
cvals.extend([-1,1])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,math.pi+0.1,0.1)
f1=lambda x: sp.sin(x)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4g')
plt.show() 
#h
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=sp.sin(2*x)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>2: cvals.remove(x_v)
cvals.extend([0,2])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,2.1,0.1)
f1=lambda x: sp.sin(2*x)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4h')
plt.show() 
#i
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=sp.cos(2*x)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <math.pi/2 or x_v>math.pi*(3/2): cvals.remove(x_v)
cvals.extend([math.pi/2,math.pi*(3/2)])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(math.pi/2,math.pi*(3/2)+0.1,0.1)
f1=lambda x: sp.cos(2*x)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4i')
plt.show() 
#j
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=sp.tan(x)**2
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-math.pi/4 or x_v>math.pi/4: cvals.remove(x_v)
cvals.extend([-math.pi/4,math.pi/4])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-math.pi/4,math.pi/4+0.1,0.1)
f1=lambda x: sp.tan(x)**2
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4j')
plt.show() 
#k
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=(math.e**x)*sp.sin(x)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>math.pi: cvals.remove(x_v)
cvals.extend([0,math.pi])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,math.pi+0.1,0.1)
f1=lambda x: (math.e**x)*sp.sin(x)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4k')
plt.show() 
#l
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**4 - 3*(x**2)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-4 or x_v>0: cvals.remove(x_v)
cvals.extend([-4,0])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-4,0.1,0.1)
f1=lambda x: x**4 - 3*(x**2)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4l')
plt.show() 
#m
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**4 - 3*(x**2)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>4: cvals.remove(x_v)
cvals.extend([0,4])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,4.1,0.1)
f1=lambda x: x**4 - 3*(x**2)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'blue')
plt.title('cau 4m')
plt.show() 
#n
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**5 - 5*(x**3)
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-4 or x_v>0: cvals.remove(x_v)
cvals.extend([-4,0])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-4,0.1,0.1)
f1=lambda x: x**5 - 5*(x**3)
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4n')
plt.show() 

#p
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**3 - 9*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <-1 or x_v>1: cvals.remove(x_v)
cvals.extend([-1,1])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(-1,1.1,0.1)
f1=lambda x: x**3 - 9*x
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4p')
plt.show() 
#q
import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt 
f=x**3-9*x
df=sp.diff(f,x)
cvals=sp.solve(df,x)
for x_v in cvals:
    if x_v <0 or x_v>3: cvals.remove(x_v)
cvals.extend([0,3])

yvals=[f.subs(x,v) for v in cvals]
x1=np.arange(0,3.1,0.1)
f1=lambda x: x**3-9*x
y=list(map(f1,x1))
plt.plot(x1,y)
plt.plot(cvals,yvals,'red')
plt.title('cau 4q')
plt.show() 

#cau5
import numpy as np
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
f=lambda x:x**2
mytable=PrettyTable()
mytable.field_names=['i','a','b']
def goldensearch(a,b,c):
    d=b-a
    i=1
    while b-a>=c:
        d=0.618*d
        x1=b-d
        x2=a+d
        if f(x1)<=f(x2):
            b=x2
        else:
            a=x1
        mytable.add_row([i,a,b])
        i=i+1
        print(mytable)
        print("cau 5 Min=",(f(a)+f(b))/2)
goldensearch(-2,1,0.3)
#cau6
import numpy as np
import math
import matplotlib.pyplot as plt
fx=lambda x: x**2
def fibonanci(a,b,c):
    fx1=2
    fx2=3
    while b-a>=c:
        d=b-a
        x1=b-d*(fx1/fx2)
        x2=a+d*(fx1/fx2)
        if fx(x1) <= fx(x2):
            b=x2
        else:
            a=x1
        temp=fx1+fx2
        fx1=fx2
        fx2=temp
    print("cau 6 min=",(fx(a)+fx(b))/2)
fibonanci(-2,1,0.3)
