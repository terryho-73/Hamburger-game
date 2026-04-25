def setup():
    global stage
    global totalNum, ing, top
    global ingX,ingY,w,h,dy
    global me, BK,playerW,playerH
    global topX, topY
    global info
    global playerX, playerY
    global caught, score, startTime, limitingredient
    global bomb, bombW, bombH,bombX,bombY
    global droppedIng
    global finalframe
    global boom, startTime, timelimit,playB,twiceScore
    global playBw,playBh,playBX,playBY
    global TSw,TSh,TSx,TSy,TStimelimit,TSdrop,TSmode,Star,TSstart, ingscore, meatscore, img0

    size(450,750)
    smooth()
    # 0 for homepage, 1 for gameplay, 2 for gameover1, 3 for gameover2
    stage = 0
    totalNum=5
    playerW=120
    playerH=60
    topX=random(0,width-playerW)
    topY=random(-300,0)
    bombW=95
    bombH=95
    bombX=random(0,width-bombW)
    bombY=random(-600,0)
    
    ing=[]
    ingX=[]
    ingY=[]
    dy=[]
    caught = []
    limitingredient=2
    droppedIng=[]
    finalframe = None
    
    top=loadImage("buns1.png")
    me = loadImage("buns2.png")
    BK = loadImage("background.png")
    bomb = loadImage("bomb2.png")
    boom = loadImage("explode.png")
    twiceScore = loadImage("bubble.png")
    playB = loadImage("playButton.png")
    Star = loadImage("star.png")
    img0 = loadImage("ing0.png")
    playBw=100
    playBh=100
    playBX=width/2-playBw/2
    playBY=height/2-playBh/2
    TSw=100 #TS stands for twice score 
    TSh=100
    TSx=random(0,width-TSw)
    TSy=random(-15000,-1000)
    TStimelimit= 0
    TSmode = False
    TSstart = 0
    ingscore = 1
    meatscore = 2

    w=100
    h=45
    info=False
    score = 0
    playerX = width/2-playerW/2
    playerY = 680
    startTime = 0
    timelimit = 120
    
    for i in range(0,limitingredient):
            ing.append(loadImage("ing"+str(i)+".png"))
            droppedIng.append(i)
            ingX.append(random(0,width-w))
            ingY.append(random(-300,100))
            dy.append(random(3,6))
        
def draw():
    global w,h,ingY,info,stage
    image(BK,0,0,width,height)
    
    if stage==0:
        if info == True:
            information()
        else:
            homepage()
        
    elif stage == 1:
        gameplay()
        
    elif stage == 2:
        youwin()
        
    elif stage == 3:
        youlose1()
        
    elif stage == 4:
        youlose2()
        
def gameplay():
    global w,h,ingY,count,topX,topY,playerX,playerY,caught,stacking,score,ing,stage,bombY,bombX,droppedIng
    global finalframe,startTime,timelimit,TSmode, TStimelimit, TSstart
    global TSy
    image(BK,0,0,width,height)
    fill(255)
    rect(0,0,370,125)
    stacking = len(caught)*10
    
    fill(1,100,32)
    current_time=(millis()-startTime)/1000
    countdown = timelimit- current_time
    text("Time Remained: " + str(countdown) + "s" ,20,50)                    
    text("Score: " + str(score), 20,100)
    
    if TSmode ==True:
        TStimelimit = 20
        TSTimePass = (millis()-TSstart)/1000
        TStime=TStimelimit-TSTimePass
        fill(255)
        rect(0,0,370,165)
        fill(1,100,32)
        text("Time Remained: " + str(countdown) + "s" ,20,50)                    
        text("Score: " + str(score), 20,100)
        fill(0,0,255)
        text("2x Score: " + str(TStime) +"s",20,150)
        image(Star,250,120,20,20)
        
        if (TStime < 0):
            TSmode = False #twice Score mode off after countdown reach 0
    
    caughtY = playerY - 10
    
    if topY>=1400:
        topX=random(0,width-playerW)
        topY=-50
        
    if bombY>=900:
        bombX=random(0,width-bombW)
        bombY=-50
    
    if mousePressed==True:
        playerX=mouseX-playerW/2

    rare_index = 0
    meat_prob = 0.05
    for i in range(len(ing)):
        image(ing[i],ingX[i],ingY[i],w,h)
        ingY[i]+=dy[i]
        if mousePressed == True and (TSy+TSh>=playerY-stacking) and (TSx+TSw>=mouseX-playerW/2) and (TSx<mouseX + playerW/2) and (TSy<=playerY-stacking+10):
            TSy = random(-40000,-10000)
            TSstart = millis()
            TSmode = True #twice score mode on

        elif mousePressed == True and (topY+10>=playerY-stacking) and (topX+playerW>mouseX-playerW/6) and (topX<mouseX + playerW/6) and (topY<=playerY-stacking+10):
            topX=1999
            caught.append("top")
            
        elif (bombY+bombH-25>=playerY-stacking-10) and (bombX+bombW>mouseX-playerW/3) and (bombX<mouseX + playerW/3) and (bombY<=playerY-stacking+10): #when bomb is caught
            bombX=1999
            caught.append("bomb")
            
        else:        
            if mousePressed == True and (ingY[i]+10>=playerY-stacking) and (ingX[i]+w>mouseX-playerW/6) and (ingX[i]<mouseX + playerW/6) and (ingY[i]<=playerY-stacking+10):
                caught.append(ing[i])
                if droppedIng[i]==0:
                    score+=meatscore*2 if TSmode==True else meatscore
                    
                else:
                    score+=ingscore*2 if TSmode==True else ingscore
                
                if random(1) <= meat_prob:
                    ing[i] = loadImage("ing"+str(0)+".png")
                    droppedIng[i] = 0
                    
                else:
                    newIng= int(random(1, totalNum))
                    ing[i] = loadImage("ing" + str(newIng) + ".png")
                    droppedIng[i]=newIng
                ingY[i] = random(-300,-100)
                ingX[i] = random(0,width-w)
                dy[i]=random(4,7)
                    
            #refresh
            if (ingY[i]>height):
                if random(1) <= meat_prob:
                    ing[i] = loadImage("ing"+str(0)+".png")
                    droppedIng[i] = 0
                    
                else:
                    newIng= int(random(1, totalNum))
                    ing[i] = loadImage("ing" + str(newIng) + ".png")
                    droppedIng[i]=newIng
                ingY[i] = random(-300,-100)
                ingX[i] = random(0,width-w)
                dy[i]=random(4,7)
                
    image(top,topX,topY,playerW,playerH)
    topY+=2
    image(bomb,bombX,bombY,bombW,bombH)
    bombY+=4
    image(twiceScore,TSx,TSy,TSw,TSh)
    TSy+=random(4,9)
    image(me,playerX,playerY,playerW,playerH)
                        
    for caught_item in caught:
        if caught_item == "top":
            image(top,playerX,caughtY-10, playerW,playerH)
            finalframe = get(0,0,width,height)
            stage = 2
            
        elif caught_item == "bomb":
            image(boom,playerX-15,caughtY-bombH/1.7,150,150)
            finalframe = get(0,0,width,height)
            stage = 3
        else:
            image(caught_item, playerX+9, caughtY, w, h)
        caughtY -= 10  
        
    if stacking >= 270:
        playerY = 680 + (stacking / 5)  
    else:
        playerY = 680  
            
    if (countdown< 0):
        finalframe = get(0,0,width,height)
        stage = 4
        
def homepage():
    global stage
    noStroke()
    fill(255)
    rect(0,0,450,260)
    fill(0)
    textSize(32)
    text("Welcome! Click 's' or the \nstart button to start the \ngame. \nPress 'i' to display the \ngame rules.",20,50)
    image(playB,playBX,playBY,playBw,playBh)
    stroke(0)
    strokeWeight(2)
    
def information():
    fill(255)
    rect(0,0,450,560)
    fill(0)
    textSize(20)
    text("Instructions: \nYou have the bottom of the burger, catch\
          \nas many ingredients as possible to get \nhigher score in the time limit.\
           \n\nRemember to catch the top of the burger \nto finish the game. Otherwise, you will fail.\
           \n\nYou can always restart by clicking 'r' or \nexit by clicking 'e'.",20,50)
    image(bomb,20,360,50,50)
    fill(255,0,0)
    text(": pay attention to them!!!",70,395)
    image(twiceScore,20,420,40,40)
    fill(1,50,32)
    text(": catch it to get temporary twice score\n bonus!",70,445)
    image(img0,20,505,40,20)
    text(": other ingredients = 2:1\n(score awarded when caught)",70,520)

def keyPressed():
    global info, stage, startTime
    if (stage==0):
        if key == "i" or key =="I":
            info = True
        if key =="s" or key=="S":
            stage=1
            startTime = millis()
    if(stage==0) or (stage==1) or (stage==2) or (stage==3) or (stage==4):
        if key == "r" or key == "R":
            setup()
        elif key == "e" or key =="E":
            exit()
        
def keyReleased():
    global info
    if key == "i" or key== "I" and stage==0:
        info = False
        
def mousePressed():
    global stage, startTime
    if (stage==0) and info==False:
        if mouseX >= playBX and mouseX <playBX+playBw and \
           mouseY >= playBh and mouseY <playBY+playBh:
               stage = 1
               startTime = millis()
               
    if (stage==2) or (stage==3):
        if mouseX>=165 and mouseX<165+120 and\
           mouseY>=300 and mouseX<300+60:
               setup()
               
    if (stage==4):
        if mouseX>=165 and mouseX<165+120 and\
           mouseY>=200 and mouseY<=200+70:
               setup()

def youlose1():
    global stage, finalframe,bombY
    image(finalframe,0,0)
    fill(255,255,0)
    rect(10,30,430,350)
    fill(255,0,0)
    textSize(25)
    text("Oh no! You catch a bomb!!! \nClick 'r' to start a new game.",50,130)
    RestartButton(165,300)
    
def youlose2():
    global stage, finalframe
    image(finalframe,0,0)
    fill(255,255,0)
    rect(10,30,430,250)
    fill(255,0,0)
    textSize(25)
    text("You run out of time!",100,130)
    RestartButton(165,200)
    
def youwin():
    global stage,topY
    image(finalframe,0,0)
    fill(255,255,0)
    rect(40,150,370,230)
    rect(40,500,370,80)
    fill(1,100,56)
    textSize(25)
    text("Congratulation! You Win!\nClick 'r' to restart.",70,200)
    fill(0)
    textSize(45)
    text("Your Score: "+ str(score),70,560)
    fill(0,255,0)
    RestartButton(165,300)
    
def RestartButton(rectX,rectY):
    fill(0,255,0)
    stroke(0)
    strokeWeight(2)
    rect(rectX, rectY, 120, 70)
    fill(0)
    textSize(32)
    text("Restart",rectX+5,rectY+45)
    

    
    
        
        

    

    

    
               

    
