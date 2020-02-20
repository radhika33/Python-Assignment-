# question 3:-Python Program to Put Even and Odd elements in a List into Two Different Lists

list3=[22,21,15,16,35,91,42,32]
print(list3)
even =[] # empty even list
odd =[]  #empty odd list
for i in list3:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
