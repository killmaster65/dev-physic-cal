from flask import Flask, render_template

from funtions import getdisBySpeedTime, getspeedByTimeDis, gettimeByDisSpeed

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/speedPage')
def speedPage():
    return render_template('speedPage.html')
from flask import Flask, request, render_template


@app.route('/speedPage', methods=['get'])
def my_form_post():
    try:
        speed = request.form['speed']
        time = request.form['time']
        distance = request.form['distance']
        if time == 0:
            answerTime = 0
            gettimeByDisSpeed()
            return render_template("speedPage.html", answerTime = answerTime)
        elif speed == 0:

            getspeedByTimeDis()
            
        elif distance == 0:
            getdisBySpeedTime()
           
    except ValueError:
        print("please provide all number posible.")
    


