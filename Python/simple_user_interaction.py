#Simple User Interaction !

game_list = [0,1,2]
def display_game(game_list):
	print(" Here Is The Current List ")
	print(game_list)
			
def position_check():
	choice = 'wrong'
	while choice not in ['0','1','2']:
		choice=input("Enter Position You Want To Replace (0,1,2) :- ")
		if choice not in ['0','1','2']:
				print("Sorry Invalid Choice !")
				
	return int(choice)
	
def replacement_choice(game_list,position):
	user_replacement = input("Enter A Stiring You Want To Replace :- ")
	
	game_list[position] = user_replacement
	
	return game_list

def gameon_choice():
	choice = 'wrong'
	while choice not in ['Y' , 'N']:
		choice=input("Do You Still want To Continue Game ? (Y or N) ")
		if choice not in [ 'Y' , 'N' ]:
			print("Sorry Invalid Choice !")
		
	if choice == "Y":
						return True
						
	else:
						return False
						
	return int(choice)
	
#Real algo
game_on = True
game_list = [0,1,2]
while game_on == True:
		display_game(game_list)
		pos = position_check()
		game_list = replacement_choice(game_list,pos)
		display_game(game_list)	
		game_on = gameon_choice()
				