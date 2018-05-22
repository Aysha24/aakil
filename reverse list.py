n=int(input("enter the number of elements:"))
l=[]
for i in range (1,n+1):
	a=int(input("enter the elements:"))
	l.append(a)
	l = l[::-1]
print(l)
