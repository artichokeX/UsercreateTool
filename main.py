import json
from services import *

createUser = input("Press 1 to Add a User, 2 to Remove a User, or 3 to view list of Users: ")

while createUser == "1":
		name = input("What is your name: ")
		age = input("What is your age: ")

		data = {
			"name": name,
			"age": age
		}

		write_json(data)

		add = input("Would you like to modify your data? Press 1 to add, 3 to list users, or 2 to close: ")	
		
		if add == "2":
			break

		if add == '3':
			break