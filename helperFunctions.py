import requests



def get_SingleUser(ENDPOINT, user_id):
    return requests.get(ENDPOINT + f"api/users/{user_id}")

def get_listOfUsers(ENDPOINT, page_number):
    return requests.get(ENDPOINT + f"api/users?page={page_number}")

def createUser(ENDPOINT, createdUser):
    return requests.post(ENDPOINT + "api/users", json=createdUser)

def updateUser(ENDPOINT, payload):
    return requests.put(ENDPOINT + "api/users/2", json=payload)

def loginFunc(ENDPOINT):
    return requests.post(ENDPOINT, "api/login")
