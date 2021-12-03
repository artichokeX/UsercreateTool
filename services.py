import json
import api
import uuid

api = api.Api()
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
		api.update_json(data)

	def inputData(self, x):
		if x == "1" or x == 'yes' or x == 'y':
			Services.addUser()
		elif x == "2" or x == 'no' or x == 'n':
			exit('Quitting Program')
		elif x == "3":
			api.list_json()
		elif x == "d":
			api.removeUser()
