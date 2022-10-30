# breakout.py
#
# CS50 AP
# Name: Kenny Pham P.4

from graphics import *
from random import *

# height and width of game's window in pixels
HEIGHT = 600
WIDTH = 400



# number of rows and columns of bricks
ROWS = 5
COLS = 10

# radius of ball in pixels
RADIUS = 10

# size of paddle in pixels
PADWIDTH = 60
PADHT = 10

# number of lives
LIVES = 3

# brick size
BRKWDTH = (WIDTH-COLS)/COLS - 4
BRKHT = 10

# bricks list (array)
bricks = []

# instantiate window
win = GraphWin("Breakout", WIDTH, HEIGHT)


def main():

    # instantiate bricks
    initBricks()

    # instantiate ball, centered in middle of window
    ball = initBall()

    # instantiate paddle, centered at bottom of window
    paddle = initPaddle()

    # instantiate scoreboard, centered in middle of window
    label = initScoreboard()

    # number of lives initially
    lives = LIVES

    # instantiate lives scorekeeper
    livesText = initLives()

    # number of points initially
    score = 0

    # number of bricks initially
    numBricks = COLS * ROWS

    # initial velocity
    xvelocity = 0.07#(random() * 3 + 2)
    yvelocity = 0.07

    #wait for mouse click
    win.getMouse()

    # play game
    while True:

        # move ball move using xvelocity, yvelocity
        ball.move(xvelocity, yvelocity)

        # get x and y coordinate of center of ball (xBall, yBall)
        centerBall = ball.getCenter()
        xBall = centerBall.getX()
        yBall = centerBall.getY()
        

        # bounce off edge of window
        
        
        if yBall <= RADIUS:
            yvelocity = -yvelocity

        if xBall <= RADIUS:
            xvelocity=-xvelocity
        
        if xBall >= WIDTH - RADIUS:
            xvelocity=-xvelocity

        # if ball goes below paddle, decrease lives by 1
        # if no more lives, game over, else sleep 2 seconds and
        # instantiate new ball
        # TODO
      
        if yBall >= HEIGHT:
            lives-=1
            updateLives(livesText, lives)
            ball.undraw()
            ball = initBall()
            if lives == 0:
                gameOver(label)
            time.sleep(2)

                
        # paddle movement
        # TODO
        paddleMove(paddle)

        # if paddle hits ball reverse ball direction
        # TODO
        if padHit(paddle, xBall, yBall) == True:
            yvelocity = -yvelocity
            

        # detect collision with bricks
        #for brick in bricks:
            # if ball collides with a brick, undraw the brick
            # remove the brick from the list (bricks.remove(brick))
            # reverse the yvelocity
            # decrease the number of bricks by 1
            # increase the score by 1
            # update the scoreboard
            # if no more brickes left you win!
            # TODO
        for brick in bricks:
            if checkCollision(brick, yBall, xBall) == True:
                brick.undraw()
                bricks.remove(brick)
                yvelocity = -yvelocity
                score +=1
                updateScoreboard(label, score)
                if bricks == 0:
                    youWin(label)



    # wait for click before exiting
    win.getMouse()
    win.close()

    # all done!
    exit(0)

def initBricks():
    color= ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE"]

    for i in range (ROWS):
        for j in range (COLS):
            x = j * (BRKWDTH + 5) + 2
            y = i * (BRKHT + 5) + 2
            rect = Rectangle(Point(x, y), Point(x + BRKWDTH, y + BRKHT))
            rect.setFill(color[i])
            rect.draw(win)
            bricks.append(rect)



# instantiate paddle as a rectangle object, in bottom middle of window
def initPaddle():
    p1 = Point(WIDTH* 3/8,540)
    p2 = Point(WIDTH * 5/8, 550)
    paddle = Rectangle(p1,p2)
    paddle.setFill('black')
    paddle.draw(win)
    return paddle

# instantiate ball as a circle in center of window below the scoreboard
def initBall():
    RADIUS = 12
    color = "purple"
    center = Point(WIDTH/2, HEIGHT/1.5)
    ball = Circle(center, RADIUS)
    ball.setFill(color)
    ball.draw(win)
    return ball

# if ball touches left or right side of window, return True, else return False
def checkSides(xBall):
    centerBall = ball.getCenter()
    xBall = centerBall.getX()
    yBall = centerBall.getY()
    if xBall <= 12:
        return True  
    if xBall >= WIDTH - 12:
        return True
    return False

def paddleMove(paddle):
    user_event = win.checkKey()
    padPt = paddle.getP1()
    padX = padPt.getX()
    if user_event == "Left" and padX > 0:
        paddle.move(-20, 0)
    elif user_event == "Right" and padX + PADWIDTH < WIDTH:
        paddle.move(20, 0)

def padHit(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def initLives():
    anchorpoint = Point(80, HEIGHT - 20)
    livesText = Text(anchorpoint, "Lives Remaining: " + str(LIVES))
    livesText.draw(win)
    return livesText

def updateLives(livesText, lives):
    livesText.setText("Lives Remaining: " + str(lives))
    return livesText

def initScoreboard():
    x = WIDTH / 2
    y = HEIGHT / 2
    anchorPoint = Point(x, y)
    label = Text(anchorPoint, "0")
    label.setSize(36)
    label.setTextColor("Dark Gray")
    label.draw(win)
    return label

def checkCollision(brick, yBall, xBall):
    brickCorner = brick.getP2()
    xBrick = brickCorner.getX()
    yBrick = brickCorner.getY()
    if yBall - yBrick < 5 and xBall > (xBrick - BRKWDTH) and xBall < xBrick :
        return True
    else:
        return False

def updateScoreboard(label, score):
    label.setText(score)
    return label

def gameOver(label):
    updateScoreboard(label, "You Lose!")
    time.sleep(4)
    exit(0)

def youWin(label):
    updateScoreboard(label, "You Win!")
    time.sleep(4)
    exit(0)



if __name__ == "__main__":
    main()
