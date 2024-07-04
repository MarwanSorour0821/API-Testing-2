import requests
from helperFunctions import get_SingleUser, get_listOfUsers, createUser, updateUser, loginFunc
from datetime import date, datetime


ENDPOINT = "https://reqres.in/"

def test_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_singleUser():
    response = get_SingleUser(ENDPOINT,2)
    data = response.json()
    assert response.status_code == 200

def test_listOfUsers():
    response = get_listOfUsers(ENDPOINT,1)
    data = response.json()
    assert data["page"] == 1
    assert len(data) == 6
    assert response.status_code == 200
    

def test_creationOfUser():
    userCreation = {
        "name": "marwan",
        "job": "software engineer"
    }

    create_user_response = createUser(ENDPOINT, userCreation) 
    assert create_user_response.status_code == 201
    
    data = create_user_response.json()
    assert data["createdAt"]

def test_updateUser():
    payLoad = {
        "name": "marwan",
        "job": "software engineer" 
    }

    updateResponse = updateUser(ENDPOINT, payLoad)
    assert updateResponse.status_code == 200
    
    data = updateResponse.json()
    print(data["updatedAt"])
    assert data["updatedAt"]

    now = date.today()
    stringNow = str(now)
    print(stringNow)
    date_only_str = data["updatedAt"][:10]
    # date_only = datetime.strptime(date_only_str, "%Y-%m-%d").date()
    assert stringNow == date_only_str
    




