from flask import Flask, render_template

app: Flask = Flask(__name__)

app.run(debug = True)