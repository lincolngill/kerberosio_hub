#!/usr/bin/env python3
from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("layout.html")

if __name__ == "__main__":
    if os.environ['FLASK_DEBUG'].upper()[0] == "Y":
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:         
        from waitress import serve
        serve(app, host='0.0.0.0', port=8080)