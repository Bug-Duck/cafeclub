# API Documentation

## Create User

**URL** : `/api/v1/create_user`

**Method** : `POST`

**Data constraints** :

```json
{
    "username": "[non-empty string]",
    "email": "[valid email address]",
    "password": "[non-empty string]",
    "avatar": "[optional string]",
    "bio": "[optional string]"
}
```

**Data example** :

```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword",
    "avatar": "https://example.com/avatar.jpg",
    "bio": "This is a test user."
}
```

### Success Response

**Condition** : If the user was successfully created.

**Code** : `201 CREATED`

**Content example** :

```json
{
    "code": 201,
    "text": "User created"
}
```

### Error Responses

**Condition** : If the provided username or email is already in use.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "Username already taken"
}
```

or

```json
{
    "code": 400,
    "text": "Email already taken"
}
```

**Condition** : If the provided data is invalid (e.g., missing required fields).

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "[specific error message]"
}
```


## Get User Details

**URL** : `/api/v1/get_user_details`

**Method** : `GET`

**URL Parameters** : `user_id=[integer]`

### Success Response

**Condition** : If the user was found in the database.

**Code** : `200 OK`

**Content example** :

```json
{
    "code": 200,
    "details": {
        "id": 1,
        "registered_on": 1706782119,
        "username": "testuser",
        "email": "testuser@example.com",
        "tags": ["tag1", "tag2"],
        "avatar": "https://example.com/avatar.jpg",
        "bio": "This is a test user."
    }
}
```

### Error Responses

**Condition** : If the `user_id` is not provided or is not a decimal.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "Invalid user_id"
}
```

**Condition** : If the user was not found in the database.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "User not found"
}
```


## Login

**URL** : `/api/v1/login`

**Method** : `POST`

**Data constraints** :

```json
{
    "username": "[non-empty string]",
    "password": "[non-empty string]",
    "revoke_others": "[optional boolean]"
}
```

**Data example** :

```json
{
    "username": "testuser",
    "password": "testpassword",
    "revoke_others": true
}
```

### Success Response

**Condition** : If the user was successfully logged in.

**Code** : `200 OK`

**Content example** :

```json
{
    "code": 200,
    "token": "[generated token]"
}
```

### Error Responses

**Condition** : If the provided username or password is incorrect.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "User not found"
}
```

or

```json
{
    "code": 400,
    "text": "Invalid password"
}
```

**Condition** : If the user has too many active tokens and `revoke_others` is not set to true.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "code": 400,
    "text": "Too many tokens"
}
```