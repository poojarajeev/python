s=int(input("enter the no"))
f=1
if s<0:
	print("enter a positive no.")
elif s==0:
	print("factorial value is 0")
else:
	for i in range(1,s):
		f=s*i
	print("factorial of no.",s,"is",f)
	