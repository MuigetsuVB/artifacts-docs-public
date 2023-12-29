import requests
import time

#Server url
server = "https://api.artifactsmmo.com"
#Your account token (https://artifactsmmo.com/account)
token = "YOUR_TOKEN_HERE"
#Name of yout character
character = "CHARACTER_NAME" 
cooldown = 5

def perform_gathering() -> int:
    url = f"{server}/my/{character}/action/gathering"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    gathering_response  = requests.post(url, headers=headers)

    if gathering_response.status_code == 498:
        print("The character cannot be found on your account.")
        exit()
    elif gathering_response.status_code == 497:
        print("Your character's inventory is full.")
        exit()
    elif gathering_response.status_code == 499:
        print("Your character is in cooldown.")
    elif gathering_response.status_code == 493:
        print("The resource is too high-level for your character.")
        exit()
    elif gathering_response.status_code != 200:
        print("An error occured while gathering the ressource.")
        exit()
    else:
        data = gathering_response.json()["data"]
        print("Your character successfully gathered the ressource.")

        #Return the cooldown in seconds
        return data["cooldown"]["totalSeconds"]

#Loop
while True:
    cooldown = perform_gathering()

    # Wait for the cooldown
    time.sleep(cooldown)