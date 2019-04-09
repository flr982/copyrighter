# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
#from flask_restful import Resource, Api
import os
from replacer import rpl
from  updater import add_key, rm_key

app = Flask(__name__)
#api = Api(app)

@app.route('/', methods=['GET'])
def get_home():
    return app.send_static_file("home.txt")

@app.route('/replace/', methods=['POST'])
def post_file():
    input_file = request.stream.read().decode()
    return rpl(input_file)

@app.route('/keywords/', methods=['GET'])
def get():
    return app.send_static_file("Keyword.txt")

@app.route('/keywords/add/<name>', methods=['POST'])
def get_add(name):
    return add_key(name)

@app.route('/keywords/remove/<name>', methods=['POST'])
def post_rm(name):
    return rm_key(name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

