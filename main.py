import json
from services import *

createUser = input("Press 1 to Add a User, 2 close, or 3 to view list of Users: ")

def input1():
	name = input("What is your name: ")
	age = input("What is your age: ")	
	data = {
		"name": name,
		"age": age
	}
	write_json(data)

def input2():
	exit('quitting')

def input3():
	list_json()

def main():
	while createUser == "1":
		input1()
		break
	
	while createUser == "2":
		input2()
		break

	while createUser == "3":
		input3()
		break
	
	add = input("Would you like to modify your data? Press 1 to add, 3 to list users, or 2 to close: ")	
	while add == '2':
		input2()
	while add == '3':
		input3()
		break
	
main()