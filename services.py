import json
from api import *
from services import *
import uuid

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

def removeUser():
    uuid = input('enter a uuid to remove: ')
    users = json.load(open('./data/dict.json'))

    # loop through data and remove user
    for i in range(len(users)):
        if users[i]['person']['uuid'] == uuid:
            users.pop(i)
            break

    # update json with new data.
    open('./data/dict.json', 'w').write(
        json.dumps(users, sort_keys=True, indent=4))

def inputData(x):
    if x == "1" or x == 'yes' or x == 'y':
        addUser()
    elif x == "2" or x == 'no' or x == 'n':
        exit('Quitting Program')
    elif x == "3":
        list_json()
    elif x == "d":
        removeUser()