import math
import sympy as sp 
#cau1
#a
x=sp.symbols('x')
f=4-x*x
dfa=sp.diff(f,x)
print("1a-dao ham 1 fx =",dfa)
dfa2=sp.diff(f,x,2)
print("1a-dao ham 2 fx=",dfa2)
#b
x=sp.symbols('x')
f=(x-1)*(x-1)+1
dfb=sp.diff(f,x)
print("1a-dao ham 1 fx =",dfb)
dfb2=sp.diff(f,x,2)
print("1a-dao ham 2 fx=",dfb2)
#c
t=sp.symbols('t')
f=1/(t*t)
dfc=sp.diff(f,t)
print("1a-dao ham 1 gx =",dfc)
dfc2=sp.diff(f,t,2)
print("1a-dao ham 2 gx=",dfc2)
#d
z=sp.symbols('z')
f=(1-z)/(2*z)
dfd=sp.diff(f,z)
print("1a-dao ham 1 kx =",dfd)
dfd2=sp.diff(f,z,2)
print("1a-dao ham 2 kx=",dfd2)
#e
z=sp.symbols('z')
f=sp.sqrt(3*z)
dfe=sp.diff(f,z)
print("1a-dao ham 1 kx =",dfe)
dfe2=sp.diff(f,z,2)
print("1a-dao ham 2 kx=",dfe2)
#f
z=sp.symbols('z')
f=sp.sqrt(2*z+1)
dff=sp.diff(f,z)
print("1a-dao ham 1 kx =",dff)
dff2=sp.diff(f,z,2)
print("1a-dao ham 2 kx=",dff2)


#cau2
#a
x=sp.symbols('x')
f2a=x*x+1
d2fa=sp.diff(f2a,x)
slope=d2fa.subs(x,2)
y1=slope*(x-2)+5
sp.plot(f2a,y1,(x,-5,5))
#b
x=sp.symbols('x')
f2b=x-2*x*x
d2fb=sp.diff(f2b,x)
slope=d2fb.subs(x,2)
y2=slope*(x-1)+(-1)
sp.plot(f2a,y2,(x,-5,5))
#d
x=sp.symbols('x')
f2d=8/(x*x)
d2fd=sp.diff(f2d,x)
slope=d2fd.subs(x,2)
y4=slope*(x-2)+2
sp.plot(f2d,y4,(x,-5,5))
#e
x=sp.symbols('x')
f2e=sp.sqrt(x)
d2fe=sp.diff(f2e,x)
slope=d2fe.subs(x,2)
y5=slope*(x-2)+5
sp.plot(f2e,y5,(x,-5,5))
#f
t=sp.symbols('t')
f2f=t*t*t + 3*t
d2ff=sp.diff(f2f,t)
slope=d2ff.subs(t,2)
y6=slope*(t-1)+4
sp.plot(f2f,y6,(t,-5,5))
#h
z=sp.symbols('z')
f2z=1+sp.sqrt(4-z)
d2fz=sp.diff(f2z,z)
slope=d2fz.subs(z,2)
y8=slope*(z-3)+2
sp.plot(f2z,y8,(z,-5,5))

#cau8
#a
x=sp.symbols('x')
fxx=x**3 - 3*x +1
dfx=sp.diff(fxx,x)
slope=dfx.diff(x,3)
y8a=slope*(x-3)+fxx.subs(x,3)
sp.plot(fxx,y8a,(x,-5,5))
#14
#a
t=sp.symbols('t')
f14=10*10*10*10*10*10+10*10*10*10*t-10*10*10*t*t
df14=sp.diff(f14,t)
p=df14.subs(t,0)
print("t=0 thi ",p)
#b
t=sp.symbols('t')
f14=10**6+10*10*10*10*t-(10**3)*t*t
df14=sp.diff(f14,t)
k=df14.subs(t,5)
print("t=5 thi ",k)
#c
t=sp.symbols('t')
f14=10**6+10*10*10*10*t-(10**3)*t*t
df14=sp.diff(f14,t)
l=df14.subs(t,10)
print("t=10 thi ",l)
#15
import math
import sympy as sp
t = sp.symbols('t')
s = 24*t -0.8*t*t
v = sp.diff(s,t)  
a = sp.diff(v,t)
#a
print("Velocity at t " ,v)
print("Acceleration at t " ,a)
#b
cao = sp.solve(v)
print("The highest point is at ",cao)
#c
okk = s.subs(t,cao[0])
print("The rock go: ",okk)

#cau16
import sympy as sp
def newton(f,x,x0,tol,n):
    dfk=sp.diff(f,x)

    for i in range(n):
        if abs(f.subs(x,x0))<tol:
            return x0

        x_new=x0 - f.subs(x,x0) / dfk.subs(x,x0)
        if abs(x_new - x0 ) < tol:
            return x_new

        x0=x_new
        return x0


x=sp.symbols('x')
f=x*x - 2*x +1
print(newton(f,x,0,1e-8,1000))

#
import sympy as sp
def newton(f,x,x0,tol,n):
    dfk=sp.diff(f,x)

    for i in range(n):
        if abs(f.subs(x,x0))<tol:
            return x0

        x_new=x0 - f.subs(x,x0) / dfk.subs(x,x0)
        if abs(x_new - x0 ) < tol:
            return x_new

        x0=x_new
        return x0


x=sp.symbols('x')
f=x*x*x -4
print(newton(f,x,0,2,3))