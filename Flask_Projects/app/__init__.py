from flask import Flask 

enviroment = Flask(__name__)

@enviroment.route("/") #Decorador python
def index ():
    return "<h1> My app </h1>"