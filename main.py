from os.path import exists
import os
import services
services = services.Services()

def main():
	if not (exists('./data/dict.json')):
		os.mkdir("data")
	open('./data/dict.json', 'w').write('[]')

	print(
	'Enter one of the following commands...\n 1 = Add new user \n 2 = Quit the program \n 3 = List users \n d = Delete a user')

	createUser = input("Command: ")
	services.inputData(createUser)

	while createUser:
		add = input("Would you like to modify your data? (yes/no)")	
		services.inputData(add)



if __name__ == "__main__":
	main()
