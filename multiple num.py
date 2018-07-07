a=int(input())
mul=1
temp=a
while(temp>0):
  b=temp%10
  mul=mul*b
  temp=temp/10
print(mul)
  
