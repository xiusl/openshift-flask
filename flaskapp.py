# coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello openshift'

if __name__ == '__main__':
    app.run('0.0.0.0')
