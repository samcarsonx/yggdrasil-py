'''
Python wrapper for Mojang's Yggdrasil authentication service by Sam Carson.
Works on Python 3.6+ due to f-strings but can be changed to %s or .format()
'''

import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def authenticate(username:str, password:str, agentName:str = 'Minecraft', clientToken:str = None, requestUser:str = False):
    '''
    Authenticates a user using their password.
    Parameters:
      username - Username of agent/Mojang email (if migrated)
      password - Password for the account used
      agentName - Agent, defaults to Minecraft, can also be Scrolls
      clientToken - Client identifier, must be random and identical per request
      requestUser - If set to True, request for user object too
    '''
    data = json.dumps({"agent":{"name":agentName,"version":1}, "username":username, "password":password, "clientToken":clientToken, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/authenticate', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response

def refresh(accessToken:str, clientToken:str, requestUser:bool = False):
    '''
    Refreshes a valid accessToken. It can be used to keep a user logged in between gaming sessions and is preferred over storing the user's password in a file.
    Parameters:
      accessToken - Valid accessToken, gained from authenticate()
      clientToken - Identical to the clientToken used to get the accessToken in the first place
      requestUser - If set to True, request for user object too
    '''
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/refresh', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response

def validate(accessToken:str, clientToken:str = None):
    '''
    Checks if an accessToken is usable for authentication with a Minecraft server.
    Parameters:
      accessToken - Valid accessToken, gained from authenticate()
      clientToken - Identical to the clientToken used to get the accessToken in the first place
    '''
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken})
    try: response = json.loads(requests.post(url + '/validate', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    return False

def signout(username:str, password:str):
    '''
    Invalidates accessTokens using an account's username and password.
    Parameters:
      username - Username of agent/Mojang email (if migrated)
      password - Password for the account used
    '''
    data = json.dumps({"username":username, "password":password})
    try: response = json.loads(requests.post(url + '/signout', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    return False

if __name__ == '__main__':
    raise Exception('Must be imported, not run as standalone')
