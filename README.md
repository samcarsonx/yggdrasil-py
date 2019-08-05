# yggdrasil-py
Python 3.6+ wrapper by **Sam Carson** for the **Mojang Yggdrasil authentication service.**
Please reference [the documentation](https://wiki.vg/Authentication) for extra information.

This wrapper is supported only for Python 3.6 and above because of the use of f-strings when an `Exception` is raised. You could easily modify the code to use `%s` formatting or the `.format()` function, but they are not as efficient.

Minecraft 1.6 introduced a new authentication scheme called **Yggdrasil** which completely replaces the [previous authentication system](https://wiki.vg/Legacy_Authentication "Legacy Authentication"). Mojang's other game, Scrolls, uses this method of authentication as well.

## Authenticate
*Authenticates a user using their password.*
```python
def authenticate(username:str, password:str, agentName:str = 'Minecraft', clientToken:str = None, requestUser:str = False):
```
**Arguments:**
* String *(required)*
Username of agent/Mojang email (if migrated)
* String *(required)*
Password for the account used
* String *(optional)*
Agent, defaults to `Minecraft`, can also be `Scrolls`
* String *(optional)*
Client identifier, must be random and identical per request
* Boolean *(optional)*
If set to `True` request for user object too (default is `False`)

**Response:**
* Check the Authenticate section of [the documentation](https://wiki.vg/Authentication#Authenticate) for details.

**Example:**
```python
from yggdrasil import authenticate
import random

randomClientToken = random.randint(10000,99999)
mc = authenticate('test@example.com','p455w0rd', 'Minecraft', randomClientToken, False)
print(mc['accessToken'])
```

## Refresh
*Refreshes a valid accessToken. It can be used to keep a user logged in between gaming sessions and is preferred over storing the user's password in a file.*
```python
def refresh(accessToken:str, clientToken:str, requestUser:bool = False):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(required)*
Identical to the `clientToken` used to get the `accessToken` in the first place
* Boolean *(optional)*
If set to `True` request for user object too (default is `False`)

**Response:**
* Check the Refresh section of [the documentation](https://wiki.vg/Authentication#Refresh) for details.

**Example:**
```python
from yggdrasil import refresh
print(refresh(mc['accessToken'], randomClientToken))
# Note: invalidates inputted accessToken
```

## Validate
*Checks if an accessToken is usable for authentication with a Minecraft server.*
```python
def validate(accessToken:str, clientToken:str = None):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(optional)*
Identical to the `clientToken` used to get the `accessToken` in the first place

**Response:**
* Returns Boolean for whether `accessToken` is valid (and `clientToken` match, if defined)

**Example:**
```python
from yggdrasil import validate
print(validate(mc['accessToken'], randomClientToken))
```

## Signout
*Invalidates accessTokens using an account's username and password.*
```python
def signout(username:str, password:str):
```
**Arguments:**
* String *(required)*
Username of agent/Mojang email (if migrated)
* String *(required)*
Password for the account used

**Response:**
* Returns `True` unless error thrown

**Example:**
```python
from yggdrasil import signout
print(signout('test@example.com','p455w0rd'))
```

## Invalidate
*Invalidates accessTokens using a client/access token pair.*
```python
def invalidate(username:str, password:str):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(required)*
Identical to the `clientToken` used to get the `accessToken` in the first place

**Response:**
* Returns `True` unless error thrown

**Example:**
```python
from yggdrasil import invalidate
print(signout(mc['accessToken'], randomClientToken))
```
