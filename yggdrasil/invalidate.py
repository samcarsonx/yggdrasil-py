import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def invalidate(accessToken:str, clientToken:str, authServer:str = url):
    '''
    Invalidates accessTokens using a client/access token pair.
    Parameters:
      accessToken - Valid accessToken, gained from authenticate()
      clientToken - Identical to the clientToken used to get the accessToken in the first place
      authServer - Authentication server, defaults to authserver.mojang.com
    Returns: True if success, otherwise the error
    '''
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken})
    try: response = json.loads(requests.post(authServer + '/invalidate', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    return False
