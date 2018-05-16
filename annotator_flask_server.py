# IOHAVOC making a flask server to handle POST requests coming from annotator frontend

from flask import Flask, request, render_template, Response
import pprint
import json

app = Flask(__name__)

@app.route('/examples')
def examples():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return("pong")

@app.route('/save', methods=['POST', 'GET'])
def save_annotations():
    print("in save_annotations!!!!")
    return json.dumps({'success':True}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)