from flask import Flask

app=Flask(__name__)


app.config['SECRET_KEY']='thisisfirstflaskapp'

from pbl import routes