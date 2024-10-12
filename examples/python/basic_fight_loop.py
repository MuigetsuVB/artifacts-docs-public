"""
_This function perform a fight action_ 
(https://api.artifactsmmo.com/docs/#/operations/action_fight_my__name__action_fight_post)
"""
import time
import requests

def fight():
    """Fight mob on a map tile"""

    #Your account token (https://artifactsmmo.com/account)
    token = "YOUR_TOKEN_HERE"

    #Name of yout character
    character = "CHARACTER_NAME"

    #Server url
    url = f"https://api.artifactsmmo.com/my/{character}/action/fight"
    timeout = 10

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers, timeout=timeout)
    if response.status_code == 200:
        data = response.json()
        print(f"You {data['data']['fight']['result']} the fight!") #fight result
        print(f"You win {data['data']['fight']['xp']} Exp points")#exp gain
        print(f"You win {data['data']['fight']['gold']} Gold")#gold gain
        for item in data['data']['fight']['drops']:#all items drop by the monster
            print(f"You found {item['quantity']} {item['code']}")#item code and quantity
        time.sleep(data['data']['cooldown']['total_seconds'])#cooldown managment before next action
    else:
        print(f'error : {response.status_code}')#error gestion with status code

#main loop
while True:
    fight()
