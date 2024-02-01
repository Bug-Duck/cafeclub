from hashlib import sha512

def get_salt():
    with open("./databases/salt.txt","r") as f:
        return f.read()

def get_password_sum(password: str) -> str:
    return sha512((password+get_salt()).encode("utf-8")).hexdigest()
