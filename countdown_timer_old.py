from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

color = (0,255,0)
           
def show_pixels(numbers):
  for y in range(1,9):
      for x in range(0,8):
          pixel = numbers[((y-1)*8)+x]
          sense.set_pixel(x, y-1, pixel*color[0], pixel*color[1], pixel*color[2])

DIGIT = [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1, #0
         0,0,1,0,0,1,0,0,1,0,0,1,0,0,1, #1
         1,1,1,0,0,1,1,1,1,1,0,0,1,1,1, #2
         1,1,1,0,0,1,1,1,1,0,0,1,1,1,1, #3
         1,0,1,1,0,1,1,1,1,0,0,1,0,0,1, #4
         1,1,1,1,0,0,1,1,1,0,0,1,1,1,1, #5
         1,1,1,1,0,0,1,1,1,1,0,1,1,1,1, #6
         1,1,1,0,0,1,0,0,1,0,0,1,0,0,1, #7
         1,1,1,1,0,1,1,1,1,1,0,1,1,1,1, #8
         1,1,1,1,0,1,1,1,1,0,0,1,1,1,1] #9
         
# MAIN         
         
print("Timer (MAX. 960 secs)")
time = int(input("Set timer (sec): "))

sec = 0
while(time > 0):
    
    if time % 60 == 0:
      sec += 60
    else:
      sec = time % 60
    
    if not time <= 60: # Time more than 60 / Dot Timer Required
        dot = int(time / 60)
        dotTimerPixel = ([1]*dot) + ([0]*(16-dot))
    else:
        dotTimerPixel = [0]*16 # Time less than or equal to 60
    
    first_digit = int(sec / 10)
    second_digit = sec-(int(sec/10)*10)
    
    numbers = []
    for j in range(0,5):
        temp = []
        if first_digit != 0:
            temp_digit_first = DIGIT[15*first_digit + (j*3) : 15*first_digit + (j*3) +3]
        else:
            temp_digit_first = [0] * 3
        temp_digit_second = DIGIT[15*second_digit + (j*3) : 15*second_digit + (j*3) +3]
        temp = temp + [0] + temp_digit_first + [0] + temp_digit_second
        numbers += temp
    
    sec -= 1
    time -= 1
  
    pixels = dotTimerPixel + [0]*8 + numbers
    show_pixels(pixels)
    sleep(1)
           
smile = [0]*8 + ([0,1,1,0]*4) + [0]*8 + ([0,1,1,0]*2) + [0] + [1]*6 + [0]*3 + [1]*4 + [0]*10
show_pixels(smile)
