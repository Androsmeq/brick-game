import os
import keyboard
import time


clear = lambda: os.system('clear')

height = 20
width = 25

x1 = height-2
y1 = 11
x2 = height-2
y2 = 12
x3 = height -2
y3 = 13
y11= 10
x11=height-2
x33= height-2
y33= 14
ballx = 3
bally = 12

line = 0

mide_sus = 0
mide_jos = 0
left_sus = 0
right_sus = 0
right_jos = 0
left_jos = 0
start = True

while True:
    print(unichr(9619)*(width+2))
    for i in range(height):
        line+=1
        if line == x1:
            print(unichr(9619)+ " "*(y1-2)+unichr(9604)+unichr(9604)+unichr(9604)+unichr(9604)+" "*(width-y3)+unichr(9619))
        elif line == ballx:
            print(unichr(9619)+ " " * (bally - 1) + unichr(9679) + " " * (width - bally)+unichr(9619))

        else:
            print(unichr(9619)+ " "*width+unichr(9619))
    print(unichr(9619)*(width+2))

    if (keyboard.is_pressed('d')):
        if y33==width:
            pass
        else:
            y1 += 1
            y2 += 1
            y3 += 1
            y11+=1
            y33+=1


    elif (keyboard.is_pressed('a')):
        if y1==2:
            pass
        else:
            y1 -= 1
            y2 -= 1
            y3 -= 1
            y11-=1
            y33-=1

    if start:
        ballx +=1
    if ballx==height:
        clear()
        print("Game over!")
        quit()
    if bally==width:
        if right_sus==1:
            right_sus=0
            left_sus=1
        else:
            right_jos=0
            left_jos=1

    if ballx==1:
        if mide_sus ==1:
            mide_sus = 0
            mide_jos =1
        if right_sus==1:
            right_sus=0
            right_jos=1
        if left_sus==1:
            left_sus=0
            left_jos=1
    if bally==1:

        if left_sus==1:
            left_sus=0
            right_sus=1
        else:
            left_jos=0
            right_jos=1


    if mide_sus==1:
        ballx-=1

    if mide_jos==1:
        ballx+=1

    if left_sus==1:
        ballx-=1
        bally-=1

    if right_sus ==1:
        ballx-=1
        bally+=1

    if left_jos==1:
        ballx+=1
        bally-=1

    if right_jos==1:
        ballx+=1
        bally+=1



    if ballx == x2 and bally ==y2:
        print("\a")
        start = False
        mide_sus =1
        mide_jos=0
        left_sus = 0
        right_sus= 0
        left_jos=0
        right_jos=0

    if ballx ==x1 and bally==y1 :
        print("\a")
        start=False
        mide_sus = 0
        mide_jos = 0
        left_sus = 1
        right_sus = 0
        left_jos=0
        right_jos=0

        ballx-=1
        bally-=1
    if ballx == x11 and bally == y11:
        print("\a")
        start=False
        mide_sus = 0
        mide_jos = 0
        left_sus = 1
        right_sus = 0
        left_jos=0
        right_jos=0

        ballx-=1
        bally-=1

    if ballx ==x1 and bally==y3:
        print("\a")
        start=False
        mide_sus = 0
        mide_jos = 0
        left_sus = 0
        right_sus = 1
        left_jos=0
        right_jos=0

        ballx-=1
        bally+=1
    if ballx == x33 and bally == y33:
        print("\a")
        start = False
        mide_sus = 0
        mide_jos = 0
        left_sus = 0
        right_sus = 1
        left_jos = 0
        right_jos = 0

        ballx -= 1
        bally += 1





    time.sleep(.05)
    clear()
    print(ballx)
    print(y1)
    print(right_sus)
    line=0