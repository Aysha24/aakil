i=int(input("enter a number:"))
r=int(input("enter a number:"))
d=0
for m in range(i,r):
  if m>1:
    for k in range(2,m):
      if(m%k)==0:
        break
      else:
        d+=1
print(d)
