a=int(input("enter a number:"))
b=int(input("enter a number:"))
for i in range(a,b):
  sum=0
  temp=i
  while temp>0:
    dig=temp%10
    sum+=dig**3
    temp//=10
  if i==sum:
    print(i)
