
# yggdrasil-py
 [![PyPI Version](https://img.shields.io/pypi/v/yggdrasil-py)](https://pypi.org/project/yggdrasil-py/)
 [![MIT Licence](https://img.shields.io/github/license/samcarsonx/yggdrasil-py)](https://github.com/samcarsonx/yggdrasil-py/blob/master/LICENSE.txt)
 [![Forks](https://img.shields.io/github/forks/samcarsonx/yggdrasil-py)](https://github.com/samcarsonx/yggdrasil-py/fork)
 [![Stars](https://img.shields.io/github/stars/samcarsonx/yggdrasil-py)](https://github.com/samcarsonx/yggdrasil-py/stargazers)
 [![Open Issues](https://img.shields.io/github/issues/samcarsonx/yggdrasil-py)](https://github.com/samcarsonx/yggdrasil-py/issues)
 ![Supported Versions](https://img.shields.io/pypi/pyversions/yggdrasil-py)
 ![Last Commit](https://img.shields.io/github/last-commit/samcarsonx/yggdrasil-py)
 ![Commits since last release](https://img.shields.io/github/commits-since/samcarsonx/yggdrasil-py/latest)
 ![PyPI Status](https://img.shields.io/pypi/status/yggdrasil-py)

Open-source Python 3.6+ wrapper by **Sam Carson** for the **Mojang Yggdrasil authentication service.** Please reference [the documentation](https://wiki.vg/Authentication) for extra information.

**Install via PyPI using the following command:** `pip install yggdrasil-py`

This wrapper is supported only for Python 3.6 and above because of the use of f-strings when an `Exception` is raised. You could easily modify the code to use `%s` formatting or the `.format()` function, but they are not as efficient.

Minecraft 1.6 introduced a new authentication scheme called **Yggdrasil** which completely replaces the [previous authentication system](https://wiki.vg/Legacy_Authentication "Legacy Authentication"). Mojang's other game, Scrolls, uses this method of authentication as well.

Since a recent [pull request](https://github.com/samcarsonx/yggdrasil-py/pull/1), support has been added for custom authentication servers. As far as I am aware, the only instance of this is [ely.by](https://ely.by).

## Authenticate
*Authenticates a user using their password.*
```python
def authenticate(username:str, password:str, agentName:str = 'Minecraft', clientToken:str = None, requestUser:str = False, authServer:str = url):
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
* String *(optional)*
Custom authentication server. Defaults to `https://authserver.mojang.com`

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
def refresh(accessToken:str, clientToken:str, requestUser:bool = False, authServer:str = url):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(required)*
Identical to the `clientToken` used to get the `accessToken` in the first place
* Boolean *(optional)*
If set to `True` request for user object too (default is `False`)
* String *(optional)*
Custom authentication server. Defaults to `https://authserver.mojang.com`

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
def validate(accessToken:str, clientToken:str = None, authServer:str = url):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(optional)*
Identical to the `clientToken` used to get the `accessToken` in the first place
* String *(optional)*
Custom authentication server. Defaults to `https://authserver.mojang.com`

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
def signout(username:str, password:str, authServer:str = url):
```
**Arguments:**
* String *(required)*
Username of agent/Mojang email (if migrated)
* String *(required)*
Password for the account used
* String *(optional)*
Custom authentication server. Defaults to `https://authserver.mojang.com`

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
def invalidate(accessToken:str, clientToken:str, authServer:str = url):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(required)*
Identical to the `clientToken` used to get the `accessToken` in the first place
* String *(optional)*
Custom authentication server. Defaults to `https://authserver.mojang.com`

**Response:**
* Returns `True` unless error thrown

**Example:**
```python
from yggdrasil import invalidate
print(signout(mc['accessToken'], randomClientToken))
```
