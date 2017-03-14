# importing the obvious
from sense_hat import SenseHat
from time import sleep
from random import randint

# function to move items in an array to left and fill with "w", do not rotate if line has no stripe
def rotateline ():
    for i in range(8):
        if timer[i] > 0:
            image[i].append(w)
            del image[i][0]
    return

# create image to display from 8 separate items and just items 0 to 7 from each one
def createline():
    final = image[0][0:8]+image[1][0:8]+image[2][0:8]+image[3][0:8]+image[4][0:8]+image[5][0:8]+image[6][0:8]+image[7][0:8]
    return final

# decrease timers for each line which has a stripe
def tick():
    for i in range(8):
        if timer[i] > 0:
            timer[i] = timer[i] - 1
    return

# setup the enviroment, my HAT is upside down so rotate 180 degrees and clear the HAT leds
sense = SenseHat()
sense.set_rotation(180)
sense.clear()

# define many colors
w = (0,0,0)
r1 = (255,0,0)
r2 = (192,0,0)
r3 = (129,0,0)
r4 = (66,0,0)
g1 = (0,255,0)
g2 = (0,192,0)
g3 = (0,129,0)
g4 = (0,66,0)
b1 = (0,0,255)
b2 = (0,0,192)
b3 = (0,0,129)
b4 = (0,0,66)
rb1 = (255,0,255)
rb2 = (192,0,192)
rb3 = (129,0,129)
rb4 = (66,0,66)
gb1 = (0,255,255)
gb2 = (0,192,192)
gb3 = (0,129,129)
gb4 = (0,66,66)
rg1 = (255,255,0)
rg2 = (192,192,0)
rg3 = (129,129,0)
rg4 = (66,66,0)
rgb1 = (255,255,255)
rgb2 = (192,192,192)
rgb3 = (129,129,129)
rgb4 = (66,66,66)

# degine more stripes
rline = [w,w,w,w,w,w,w,w,r1,r2,r3,r4,w]
gline = [w,w,w,w,w,w,w,w,g1,g2,g3,g4,w]
bline = [w,w,w,w,w,w,w,w,b1,b2,b3,b4,w]
rgline = [w,w,w,w,w,w,w,w,rg1,rg2,rg3,rg4,w]
gbline = [w,w,w,w,w,w,w,w,gb1,gb2,gb3,gb4,w]
rbline = [w,w,w,w,w,w,w,w,rb1,rb2,rb3,rb4,w]
rgbline = [w,w,w,w,w,w,w,w,rgb1,rgb2,rgb3,rgb4,w]

# initialisation of the variables
colors = [rline, gline, bline, rgline, gbline, rbline, rgbline]
line0 = [w,w,w,w,w,w,w,w,w,w,w,w,w]
image = [line0, line0, line0, line0, line0, line0, line0, line0]
timer = [0,0,0,0,0,0,0,0]

# main loop
while True:

    # get a random number
    cislo = randint(0,10)

    # if we get 8-10 then just tick, otherwise do new stripe on this line 
    if cislo < 8:

        # if there is already a stripe on this line, do nothing
        if timer[cislo] == 0:

            # choose a color
            farba = randint(0,6)

            # move predefined stripe to the image
            image[cislo] = list(colors[farba])
            # start a timer for this line
            timer[cislo] = 12
    
    # create the image
    pixels = createline()

    # show the image
    sense.set_pixels(pixels)

    # move lines to the left
    rotateline ()

    # tick
    tick()

    # wait
    sleep(0.1)
