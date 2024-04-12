#bt1
arr=list(range(50,100,1))
print(arr)
arr.insert(50,100)
print(arr)
for x in arr:
    if x % 2 != 0:
        print(x)
#bt2 
inm=list(range(1500,2701,1))
for i in inm:
    if i % 7==0 and i % 5==0:
       print(i)

#bt3 
onm = list(range(0,21,1))
for k in onm:
    if (k == 3 or k==16):
        continue
    print(k)


#bt4
numbers=[1,2,3,4,5,6,7,8,9]
noen = 0 
noon = 0 
for a in numbers:
    if a %2 !=0:
        noen +=1
    else:
        noon +=1
print("numbers of even number:",noen)
print("numners of odd number:",noon)

#bt5
Tong=0
pooo= list (range(1,100,1)) 
for p in pooo:
    if p<100:
        Tong = Tong + p/(p+1) 
print(Tong)

#bt6 
import numpy as np
w = np.arange(12, 38)
print(w)




