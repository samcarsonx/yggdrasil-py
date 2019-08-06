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
    Returns: Formatted JSON, see API documentation
    '''
    data = json.dumps({"agent":{"name":agentName,"version":1}, "username":username, "password":password, "clientToken":clientToken, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/authenticate', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response
