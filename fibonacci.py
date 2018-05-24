b=int(input("enter the number:"))
m1=0
m2=1
for i in range(0,b):
  sum=m1+m2
  print (sum)
  m1=m2
  m2=sum
