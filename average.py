n=int(input("enter the range:"))
l=[]
for i in range(0,n):
  a=int(input("enter the numbers:"))
  l.append(a)
print l
b=sum(l)/len(l)
print(b)
