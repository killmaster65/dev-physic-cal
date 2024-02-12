from flask import Flask, render_template, request


from functions import getdisBySpeedTime, getspeedByTimeDis, gettimeByDisSpeed

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/speedPage')
def speedPage():
    return render_template('speedPage.html')


@app.route('/disPage')
def disPage():
    return render_template('disPage.html')

@app.route('/speedResult')
def speedResult():
    return render_template('speedResult.html')

@app.route('/disResult')
def disResult():
    return render_template('disResult.html')

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
            from functions import answerTime
            
            return render_template("speedResult.html", answerTime = answerTime, 
                                   time = answerTime,
                                   distance = distance,
                                   speed = speed)
        elif speed == 0.0:

            getspeedByTimeDis(time, speed, distance)
            from functions import answerSp
            return render_template("timeResult.html", answerSp = answerSp,
                                   speed = answerSp,
                                   distance = distance,
                                   time = time)
           
            
        elif distance == 0.0:
            getdisBySpeedTime(time, speed, distance)
            from functions import answerDis
            return render_template("disPage.html", answerDis = answerDis,
                                   time = time,
                                   speed = speed,
                                   distance = answerDis)
    except ValueError:
        print("please provide all number posible.")
    


