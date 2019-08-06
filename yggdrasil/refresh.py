import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def refresh(accessToken:str, clientToken:str, requestUser:bool = False):
    '''
    Refreshes a valid accessToken. It can be used to keep a user logged in between gaming sessions and is preferred over storing the user's password in a file.
    Parameters:
      accessToken - Valid accessToken, gained from authenticate()
      clientToken - Identical to the clientToken used to get the accessToken in the first place
      requestUser - If set to True, request for user object too
    Returns: Formatted JSON, see API documentation
    '''
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/refresh', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response
