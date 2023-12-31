# pip install flask

import json
from flask import Flask, render_template ,request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world"

@app.route("/hello")
def hello():
    return  render_template("hello.html", content ="Jack", age=20)
@app.route("/coin", methods=['GET', 'POST'])
def coin():
    if request.method == 'POST':
        data = json.loads(request.get_data(), encoding= 'utf-8')
        print(data)
        res = requests.get("https://api.upbit.com/v1/ticker?markets="+ data['market'])

        print(res)
        return res.content

    else:
        res = requests.get("https://api.upbit.com/v1/market/all")
        coin_list = json.loads(res.content)
        print(coin_list)
        return render_template('coin.html', coins=coin_list)

if __name__ =='__main__':
    app.run(debug=True, port=5555)