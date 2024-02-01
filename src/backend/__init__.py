from flask import Flask
from routes import create_user, get_user_details

app=Flask(__name__, static_folder='./static', template_folder='./templates')
@app.errorhandler(500)
def error(e):
    return {"code":500,"text":"Internal server error"}, 500
app.add_url_rule("/v1/create_user", view_func=create_user, methods=['POST'])
app.add_url_rule("/v1/get_user_details", view_func=get_user_details, methods=['GET'])
app.run(debug=True)