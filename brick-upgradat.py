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

b1x = 3
b1y = 23

brick={
    3:3,
    2:12,
    4:9,
    6:15

}

b1 = True
def lovit():
    global mide_sus, mide_jos, right_sus, right_jos, left_jos, left_sus
    if mide_sus == 1:
        mide_sus = 0
        mide_jos = 1
    if right_sus == 1:
        right_sus = 0
        right_jos = 1
    if left_sus == 1:
        left_sus = 0
        left_jos = 1

while True:
    print(unichr(9619)*(width+2))
    for i in range(height):
        line+=1
        if line == x1:
            print(unichr(9619)+ " "*(y1-2)+unichr(9604)+unichr(9604)+unichr(9604)+unichr(9604)+" "*(width-y3)+unichr(9619))
        elif line == ballx:
            if line in brick:
                if bally==brick[line]:
                    print(unichr(9619) + " " *(bally - 1) + unichr(9679) + " " * (width - bally)+unichr(9619) )

                elif bally <= brick[line]:
                    print(unichr(9619) + " " * (bally-1) + unichr(9679) + " " * (brick[line] - bally-2) + unichr(9619)+unichr(9619) + " " * (width - brick[line])+unichr(9619))
                else:
                    print(unichr(9619) + " " * (brick[line] - 2) +unichr(9619)+ unichr(9619) + " " * (bally - brick[line] -1) + unichr(9679) + " " * (width - bally)+unichr(9619))
            else:
                print(unichr(9619)+ " " * (bally - 1) + unichr(9679) + " " * (width - bally)+unichr(9619))
        elif line in brick:
            print(unichr(9619)+ " "*(brick[line]-2)+unichr(9619)+unichr(9619)+" "*(width-brick[line])+ unichr(9619))
        elif ballx == line and line in brick :
            print("aaaaa")
            if bally<=brick[line]:
                print(unichr(9619)+" "*(bally-1)+unichr(9679)+" "*(width-(bally-brick[line]))+unichr(9619)+" "*(width-(bally-brick[line])))
            else:
                print(unichr(9619)+" "*(brick[line]-1)+unichr(9619)+" "*(width-(brick[line]-bally))+unichr(9679)+" "*(width-(bbrick[line]-bally)))
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


    if ballx == b1x and bally == b1y:
        b1=False
        lovit()
        b1y=0
    if ballx in brick and bally== brick[ballx]:
        brick.pop(ballx)
        lovit()
    if ballx in brick and bally == brick[ballx]+1:
        brick.pop(ballx)
        lovit()

    if bally == width:


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





    time.sleep(.1)
    clear()
    print(ballx)
    print(bally)

    line=0