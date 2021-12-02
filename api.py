import json

def open_json():
  with open('./data/dict.json','r+') as file:
    json.load(file)
    
# Append new data to existing JSON DB
def update_json(new_data, filename='./data/dict.json'):
   with open(filename,'r+') as file:
         # First we load existing data into a dict.
       file_data = json.load(file)
       # Join new_data with file_data inside emp_details
       file_data.append(new_data)
       # Sets file's current position at offset.
       file.seek(0)
       # convert back to json.
       json.dump(file_data, file, indent = 4)

# List JSON data in terminal
def list_json():
  print('test')
  with open('./data/dict.json', 'r') as openfile:
    json_object = json.load(openfile)
    print('test')
    print(json.dumps(json_object, indent=4, sort_keys=True))

def write_json(new_data, filename='./data/dict.json'):
   with open(filename,'w') as file:
       # Join new_data with file_data inside emp_details
       file.write(new_data)