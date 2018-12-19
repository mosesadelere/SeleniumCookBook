import json

filename = 'myjson.json'
myList = [2,3,6,3,7,8,23]
with open(filename,'w') as fjson:
    json.dump(myList,fjson)


with open(filename) as f:
    myjson = json.load(f)
print(myjson)

def get_newUser():
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as fobject:
        json.dump(username,fobject)
    return username

def get_username():
    filename = 'username.json'
    try:
        with open(filename) as fName:
            username = json.load(fName)
    except FileNotFoundError:
       return None
    else:
        return username

def greetUsers():
    username = get_username()
    if username:
        print('Welcome back ' + username)
    else:
        username = get_newUser()
        print('Next time you come, we will remember you' + username)
    

greetUsers()