from sense_hat import SenseHat
from time import sleep
from threading import Thread

sense = SenseHat()
sense.clear()

color = (255,255,255)

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

time = 0

final_stop = False

while not final_stop:
    def show_pixels(numbers):
      for y in range(1,9):
          for x in range(0,8):
              pixel = numbers[((y-1)*8)+x]
              if pixel > 1:
                  if pixel == 2:
                      sense.set_pixel(x, y-1, 0, 255, 0)
                  elif pixel == 3:
                      sense.set_pixel(x, y-1, 255, 165, 0)
                  elif pixel == 4:
                      sense.set_pixel(x, y-1, 255, 0, 0)
              else:
                  sense.set_pixel(x, y-1, pixel*color[0], pixel*color[1], pixel*color[2])

    def get_digit(num):
        if num == 60:
          return (0,0)
        first_digit = int(num / 10)
        second_digit = num-(int(num/10)*10)
        return (first_digit, second_digit)

    input = 0

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
        
        emp = [0]*24
        if input != 0:
            if input == 1:
                emp = [4]*5+[0]*5+[4]+[0]*5+[4]*5+[0]*3
            elif input == 2:
                emp = [3]*5+[0]*4+[3]+[0]*6+[3]*5+[0]*3
            elif input == 3:
                emp = [2]+[0]+[2]*3+[0]*3+[2,0]*3+[0]*2+[2]*3+[0]+[2]+[0]*3
        
        pixels = emp + numbers
        show_pixels(pixels)
        
    def gen_dotTimerPixel(time):
        if time <= 60:
          return [0]*24
        
        half_hour = int(time / 1800)
        time = time % 1800
        
        five_mins = int(time / 300)
        time = time % 300
        
        mins = int(time / 60)
        
        pi_mins = [2]*mins + [0]*(8-mins)
        pi_five_mins = [3]*five_mins + [0]*(8-five_mins)
        pi_half_hour = [4]*half_hour + [0]*(8-half_hour)
        return pi_mins + pi_five_mins + pi_half_hour
     
    hr_sel = 0
    input = 1
    show_numbers(hr_sel)

    c = True
    while(c):
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    if hr_sel < 4:
                        hr_sel += 1
                    elif hr_sel == 4:
                        hr_sel = 0
                elif event.direction == "down":
                    if hr_sel > 0:
                        hr_sel -= 1
                    elif hr_sel == 0:
                        hr_sel = 4
                elif event.direction == "middle":
                    c = False
                    break
            show_numbers(hr_sel)

    c = True
    min_sel = 0
    if hr_sel == 4:
        c = False
    else:
        input = 2
        show_numbers(min_sel)
      
    while(c):
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    if min_sel < 59:
                        min_sel += 1
                    elif min_sel == 59:
                        min_sel = 0
                elif event.direction == "down":
                    if min_sel > 0:
                        min_sel -= 1
                    elif min_sel == 0:
                        min_sel = 59
                elif event.direction == "middle":
                    c = False
                    break
            show_numbers(min_sel)
            
    c = True
    sec_sel = 0
    if hr_sel == 4:
        c = False
    else:
        input = 3
        show_numbers(sec_sel)
      
    while(c):
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    if sec_sel < 59:
                        sec_sel += 1
                    elif sec_sel == 59:
                        sec_sel = 0
                elif event.direction == "down":
                    if sec_sel > 0:
                        sec_sel -= 1
                    elif sec_sel == 0:
                        sec_sel = 59
                elif event.direction == "middle":
                    c = False
                    break
            show_numbers(sec_sel)
            
    time = (hr_sel*3600) + (min_sel*60) + sec_sel
    input = 0

    def check_stop():
        global time
        while (time > 0):
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if event.direction == "middle":
                        time = -1
            sleep(1)

    t1 = Thread(target = check_stop)
    t1.start()

    sec = 0
    while(time > 0):
        if time % 60 == 0:
          sec += 60
        else:
          sec = time % 60
        
        dotTimerPixel = gen_dotTimerPixel(time)
        
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
      
        pixels = dotTimerPixel + numbers
        show_pixels(pixels)
        sleep(1)

    if time == 0:
        smile = [0]*8 + ([0,1,1,0]*4) + [0]*8 + ([0,1,1,0]*2) + [0] + [1]*6 + [0]*3 + [1]*4 + [0]*10
        show_pixels(smile)
    elif time == -1:
        stop = [4,0,0,0,0,0,0,4,
                0,4,0,0,0,0,4,0,
                0,0,4,0,0,4,0,0,
                0,0,0,4,4,0,0,0,
                0,0,0,4,4,0,0,0,
                0,0,4,0,0,4,0,0,
                0,4,0,0,0,0,4,0,
                4,0,0,0,0,0,0,4,]
        show_pixels(stop)
    
    wait = True
    while(wait):
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    wait = False
                elif event.direction == "down":
                    wait = False
                    final_stop = True

sense.clear()
