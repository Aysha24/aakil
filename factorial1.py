a=int(input("enter a value:"))
if a<=20:
	factorial=1
	if a>0:
		for num in range(1,a+1):
			factorial=factorial*num
		print(factorial)
else:
	print("invalid")
