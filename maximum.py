list=[]
num=int(input("enter many numbers:"))
for n in range(num):
  numbers=int(input("enter a number:"))
  list.append(numbers)
print(max(list))
