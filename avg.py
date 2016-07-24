num1= float(raw_input("give me a number"))
num2= float(raw_input("give me a number"))
num3= float(raw_input("give me a number"))

def avg(n1, n2, n3):
	s=float(n1+n2+n3)
	a=(s/3)
	return a

print avg(num1, num2, num3)