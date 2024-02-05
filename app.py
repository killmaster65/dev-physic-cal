from flask import Flask, render_template, request


from funtions import getdisBySpeedTime, getspeedByTimeDis, gettimeByDisSpeed

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/speedPage')
def speedPage():
    return render_template('speedPage.html')

@app.route('/speedPage', methods=['post'])
def my_form_post():
    try:
        speed = request.form['speedInt']
        time = request.form['timeInt']
        distance = request.form['distInt']
        speed = float(speed)
        time = float(time)
        distance = float(distance)
        if time == 0.0:
            gettimeByDisSpeed(time, speed, distance)
            from funtions import answerTime
            return render_template("result.html", answerTime = answerTime)
        elif speed == 0.0:

        #     getspeedByTimeDis()
           
        elif distance == 0.0:
            getdisBySpeedTime()
           
#except ValueError:
 #       print("please provide all number posible.")
    


