from models import User
from flask import request
from utils import get_password_sum
from sqlite3 import connect

def create_user():
    user = User()
    user.username = request.form.get('username')
    user.email = request.form.get('email')
    user.password = get_password_sum(request.form.get('password'))
    user.avatar = request.form.get('avatar')
    user.bio = request.form.get('bio')
    valid, message = user.validate()
    if valid:
        database=connect("./databases/users.db")
        cursor=database.cursor()
        if cursor.execute("SELECT * FROM users WHERE username=?",(user.username,)).fetchall():
            return {"code":400,"text":"Username already taken"}, 400
        if cursor.execute("SELECT * FROM users WHERE email=?",(user.email,)).fetchall():
            return {"code":400,"text":"Email already taken"}, 400
        cursor.execute("INSERT INTO users VALUES (NULL,?,?,?,?,?,?,?)",user._to_sql(specify_id=False))
        database.commit()
        cursor.close()
        return {"code":201,"text":"User created"}, 201
    else:
        return {"code":400,"text":message}, 400
