from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

color = (200,100,0)
           
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

def get_digit(num):
    
    first_digit = int(num / 10)
    second_digit = num-(int(num/10)*10)
    return (first_digit, second_digit)

def show_numbers(num):
    
    digit = get_digit(num)
    
    numbers = []
    for j in range(0,5):
        temp = []
        if digit[0] != 0:
            temp_digit_first = DIGIT[15*digit[0] + (j*3) : 15*digit[0] + (j*3) +3]
        else:
            temp_digit_first = [0] * 3
        temp_digit_second = DIGIT[15*digit[1] + (j*3) : 15*digit[1] + (j*3) +3]
        temp = temp + [0] + temp_digit_first + [0] + temp_digit_second
        numbers += temp
    
    pixels = [0]*24 + numbers
    show_pixels(pixels)
    
min_sel = 0
show_numbers(min_sel)

c = True
while(c):
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                if min_sel < 16:
                    min_sel += 1
            elif event.direction == "down":
                if min_sel > 0:
                    min_sel -= 1
            elif event.direction == "middle":
                c = False
                break
        show_numbers(min_sel)
        
sec_sel = 0
show_numbers(sec_sel)

c = True
while(c):
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                if sec_sel < 59:
                    sec_sel += 1
            elif event.direction == "down":
                if sec_sel > 0:
                    sec_sel -= 1
            elif event.direction == "middle":
                c = False
                break
        show_numbers(sec_sel)
        
time = (min_sel*60) + sec_sel

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
    
    digit = get_digit(sec)
    
    numbers = []
    for j in range(0,5):
        temp = []
        if digit[0] != 0:
            temp_digit_first = DIGIT[15*digit[0] + (j*3) : 15*digit[0] + (j*3) +3]
        else:
            temp_digit_first = [0] * 3
        temp_digit_second = DIGIT[15*digit[1] + (j*3) : 15*digit[1] + (j*3) +3]
        temp = temp + [0] + temp_digit_first + [0] + temp_digit_second
        numbers += temp
    
    sec -= 1
    time -= 1
  
    pixels = dotTimerPixel + [0]*8 + numbers
    show_pixels(pixels)
    sleep(1)
           
smile = [0]*8 + ([0,1,1,0]*4) + [0]*8 + ([0,1,1,0]*2) + [0] + [1]*6 + [0]*3 + [1]*4 + [0]*10
show_pixels(smile)
