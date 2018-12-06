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

while(True):
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up": #Add overflow detection
                min_sel += 1
            elif event.direction == "down":
                min_sel -= 1
            elif event.direction == "middle":
                pass
        show_numbers(min_sel)
            