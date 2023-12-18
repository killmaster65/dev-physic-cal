def getspeed():
  global speed
  distance = input("what is the total distance?: ")
  distance = float(distance)
  print("  ")
  time = input("what is the total time?: ")
  time = float(time)
  print("  ")
  speed = distance/time
  print("the speed is: ",speed)