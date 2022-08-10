#1
l1=['m','n']
l2=[]
for i in range(3):
    a=l1[0]+str(i+0)
    l2.append(a)
for i in range(3):
    a=l1[1]+str(i+1)
    l2.append(a)
print(l2)
print()

#2
l=[[4,5,3],[6,3,2],[6,9,1]]
l1=[]
sum=0
for i in l:
    for j in i:
        sum+=j
    l1.append([sum])
print(l1)
print()

#3
l=[1,3,6,8,7,5,56,8,3,6]
print("List with duplicate elements :",l)
l1=set(l)
print("List without duplicate elements :",l1)
print()

#4
n1=[]
for x in range (1200,3000):
    if(x%4==0) and (x%8==0) and ((x%6)!=0):
        n1.append(x)
print(n1)