from flask import Flask, render_template, request

from funtions import getdisBySpeedTime, getspeedByTimeDis, gettimeByDisSpeed

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/speedPage')
def speedPage():
    return render_template('speedPage.html')


@app.route('/speedPage', methods=['POST'])
def my_form_post():
    #try:
        speed = float(request.form['speedInt'])
        time = float(request.form['timeInt'])
        distance = float(request.form['distInt'])
     
        if time == 0:
            print("works")
            answerTime = 0
            gettimeByDisSpeed(speed,time,distance)
            return render_template("result.html", answerTime = answerTime)
        # elif speed == 0:

        #     getspeedByTimeDis()
            
        # elif distance == 0:
        #     getdisBySpeedTime()
           
#except ValueError:
 #       print("please provide all number posible.")
    


