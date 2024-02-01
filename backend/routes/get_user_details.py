from models import User
from flask import request
from sqlite3 import connect

def get_user_details():
    user_id=request.args.get('user_id',"")
    if not user_id.isdecimal():
        return {"code":400,"text":"Invalid user_id"}, 400
    database=connect("./databases/users.db")
    cursor=database.cursor()
    user=cursor.execute("SELECT * FROM users WHERE id=?",(user_id,)).fetchone()
    cursor.close()
    database.close()
    if not user:
        return {"code":400,"text":"User not found"}, 400
    user=User()._from_sql(user)
    return {"code":200,"details":{"id":user.id,"registered_on":user.registered_on,"username":user.username,"email":user.email,"tags":user.tags,"avatar":user.avatar,"bio":user.bio}}, 200