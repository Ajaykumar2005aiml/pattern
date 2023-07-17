R=int(input())
for i in range(1,R+1):
    for j in range(i,R):
        print(" ",end="")
    for j in range(1,i+1):
      if j!=R:
        if (j==1 or i==R or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
      else:
        print("*",end="")
    print()
