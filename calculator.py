print("select  operation")
print("option 1 -addition")
print("option 2 -subtraction")
print("option 3 -multiplication")
print("option 4 -division")
choice = input("enter choice")
num1=int(input("Enter first no."))
num2=int(input("Enter second no."))
if choice == '1':
	s=num1+num2
elif choice == '2':
	if num1>num2:
		s=num1-num2
	else:
		s=num2-num1
elif choice == '3':
	s=num1*num2
elif choice == '3':
	s=num1/num2
else:
	print("invalid input")
print(s)