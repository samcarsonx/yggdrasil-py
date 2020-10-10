import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def signout(username:str, password:str, authServer:str = url):
    '''
    Invalidates accessTokens using an account's username and password.
    Parameters:
      username - Username of agent/Mojang email (if migrated)
      password - Password for the account used
      authServer - Authentication server, defaults to authserver.mojang.com
    Returns: True if success, otherwise the error
    '''
    data = json.dumps({"username":username, "password":password})
    try: response = json.loads(requests.post(authServer + '/signout', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    return False
