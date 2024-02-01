from models import User
from flask import request, current_app
from sqlite3 import connect
from utils import get_password_sum, generate_token

def login():
    username=request.form.get('username',"")
    password=request.form.get('password',"")
    revoke_others=request.form.get('revoke_others',False) == "true"
    if not username or not password:
        return {"code":400,"text":"Username and password are required"}, 400
    database=connect("./databases/users.db")
    cursor=database.cursor()
    user=cursor.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
    cursor.close()
    database.close()
    if not user:
        return {"code":400,"text":"User not found"}, 400
    user=User()._from_sql(user)
    if user.password!=get_password_sum(password):
        return {"code":400,"text":"Invalid password"}, 400
    if len(current_app.config['tokens'].get(user.id,[])) >= 10:
        if not revoke_others:
            return {"code":400,"text":"Too many tokens"}, 400
        else:
            token=generate_token()
            current_app.config['tokens'][user.id]=[token]
            return {"code":200,"token":token}, 200
    token=generate_token()
    if user.id in current_app.config['tokens'].keys():
        current_app.config['tokens'][user.id].append(token)
    else:
        current_app.config['tokens'][user.id]=[token]
    return {"code":200,"token":token}, 200
