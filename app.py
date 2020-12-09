from flask import Flask, jsonify
from flask_cors import CORS
from os import path
import json
import os


app = Flask(__name__)
CORS(app)


def read_file(file_path):
    logs = []
    with open(file_path) as json_file:
        for line in json_file:
            logs.append(json.loads(line))
    return logs


def read_files(folder_path):
    logs = []
    if not path.exists(folder_path):
        print("No Logs folder found")
        return None

    for file in os.listdir(folder_path):
        if file.endswith(".log") or file.endswith(".json"):
            logs += read_file(f"{folder_path}{file}")
    print(len(logs))
    return logs

@app.route('/')
def hello_world():
    return jsonify(read_files("./logs/"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9443)
