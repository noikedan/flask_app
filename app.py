from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "aaa"

user_data = {}
user_message = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        msg = "こんにちは、ゲスト"  "さん。"
        return render_template("index.html",title="一行チャット",
                               message=msg,
                               post_message=user_message,
                              )

    if request.method == 'POST':
        name = request.form["name"]
        pm = request.form["post_message"]
        user_message.append( name + "!!!" + pm)
        return redirect("/")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)