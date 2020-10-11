import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def validate(accessToken:str, clientToken:str = None, authServer:str = url):
    '''
    Checks if an accessToken is usable for authentication with a Minecraft server.
    Parameters:
      accessToken - Valid accessToken, gained from authenticate()
      clientToken - Identical to the clientToken used to get the accessToken in the first place
      authServer - Authentication server, defaults to authserver.mojang.com
    Returns: Boolean, if accessToken is valid
    '''
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken})
    try: response = json.loads(requests.post(authServer + '/validate', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    return False
