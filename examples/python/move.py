"""_This function help you to perform a move action_"""
import time
import requests

def move(x, y):
    """_Move the character to the x and y coord parameters_
    you can find all tiles map coord here https://artifactsmmo.com/encyclopedia/maps

    Args:
        x (_int_): _The X coord of a tile map_
        y (_int_): _The Y coord of a tile map_
    """
    destination_coord = {
        "x": x,
        "y": y
    }
    #Your account token (https://artifactsmmo.com/account)
    token = "YOUR_TOKEN_HERE"
    #Name of yout character
    character = "CHARACTER_NAME"
    #Server url
    url = f"https://api.artifactsmmo.com/my/{character}/action/move"
    timeout = 10
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=destination_coord, headers=headers, timeout=timeout)
    data = response.json()
    if response.status_code == 200:
        print(f"You arrived at {data['data']['destination']['name']}") 
        print(f"The place look like {data['data']['destination']['skin']}")
        print(f"The place contains {data['data']['destination']['content']['code']}")
        time.sleep(data['data']['cooldown']['total_seconds'])
    else:
        print(f'erreur : {response.status_code}')#error gestion with status code
