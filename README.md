# yggdrasil-py
Python 3.6+ wrapper by **Sam Carson** for the **Mojang Yggdrasil authentication service.**
Please reference [the documentation](https://wiki.vg/Authentication) for extra information.

This wrapper is supported only for Python 3.6 and above because of the use of f-strings when an `Exception` is raised. You could easily modify the code to use `%s` formatting or the `.format()` function, but they are not as efficient.

Minecraft 1.6 introduced a new authentication scheme called **Yggdrasil** which completely replaces the [previous authentication system](https://wiki.vg/Legacy_Authentication "Legacy Authentication"). Mojang's other game, Scrolls, uses this method of authentication as well.

## Authenticate
```python
def authenticate(username, password, agentName = 'Minecraft', clientToken = None, requestUser = False):
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
mc = authenticate('test@example.com','p455w0rd', 'Minecraft', 'hello', randomClientToken, False)
print(mc['accessToken'])
```

## Refresh
```python
def refresh(accessToken, clientToken, identifier, name, requestUser = False):
```
**Arguments:**
* String *(required)*
Valid `accessToken`, gained from `authenticate()`
* String *(required)*
Identical to the `clientToken` used to get the `accessToken` in the first place
* String *(required)*
Profile identifier in hexadecimal form
* String *(required)*
Player username
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
```python
def validate(accessToken, clientToken = None):
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
```python
def signout(username, password):
```
**Arguments:**
* String *(required)*
Username of agent/Mojang email (if migrated)
* String *(required)*
Password for the account used

**Response:**
* Returns `True` unless something went wrong in which case `False`

**Example:**
```python
from yggdrasil import signout
print(signout('test@example.com','p455w0rd'))
```
