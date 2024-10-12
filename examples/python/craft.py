"""_This function help you to perform a craftiong action_"""
import time
import requests

def move(item_code, number_of_item):
    """_Craft an item with the character_
    you can find all the items here https://artifactsmmo.com/encyclopedia/items

    Args:
        item_name (_str_): _The item code of what you want to craft_
        number_of_item (_int_): _The number of item you want_
    """
    item_info = {
        "code": item_code,
        "quantity": number_of_item
    }
    #Your account token (https://artifactsmmo.com/account)
    token = "YOUR_TOKEN_HERE"
    #Name of yout character
    character = "CHARACTER_NAME"
    #Server url
    url = f"https://api.artifactsmmo.com/my/{character}/action/crafting"
    timeout = 10
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=item_info, headers=headers, timeout=timeout)
    data = response.json()
    if response.status_code == 200:
        print(f"You win {data['data']['details']['xp']} Exp while making this !")
        time.sleep(data['data']['cooldown']['total_seconds'])
    else:
        print(f'erreur : {response.status_code}')#error gestion with status code
