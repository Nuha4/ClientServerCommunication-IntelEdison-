from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

from pymongo import MongoClient

#Connect to MongoDB
client = MongoClient(port=27017)
db = client.SensorEdisonDatabase

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getdata', methods=['GET'])
def get_data():
    result = db.data_table.find()
    data_list = []
    for res in result: 
        data = {
            'id' : res['id'],
            'name': res['name'], 
            'value': res['value']
        }
        data_list.append(data)
    return jsonify(data_list)

@app.route('/postdata', methods=['POST'])
def post_data():
    dataId = request.form['id']
    print("Data is: "+dataId)
    name = request.form['name']
    print("Data is: "+name)
    value = request.form['value']
    print("Data is: "+dataId + " name:"+name + " value:" +value)
    data = {
            'id' : dataId,
            'name': name, 
            'value': value
        }
    result=db.data_table.insert_one(data)
    return "added"

