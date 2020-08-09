def add(num1 , num2):
	return num1 + num2 
	
def sub(num1 , num2):
	return num1 - num2
	
def mul(num1 , num2):
	return num1 * num2
	
def div(num1 , num2):
	return num1 / num2
	
print(" Chose an Option ! \n 1 = Addition \n 2 = Subtraction \n 3 = Multiplication \n 4 = Division")
print(" ")
str = int(input("Enter Your Choice "))
print(" ")
num1 = int(input("Enter Your First Number :- "))
print(" ")
num2 = int(input("Enter Your Second Number :- "))
print(" ")
if (str == 1):
	print("Result Is ", add(num1,num2))
	
elif (str ==2):
	print("Result Is ",sub(num1,num2))
	
elif (str == 3):
	print("Result Is ",mul(num1,num2))
	
elif (str == 4):
	print("Result Is ",div(num1,num2))
	
else:
	print("You Choosed Wrong Option")
	