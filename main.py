from services import *
from api import *
from os.path import exists


if not (exists('./data/dict.json')):
	open('./data/dict.json', 'w').write('[]')


print(
	'Enter one of the following commands...\n 1 = Add new user \n 2 = Quit the program \n 3 = List users \n d = Delete a user')
createUser = input("Command: ")

# check if dict.json exists
# if it doesn't then create file

def main():
	inputData(createUser)

	while createUser:
		add = input("Would you like to modify your data? (yes/no)")	
		inputData(add)




main()