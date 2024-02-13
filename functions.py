



def getspeedByTimeDis(time, speed, distance):
  global answerSp
  speed = distance/time
  answerSp = speed
  return answerSp

def getdisBySpeedTime(time, speed, distance):
  global answerDis
  distance = speed*time
  answerDis = distance
  return answerDis
 

def gettimeByDisSpeed(time,speed,distance):

  global answerTime
  time = distance/speed
  answerTime =+ time
  return answerTime

def kineticEnergy(mass,velocity):
  global keAnswer
  global kjAnswer
  keAnswer = (mass*(velocity**2))/2
  kjAnswer = keAnswer/1000
