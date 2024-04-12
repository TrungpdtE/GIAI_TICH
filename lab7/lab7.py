import math
import sympy as sp
import numpy as np 
#cau1
#a
f_1a = lambda n: 4*n + 1
n1a_array = np.arange(1,11)
x_1a = list(map(f_1a, n1a_array) )
print(x_1a)
#b
f_1b = lambda n: 3**n
b_array = np.arange(1,11)
x_1b = list(map(f_1b, b_array) )
print(x_1b)
#c
f_1c = lambda n: n**3
c_array = np.arange(1,11)
x_1c = list(map(f_1c, c_array) )
print(x_1c)
#d
def fibonacci(num):
    series = 0
    num1 = 0
    num2 = 1
    for i in range(num):
        print(series, end=' ')
        num1 = num2
        num2 = series
        series = num1 + num2
fibonacci(10)
#cau2
#a
d = 15
a1 = 5
f_n = lambda n: a1 + (n - 1)*d
a55 = f_n(55)
for i in np.arange(1, 101):
    if f_n(i) == 230:
        print("Tai vi tri n = ", i,"thi f(n) = 230")
        break
    
    if f_n(i) > 230: break
#b
r = 1/2
a1 = 120
f_n = lambda n: a1*r**(n-1)
a10 = f_n(10)
for i in np.arange(1, 101):
    if f_n(i) == 15/32:
        print("Tai vi tri n = ", i,"thi f(n) = 15/32")
        break
    
    if f_n(i) > 15/32: break
#cau3
#a
x = sp.symbols('x')
f = sp.cos(x)
taylor_poly = f.series(x,math.pi/3, 6)
print('Taylor series of f(x) at pi/3: ', taylor_poly)
#b
x = sp.symbols('x')
f = sp.log(x)
taylor_poly = f.series(x,2, 10)
print('Taylor series of f(x) at 2: ', taylor_poly)
#c
x = sp.symbols('x')
f = sp.exp(x)
taylor_poly = f.series(x,3, 10)
print('Taylor series of f(x) at 3: ', taylor_poly)
#cau4
#a
x = sp.symbols('x')
f = sp.cos(x)
maclaurin_poly = f.series(x,0, 6)
print('Maclaurin series of f(x) : ', maclaurin_poly)
#b
x = sp.symbols('x')
f = sp.exp(x)
maclaurin_poly = f.series(x,0, 12)
print('Maclaurin series of f(x) : ', maclaurin_poly)
#c
x = sp.symbols('x')
f = 1/(1-x)
maclaurin_poly = f.series(x,0, 12)
print('Maclaurin series of f(x) : ', maclaurin_poly)
#d
x = sp.symbols('x')
f = (sp.tan(x))**-1
maclaurin_poly = f.series(x,0, 12)
print('Maclaurin series of f(x) : ', maclaurin_poly)
#cau6
#a
n = sp.symbols('n')
a_n = 1 - 0.2**n 
print("Limit of the sequence a_n =  ",sp.limit_seq(a_n, n)) 
#b
n = sp.symbols('n')
a_n = (n**3)/((n**3)+1) 
print("Limit of the sequence a_n =  ",sp.limit_seq(a_n, n)) 
#c
n = sp.symbols('n')
a_n = (3+5*n*n)/(n+(n*n)) 
print("Limit of the sequence a_n =  ",sp.limit_seq(a_n, n)) 
#6d
n = sp.symbols('n')
a_n = n**3/(n+1) 
print("Limit of the sequence a_n =  ",sp.limit_seq(a_n, n)) 
#6e
a_n = pow(math.e, 1/n)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6f
a_n = sp.sqrt((n+1)/(9*n+1))
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6g
a_n = (pow(-1, n+1)*n)/(n+n**1/2)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6h
a_n = sp.tan((2*math.pi*n)/(1+8*n))
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6i
a_n = sp.factorial(2*n-1)/sp.factorial(2*n+1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6j
a_n = sp.ln(2*n**2+1) - sp.ln(n**2 + 1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))

#cau7
#a
a7 = 0.8
firstFiveTerms7 = [a7]
a1_n = a7
for x in range(0, 4):
    a7_next = 1- 0,2**n
    firstFiveTerms7.append(a7_next)
    a7_n = a7_next
print(firstFiveTerms7)
#b
b7 = 1
firstFiveTerms2 = [b7]
b7_n = b7
for x in range(0, 4):
    b7_next = 2*n/(n**2+1)
    firstFiveTerms2.append(b7_next)
    b7_n = a2_next
print(firstFiveTerms2)
#c
c7 = 1
firstFiveTerms3 = [c7]
c7_n = c7
for x in range(0, 4):
    c7_next = pow(-1, n-1)/5**n
    firstFiveTerms3.append(c7_next)
    c7_n = c7_next
print(firstFiveTerms3)
#d
d7 = 1
firstFiveTerms4 = [d7]
a4_n = d7
for x in range(0, 4):
    d7_next = 1/sp.factorial(n+1)
    firstFiveTerms4.append(d7_next)
    d7_n = d7_next
print(firstFiveTerms4)
#e
e1 = 1
firstFiveTerms = [e1]
e_n = e1
for i in range(0, 4):
    e_next = 5*a_n - 3
    firstFiveTerms.append(e_next)
    e_n = e_next 
print(firstFiveTerms)
#f
f1 = 2
firstFiveTerms = [f1]
f_n = f1
for i in range(0, 4):
    f_next = a_n/(a_n + 1)
    firstFiveTerms.append(f_next)
    f_n = f_next 
print(firstFiveTerms)
#cau9
#a
n = sp.symbols('n')
series = sp.Sum(4**n, (n,1, sp.oo))
converged = series.is_convergent()
if converged:
    print("cau a hoi tu")
else:
    print("cau a khong hoi tu")
#b
n = sp.symbols('n')
series = sp.Sum(5/2**n, (n,1, sp.oo))
converged = series.is_convergent()
if converged:
    print("cau b hoi tu")
else:
    print("cau b khong hoi tu")
#10
def findFibo(i):
    if i < 1: return -1
    if i == 1: return 0
    if i == 2: return 1
    x1 = 0
    x2 = 1
    for k in range(3, i + 1):
        x_next = x2 +x1
        x1 = x2
        x2 = x_next 

        return x_next
print( findFibo(11) )

