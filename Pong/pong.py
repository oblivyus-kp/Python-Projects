from graphics import *
import random


RADIUS = 17
color = "purple"
win_width = 800
win_height = 600

# instantiate window
win = GraphWin("window", win_width, win_height)


# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(win_width/2, win_height/2)

# instantiate ball with center at (160, 120)
ball = Circle(center, RADIUS)

# fill the circle with black
ball.setFill(color)

# draw the circle to the window
ball.draw(win)

velocity = 0.12
v2 = 0.12

p1 = Point(30,400)
p2 = Point(50,250)
paddle1 = Rectangle(p1,p2)
paddle1.setFill("blue")
paddle1.draw(win)

p3 = Point(750,400)
p4 = Point(770,250)
paddle2 = Rectangle(p3,p4)
paddle2.setFill("purple")
paddle2.draw(win)

def paddleMove(paddle):
    user_event = win.checkKey()
    if user_event == 'w' and pady>140:
        paddle1.move(0,-20)
    if user_event == 's' and padY<450:
        paddle1.move(0,20)
    if user_event == 'Up' and pady2>140:
        paddle2.move(0,-20)
    if user_event == 'Down' and padY2<450:
        paddle2.move(0,20)

p1point = Point(win_width/6, 20)
message = Text(p1point, 'Player 1: 0')
message.setSize(14)
message.setTextColor("Dark Blue")
message.setFace('helvetica')
message.draw(win)

p2point = Point(win_width*(5/6), 20)
message2 = Text(p2point, 'Player 2: 0')
message2.setSize(14)
message2.setTextColor("Purple")
message2.setFace('helvetica')
message2.draw(win)

e = Point(win_width/2, win_height/2)
e1 = Text(e, 'PONG')
e1.setSize(12)
e1.setTextColor('BLACK')
e1.draw(win)


score1 = 0
score2 = 0

while True:
    

    #getting y values for top and bottom of both paddle1
    padPt = paddle1.getP2()
    padY = padPt.getY()
    padPt2 = paddle2.getP2()
    padY2 = padPt2.getY()

    #paddle2
    padPt3 = paddle1.getP1()
    pady = padPt3.getY()
    padPt4 = paddle2.getP1()
    pady2 = padPt4.getY()

    #getting x values for paddles
    pad = paddle1.getP2()
    padx1 = pad.getX()
    pad2 = paddle2.getP1()
    padx2 = pad2.getX()
    
    paddleMove(paddle1)
    paddleMove(paddle2)

    # move ball along x-axis
    ball.move(velocity, v2)

    # get x-coordinate of circle
    centerBall = ball.getCenter()
    xBall = centerBall.getX()
    yBall = centerBall.getY()


    #bounce of paddle2
    if xBall >= padx2-RADIUS +.1 and (yBall <= pady2 and yBall>= padY2):
        velocity = -velocity
        score2 +=1
        message2.setText('Player 2: '+str(score2))

    #bounce off paddle1
    if xBall <= padx1+RADIUS +.1 and (yBall <= pady and yBall>= padY) :
        velocity = -velocity
        score1 +=1
        message.setText('Player 1: '+str(score1))
        

    #reset ball if goes out of bound <----- TO DO
    if xBall <= RADIUS:
        ball.undraw()
        center = Point(win_width/2, win_height/2)
        ball = Circle(center, RADIUS)
        ball.setFill(color)
        ball.draw(win)
        v2=-v2
        velocity = -velocity
        time.sleep(2)
        
    if xBall >= win_width - RADIUS:
        ball.undraw()
        center = Point(win_width/2, win_height/2)
        ball = Circle(center, RADIUS)
        ball.setFill(color)
        ball.draw(win)
        v2=-v2
        velocity = -velocity
        time.sleep(2)
        
        

    # if there is a mouse click on window, close the window
    if yBall >= win_height-RADIUS:
        v2 = -v2
        
    if yBall <= RADIUS:
        v2 = -v2

    if score1 == 5:
        e1.setText('Player 1 Wins!! \n Press Space to Exit.')
        user_event = win.checkKey()
        if user_event == 'space':
            win.close()
    
    if score2 == 5:
        e1.setText('Player 2 Wins!! \n Press Space to Exit.')
        user_event = win.checkKey()
        if user_event == 'space':
            win.close()



exit(0)



