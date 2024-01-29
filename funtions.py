



def getspeedByTimeDis():
  global speed
  distance = input("what is the total distance?: ")
  distance = float(distance)
  print("  ")
  time = input("what is the total time?: ")
  time = float(time)
  print("  ")
  speed = distance/time
  print("the speed is: ",speed)
  print("  ")

def getdisBySpeedTime():
  global distance
  speed = input("what is the speed?: ")
  speed = float(speed)
  print("  ")
  time = input("what is the time?: ")
  time = float(time)
  print("  ")
  distance = speed*time
  print("the distance is: ",distance)

def gettimeByDisSpeed(time,distance,speed):
  global answer
  time = float(time)
  distance = float(distance)
  speed = float(speed)
  time = distance/speed
  answerTime = time
  
