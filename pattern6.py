n=4
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for j in range(2*n-1):
    print("*",end="")
  print()
n=3
for i in range(n,0,-1):
  for j in range(n-i):
    print("",end="")
  for j in range(2*i-1):
    print("*",end="")
  print()
