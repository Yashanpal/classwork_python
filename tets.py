#2
S=442
E=662
for x in range (S,E+1):
    if(x%2==0):
        print(x)

#1
str = "Yashan"
substr = []
for i in range(len(str)):
    for j in range(i+1, len(str)+1):
        substr.append(str[i:j])
substr = list(set(substr))
print(substr)

#4
def Multiply_matrix(A,B):
  result=[[0,0,0],[0,0,0],[0,0,0]]
  for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
  for r in result:
    print(r)

x=[[1,2,3],[9,6,7],[32,45,7]]
y=[[56,5,8],[8,9,7],[54,14,25]]

print("Result=")
Multiply_matrix(x,y)

#6
rows = int(input(" Enter the Total Number of Rows  : "))
columns = int(input(" Enter the Total Number of Columns  : "))

print("Hollow Rectangle Star Pattern") 
for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()