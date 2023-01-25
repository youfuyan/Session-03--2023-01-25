from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>CSCI5117 Session 03</h1>"
  
@app.route('/fan_site')
def fan_site():
    return render_template('fan_site.html')
  
@app.route('/user', methods=['GET'])
def user():
    username = request.args.get('username')
    return render_template('main.html', username=username)

