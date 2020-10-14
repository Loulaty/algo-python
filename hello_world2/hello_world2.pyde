ballX = 0
ballY = 0
ballXspeed = 3
ballYspeed = 5
ballradius = 5

racketX = 0
racketY = 0
racketW = 50
racketH = 20

def setup():
    global ballX, ballY, racketX, racketY
    size(400, 400)
    clear()
    frameRate(60)   
    ballX = width/2
    ballY = height/2
    racketX = mouseX - 25
    racketY = height - 50
    
def draw():
    clear()
    drawRacket()
    drawBall()  
    
def drawRacket():
    global racketW, racketX, racketY
    fill (255)
    racketX = mouseX - (racketW/2)
    racketY = height - 20
    rect(racketX, racketY, racketW, 10)
    
def drawBall():
    global ballX, ballY, ballXspeed, ballYspeed, racketW, racketY, racketX, racketH
    circle(ballX, ballY, 10)
    
    ballX += ballXspeed
    ballY += ballYspeed
    
    #droite
    if(ballX > width) :
        ballXspeed *= -1
        ballX = width-ballradius
    #gauche
    elif(ballY < 0) :
        ballYspeed *= -1
        ballY = ballradius
    #haut
    if(ballX < 0) :
        ballXspeed *= -1
        ballX = ballradius
    #bas
    elif(ballY > height) :
        ballYspeed *= -1
        ballY = height-ballradius
        
    if(racketY < ballY+ballradius < racketY +racketH and ballYspeed > 0) :
        if(racketX < ballX < racketX + racketW) :
            ballYspeed *= -1
            ballY = racketY-ballradius



        
    
