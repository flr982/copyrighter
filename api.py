# -*- coding: utf-8 -*-
from flask import Flask, request, send_file
import os, flask, sys
from replacer import rpl
from updater import add_key, rm_key

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file("home.txt")

@app.route('/replace/', methods=['POST'])
def post_file():
    input_file = request.stream.read().decode()
    rpl(input_file)
    return send_file("output.txt", attachment_filename='modified.txt', as_attachment=True)

@app.route('/keywords/', methods=['GET'])
def get():
    return app.send_static_file("Keyword.txt")

@app.route('/keywords/add/<name>', methods=['POST'])
def get_add(name):
    return add_key(name)

@app.route('/keywords/remove/<name>', methods=['POST'])
def post_rm(name):
    return rm_key(name)

@app.route('/versions/', methods=['GET'])
def flask_version():
    return("We're running flask %s on python %s" % (flask.__version__, sys.version))



if __name__ == '__main__':
    app.run(host='0.0.0.0')

