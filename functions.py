import math



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

def kineticEnergyByMV(mass,velocity):
  global keAnswer
  global kjAnswer
  keAnswer = (mass*(velocity**2))/2
  kjAnswer = keAnswer/1000

def massByKEV(mass,kineticEnergy,velocity):
  global massA
  massA = 2*(kineticEnergy/velocity**2)

def getdisplacement(final, beginning):
  global displacementA
  displacementA = final - beginning
def velocityByKEM(mass,kineticEnergy):

  global velocityA
  velocityA =  math.sqrt(kineticEnergy*2/mass)

def massbyGE(mass, ge, height, gravity):
  global massA
  massA = ge/(height*gravity)

def heightByGE(mass, ge , gravity):
  global heightA
  heightA = ge/(mass*gravity)