import secrets
with open("./databases/salt.txt","w+") as f:
    f.write(secrets.token_urlsafe(512))