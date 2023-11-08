import threading

from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS
from gevent.pywsgi import WSGIServer
import schedule
import time
import subprocess

from db import get_all_users, add_user_to_database
from loginIn import login_can

app = Flask(__name__)
CORS(app)


@app.route('/user', methods=['POST'])
@cross_origin()
def add_user():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if not login_can(username, password):
            response = jsonify({'error': 'Password Error'})
            response.headers['Content-Type'] = 'application/json'  # 指定响应内容类型为 JSON
            return response, 401
        isAdd, msg = add_user_to_database(username, password)
        print("ADD USER:", isAdd, msg)
        if isAdd:
            response = jsonify({'message': 'User added successfully'})
            response.headers['Content-Type'] = 'application/json'  # 指定响应内容类型为 JSON
            return response, 201
        else:
            response = jsonify({'error': msg})
            response.headers['Content-Type'] = 'application/json'
            return response, 500
    else:
        response = jsonify({'error': 'Missing username or password in request'})
        response.headers['Content-Type'] = 'application/json'
        return response, 400


def run_main_script():
    # 运行 main.py 文件
    print("Starting one Day")
    subprocess.run(["python", "main.py"])


def start_flask_app():
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()


if __name__ == '__main__':
    print("Starting flask_thread")

    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.start()
    print("Starting Repeating Repeating Repeating Repeating Repeating Repeating Repeating Repeating")
    schedule.every().day.at("12:00").do(run_main_script)
    while True:
        schedule.run_pending()
        time.sleep(60)  # 休眠一分钟，避免过多资源消耗
