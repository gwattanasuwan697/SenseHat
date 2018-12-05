from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

color = (0,0,255)

'''numbers = [1,1,1,1,1,1,1,1,
           1,1,1,1,1,1,1,1,
           1,0,0,0,1,0,0,0,
           1,0,1,1,1,1,1,0,
           1,0,0,0,1,0,0,0,
           1,1,1,0,1,0,1,1,
           1,0,0,0,1,0,0,0,
           1,1,1,1,1,1,1,1]'''

pixels = []

for y in range(1,9): #Set Pixels
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

'''def dotTimer(n): # Dot Timer List Creator
  temp = []
  for i in range(0,n):
    temp.append(1)
  n = abs(n-16)
  for i in range(0,n):
    temp.append(0)
  return temp'''
         
# MAIN         
         
print("Timer (MAX. 960 secs)")
time = int(input("Set timer (sec): "))

while(true):
    sec = 0
    
    if not time <= 60: # Time more than 60 / Dot Timer Required
        dot = time / 60
        dotTimerPixel = ([1]*dot) + ([0]*(16-dot))
    else:
        dotTimerPixel = [0]*16 # Time less than or equal to 60
    
    time -= 60
    sec += 60
    
    first_digit = int(sec / 10)
    second_digit = sec-(int(sec/10)*10)
    
    
    numbers = []
    for i in range(0,10):
        temp = []
        for j in range(0,4):
            temp += [0]
            temp_digit = DIGIT[15*]
    
  
pixels = dotTimerPixel + [0]*8 + numbers


        

