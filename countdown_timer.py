from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

color = (0,0,255)

numbers = [1,1,1,1,1,1,1,1,
           1,1,1,1,1,1,1,1,
           1,0,0,0,1,0,0,0,
           1,0,1,1,1,1,1,0,
           1,0,0,0,1,0,0,0,
           1,1,1,0,1,0,1,1,
           1,0,0,0,1,0,0,0,
           1,1,1,1,1,1,1,1]

#numbers = []

for y in range(1,9):
  for x in range(0,8):
    pixel = numbers[((y-1)*8)+x]
    sense.set_pixel(x, y-1, pixel*color[0], pixel*color[1], pixel*color[2])

DIGIT = [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1, #1
         1,1,1,0,0,1,1,1,1,1,0,0,1,1,1, #2
         1,1,1,0,0,1,1,1,1,0,0,1,1,1,1, #3
         1,0,1,1,0,1,1,1,1,0,0,1,0,0,1, #4
         1,1,1,1,0,0,1,1,1,0,0,1,1,1,1, #5
         1,1,1,1,0,0,1,1,1,1,0,1,1,1,1, #6
         1,1,1,0,0,1,0,0,1,0,0,1,0,0,1, #7
         1,1,1,1,0,1,1,1,1,1,0,1,1,1,1, #8
         1,1,1,1,0,1,1,1,1,0,0,1,1,1,1] #9

def dotTimer(n): # Dot Timer List Creator
  temp = []
  for i in range(0,n):
    temp.append(1)
  n = abs(n-16)
  for i in range(0,n):
    temp.append(0)
  return temp 
         
print("Timer (MAX. 960 secs)")
time = input("Set timer (sec): ")

if not time <= 60: # Time more than 60 / Dot Timer Required
  dot = time / 60
  dotTimerPixel = dotTimer(dot)
else:
  pass # Time less than or equal to 60
