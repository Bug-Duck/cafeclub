from flask import Flask
from routes import create_user, get_user_details, login
from utils import init_app

app=Flask(__name__, static_folder='./static', template_folder='./templates')

init_app(app)

@app.errorhandler(500)
def error(e):
    return {"code":500,"text":"Internal server error"}, 500


app.add_url_rule("/api/v1/create_user", view_func=create_user, methods=['POST'])
app.add_url_rule("/api/v1/get_user_details", view_func=get_user_details, methods=['GET'])
app.add_url_rule("/api/v1/login", view_func=login, methods=['POST'])