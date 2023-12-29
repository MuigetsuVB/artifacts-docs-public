import requests
import time

#Server url
server = "https://api.artifactsmmo.com"
#Your account token (https://artifactsmmo.com/account)
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QxMjMiLCJwYXNzd29yZF9jaGFuZ2VkIjoiIn0.L7aSRLu6x_Q8RjfloNIKAjYg-qeCrKcPzlESnpeNe-Q"
#Name of yout character
character = "test" 
cooldown = 5

def perform_gathering() -> int:
    url = f"{server}/my/{character}/action/gathering"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    gathering_response  = requests.post(url, headers=headers)

    #Errors examples (Full list: https://docs.artifactsmmo.com/api_guide/codes)
    if gathering_response.status_code == 498:
        print(f"The character cannot be found on your account.")
        exit()

    if gathering_response.status_code == 497:
        print(f"Your character's inventory is full.")
        exit()

    if gathering_response.status_code == 499:
        print(f"Your character is in cooldown.")

    if gathering_response.status_code == 496:
        print(f"The resource is too high-level for your character.")
        exit()

    if gathering_response.status_code != 200:
        print(f"An error occured while gathering the ressource.")
        exit()

    #If an action is successful, it will be in code 200
    if(gathering_response.status_code == 200):

        data = gathering_response.json()["data"]
        print(f"Your character successfully gathered the ressource.")

        #Return the cooldown in seconds
        return data["cooldown"]["totalSeconds"]

#Loop
while True:
    cooldown = perform_gathering()

    # Wait for the cooldown
    time.sleep(cooldown)