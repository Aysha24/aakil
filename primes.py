x=int(input("enter a number:"))
y=int(input("enter a number:"))
d=0
for i in range(x,y+1):
  if i>1:
    for j in range(2,i):
      if(i%j)==0:
        break
      else:
        d+=1
print(d)
