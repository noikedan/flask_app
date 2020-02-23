import json
import os

from flask import Flask, redirect, render_template, request

application = Flask(__name__)

DATA_FILE = "onelineChat.json"


def save_data(name, memo):
    """記録データを保存します
     :param name: お名前
     :type name: str

    :param memo: メモ
    :type memo: str
    :return: None
    """
    try:

        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []

    database.insert(0, {
        "name": name,
        "memo": memo
    })

    json.dump(database, open(DATA_FILE, mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)


def load_data():
    """記録データを返します"""
    try:
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []
    return database

@application.route('/', methods=['POST'])
def save():
    if request.method == 'POST':

        name = request.form.get('name')
        memo = request.form.get('memo')

        save_data(name , memo)

        return redirect('/')


@application.route('/')
def index():
    """トッフぺージテンプレートを使用してぺージを表示します"""

    rides = load_data()
    return render_template('index.html', rides=rides)

port = os.getenv('VCAP_APP_PORT', '5050')



if __name__ == '__main__':
    application.run(host='0.0.0.0', port=int(port), debug=True)
