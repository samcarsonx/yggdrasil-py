'''
Python wrapper for Mojang's Yggdrasil authentication service
by Sam Carson. Works on Python 3.6+
'''

import requests, json

url = 'https://authserver.mojang.com'
headers = {'Content-Type': 'application/json'}

def authenticate(username, password, clientToken = None, requestUser = False):
    data = json.dumps({"agent":{"name":"Minecraft","version":1}, "username":username, "password":password, "clientToken":clientToken, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/authenticate', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response

def refresh(accessToken, clientToken, identifier, name, requestUser = False):
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken, "selectedProfile":{"id":identifier, "name":name}, "requestUser":requestUser})
    response = json.loads(requests.post(url + '/refresh', data=data, headers=headers).text)
    if 'error' in response: raise Exception(f"{response['error']}: {response['errorMessage']}")
    else: return response

def validate(accessToken, clientToken = None):
    data = json.dumps({"accessToken":accessToken, "clientToken":clientToken})
    try: response = json.loads(requests.post(url + '/validate', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    return False

def signout(username, password):
    data = json.dumps({"username":username, "password":password})
    try: response = json.loads(requests.post(url + '/signout', data=data, headers=headers).text)
    except json.decoder.JSONDecodeError: return True
    return False

if __name__ == '__main__': raise Exception('Must be imported, not run as standalone')
