a=int(input("enter the vlue to be checked "))
p=int(a/2)
s=0
for i in range(2,p):
	if a%i == 0:
		print("the given no. is prime")
		s=1
if s==0:
	print("the given no. is not prime")
