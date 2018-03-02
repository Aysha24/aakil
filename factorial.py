a=int(input("enter a value:"))
factorial=1
if a>0:
	for num in range(1,a+1):
		factorial=factorial*num
	print(factorial)
