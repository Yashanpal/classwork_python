#LIST
l=[10,20,30,40]
l.append(90)
print(l)
#EXTEND
l1=[1,2,3,4]
l2=[10,20,30]
l1.extend(l2)
print(l1)
l2.insert(2,100)
print(l2)

l3=[10,2,548,120]
l3.pop(2)
print(l3)

#print("for taking input from user")
#l=[]
#for a in range(4):
 #   a=input("enter number:")
  #  l.append(a)
   # print(l)

#TUPLE
print()
t1=(1,2,3,5,78)
print (t1)
for x in t1:
    print (x)
print("to convert tuple into list")
l1=list(t1)
print(l1)

#SETS
s1={2,4,89,54}
print(s1)
s2={98,4,65,54,60}
print(s2)
print("set union")
S=s1.union(s2)
print(S)
#print(s1|s2)
print("set intersection")
S=s1.intersection(s2)
print(S)
#print(s1&s2)
print("set difference")
S=s1.difference(s2)
print(S)
S=s2.difference(s1)
print(S)
#print(s1-s2)

#DICTIONARY
d1={
    'name':'Yashan',
    'class':'12',
    'section':'B'
   }

d1.values()
d1['roll no.']='50'
print(d1)

#FUNCTIONS
def greet(name='stranger'):
    print("good bye " +name)
greet("Yashan")
greet()