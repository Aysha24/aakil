x=int(input("enter a number:"))
y=int(input("enter a number:"))
for i in range(x,y):
  if i>1:
    for j in range(2,i):
      if(i%j)==0:
        break
      else:
        print(i)
        break
