#Validating User Input !

##Vars##
choice = 'Wrong'
a_range= range(0,101)
within_range = False

##Condition to Run Loop untill Get Desired Choice !
while choice.isdigit() == False or within_range == False :
	choice=input("Enter You Number (0,100) :- ")

##Digit Check##	
	if choice.isdigit() == False:
		print(" Sorry This is Not a Digit")

#Range Check##
	if choice.isdigit() == True:
			if int(choice) in a_range:
				within_range = True
			
			else:
				within_range = False
				print("Sorry You Are out of range")
		
print(choice)
