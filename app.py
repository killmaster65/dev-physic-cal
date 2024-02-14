from flask import Flask, render_template, request


from functions import getdisBySpeedTime, getspeedByTimeDis, gettimeByDisSpeed,massByKEV, velocityByKEM, kineticEnergyByMV


app = Flask(__name__)
@app.route('/kePage')
def kePage():
     return render_template("kePage.html")
@app.route("/massResult")
def massResult():
    return render_template("massResult.html")

@app.route('/keResult')
def keResult():
     return render_template("keResult.html")

@app.route('/velocityResult')
def velocityResult():
     return render_template("velocityResult.html")

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
def speedForm():
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
@ app.route('/kePage',methods=['post'])
def keForm():
    try:
        mass = request.form['massInt']
        velocity = request.form['velocityInt']
        kineticEnergy = request.form['keInt']
        mass = float(mass)
        velocity = float(velocity)
        kineticEnergy = float(kineticEnergy)
        if mass == 0.0:
            massByKEV(mass,kineticEnergy,velocity)
            from functions import massA
            return render_template("massResult.html", massA = massA,
                                   mass = massA,
                                   velocity = velocity,
                                   kineticEnergy = kineticEnergy)
        elif velocity == 0.0:
             velocityByKEM(mass, kineticEnergy)
             from functions import velocityA
             return render_template("velocityResult.html", velocityA = velocityA,
                                    mass = mass,
                                    velocity = velocityA,
                                    kineticEnergy = kineticEnergy)
        elif kineticEnergy == 0.0:
             kineticEnergyByMV(mass, velocity)
             from functions import keAnswer, kjAnswer
             return render_template("keResult.html", kjAnswer = kjAnswer,
                                    keAnswer = keAnswer,
                                    velocity = velocity,
                                    mass = mass)
    except ValueError:
                print("please provide all number posible.")