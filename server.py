from flask import Flask
app = Flask(__name__)

import os
import json

from config import *

@app.route('/')
def hello_world():
    f = open(STOCK_FILE,'r+')
    return ''+str(json.load(f))

if __name__=="__main__":

    app.run()