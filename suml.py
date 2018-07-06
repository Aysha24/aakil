r=int(input(" "))
list=[]
sum=0
for i in range(1,r+1):
  a=int(input(" "))
  list.append(a)
for i in list:
  sum=sum+i
  i=i+1
print(sum)
