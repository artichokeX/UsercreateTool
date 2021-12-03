import json
import api
import uuid

class Services:
	def addUser():
		name = input("enter your name: ")
		age = input("enter your age: ")
		phone =	input("enter your phone number: ")
		email =	input("enter your phone email: ")

		data = {
			"person": {
				"uuid": str(uuid.uuid4()),
				"personal_info": {
					"name": name,
					"age": age
				},
				"contact_info": {
					"phone": phone,
					"email": email
				}
			}
		}
		update_json(data)

	def inputData(x):
	    if x == "1" or x == 'yes' or x == 'y':
		addUser()
	    elif x == "2" or x == 'no' or x == 'n':
		exit('Quitting Program')
	    elif x == "3":
		list_json()
	    elif x == "d":
        	removeUser()
