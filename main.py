#Game created for grade 10 Computer Science Summative
#By: Susan Chen, Ashley Yim, and Lauryn Seto
#For: ICS2O1, Ms. Valin
import pygame
from pygame import *
import random

#These are the settings of the game
pygame.init()
timecounter = 0
x = 40
timearray = [1500,1450,1400,1350,1300,1250,1200,1150,1100,1050,1000,950,900,850,800,750,700,650,600,550,500]
time = timearray[timecounter]
pygame.time.set_timer(USEREVENT+1, 10)
pygame.mouse.set_visible(False)
myfont = pygame.font.SysFont("monospace", 15)
gamefont = pygame.font.SysFont("monospace", 24)
h = 300
w = 400
red = (255,0,0)
yellow = (255,255,0)
white = (255,255,255)
blue = (0,255,255)
gamename = ("            Cavern Escaper           ")
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption(gamename)
clock = pygame.time.Clock()
playername = ""

#variables that we manipulate
mainloop = True
startmenu = True
health = 5
rand = True
rand2 = 1
inputTrue = False
counter = 0
challenge = False
questionnumber = 0
showquestion = False
questiontrue = False
showintro = False
showinstruct = False
showintro2 = False
showinstruct2 = False
level2 = False
levelcount = 1
challengecounter = 0
levelcounter = 5
highscoremenu = False
highscoretext = False

#textbrick gui
intro = [" You enter a mysterious door, seeking ","       for adventure. You have        ","  been transported into a dark cave,  ","     where you hear a loud snore.     "," The snore comes from a monster, which","   awakes to your arrival. You are    ","   now being chased by the monster    ","       and you have a total of        "," 10 health points. Your mission is to ","   survive and escape successfully.   ","    Otherwise, you will be caught     ","    by the monster and you cannot     ","             return home.             "]
instruct = ["       When the screen displays       ","      a yellow 'A' or a red 'B',      ","      press the left arrow key.       ","      When the screen displays a      ","       red 'A' or a yellow 'B',       ","      press the right arrow key.      ","       For every mistake made,        ","    one health point will be lost.    ","         After 5 challenges,          ","       one question will pop up       ","   as an opportunity to regain your   ","     health points. If you answer     "," correctly,you gain one health point. ","      If you answer incorrectly,      ","      you lose one health point.       "]
level2trans = ["      The monster angered further     ","       by your continued escape,      ","now he chases you with a faster speed.","  If you wish to escape, run faster!  "]
endgametrans = ["You see the cavern exit just up ahead.","        You rush towards it and       ","     as you jump out of the cave,     ","  the monster growls and walks back.  ","          You are now safe.           "]

#output gui: text that will be displayed
gameovergui = myfont.render("              Game Over!              ", 1, (white))
retrygui = myfont.render("       Retry?    -   Press Space      ", 1, (blue))
startinstruct = myfont.render("    Instruction    -   Press Enter   ",1,(blue))
gamestartgui = myfont.render("       Start    -   Press Space       ", 1, (blue))
gamenamegui = myfont.render(gamename, 1, (white))
highscoregui = gamefont.render("PREVIOUS SCORES",1,(blue))

#question gui
questionquestion = ["      Green is a primary colour.      ","The quadratic function is y=ax^2+bx+c.","       Lithium is a noble gas.       ","   Leonardo da Vinci was a pianist.   ","    Shakespeare wrote The Tempest.    ","        A cell has a nucleus.        ","  Hitler was killed by an atomic bomb ","    Convex mirrors curves inwards.    ","  Human eyes can not see ultraviolet. ","                 1+1=2                ","     Antarctica is the south pole     ","          Spiders have 6 legs         ","          Herbivores eat meat         ","          Sharks are mammals          ","      XC stands for cross-country     ","      Batman's name is Tony Stark     ","       Blue Jays is from Toronto      ","  Similar triangles have same angles  "," Refraction is the dispersion of light","         NaCl is salt chloride        "]
questiongui = myfont.render("       Press Space to continue        ",1,(blue))
showquestiongui = myfont.render("Press Left for False, Right for True",1,(white))
blitquestion = myfont.render(questionquestion[0],1,(white))

#left or right text display
A = ("A")
B = ("B")
leftA = gamefont.render(A, 1, (red))
rightA = gamefont.render(A, 1, (yellow))
leftB = gamefont.render(B, 1, (yellow))
rightB = gamefont.render(B, 1, (red))


#The loop that the game runs on
while mainloop:

    scoregui = myfont.render(("            Your Score: "+str(health)+"            "),1,(white))

    Left = True
    Right = False
    screen.fill((0,0,0)) #background
    clock.tick(20) #fps
    timetext = "Time: " + str(time)
    timergui = myfont.render(timetext,1,(white))

    #output: start menu, gameover menu, and health
    Text = ("Health: " + str(health)) #health display
    if highscoretext == True:
        playergui = myfont.render(("Name:"+playername),1,(white))
        screen.blit(playergui,(x+75,200))
    if inputTrue == True and startmenu == False and challenge == False and health > 0:
        screen.blit(timergui, (300,10))
    if inputTrue == False and startmenu == True and challenge == False:
        screen.blit(gamestartgui,(x, 140))
        screen.blit(gamenamegui, (x, 90))
        screen.blit(startinstruct, (x, 190))
    elif health <= 0:
        screen.blit(gameovergui, (x, 100))
        screen.blit(retrygui, (x, 150))
        counter = 0
        timecounter = 0
        questionnumber = 0
        time = timearray[timecounter]
        inputTrue = False
    elif health >= 1 and startmenu == False and inputTrue == True and challenge == False:
        label = myfont.render(Text, 1, (white))
        screen.blit(label, (10, 10))
    elif challenge == True and startmenu == False:
        screen.blit(showquestiongui, (x,100))
        screen.blit(questiongui, (x,150))
    if showintro == True:
        startmenu = False
        for i in range (0,9):
            introtext = myfont.render(intro[i],1,(white))
            screen.blit(introtext,(x,50+i*20))
        screen.blit(questiongui,(x,280))
    if showinstruct == True:
        startmenu = False
        for i in range (0,9):
            instructtext = myfont.render(instruct[i],1,(white))
            screen.blit(instructtext,(x,50+i*20))
        screen.blit(questiongui,(x,280))
    if showintro2 == True:
        startmenu = False
        for i in range (9,13):
            introtext = myfont.render(intro[i],1,(white))
            screen.blit(introtext,(x,70+(i-9)*20))
        screen.blit(questiongui,(x,280))
    if showinstruct2 == True:
        startmenu = False
        for i in range (9,15):
            instructtext = myfont.render(instruct[i],1,(white))
            screen.blit(instructtext,(x,70+(i-9)*20))
        screen.blit(questiongui,(x,280))

    #level2
    if level2 == True and levelcounter == 5:
        for i in range (0,4):
            level2transtext = myfont.render(level2trans[i],1,(white))
            screen.blit(level2transtext,(x,50+i*20))
        screen.blit(questiongui,(x,280))

    if level2 == True and levelcounter == 6 and levelcount == 2:
        highscoretext = True
        for i in range (0,4):
            endgametext = myfont.render(endgametrans[i],1,(white))
            screen.blit(endgametext,(x,50+i*20))
        screen.blit(questiongui,(x,280))
        screen.blit(scoregui, (x,150))

    #left or right? system: determines which key to press
    if rand == True and inputTrue == True:
        randnumber = random.randint(1,4)
        if randnumber == 1:
            rand2 = 1
            rand = False
        elif randnumber == 2:
            rand2 = 2
            rand = False
        elif randnumber == 3:
            rand2 = 3
            rand = False
        elif randnumber == 4:
            rand2 = 4
            rand = False
    if rand2 == 1 and inputTrue == True:
        Left = False
        Right = True
        screen.blit(leftA, (w/2 - 5,h/2 - 5)) #a red A
    elif rand2 == 2 and inputTrue == True:
        Left = True
        Right = False
        screen.blit(rightA, (w/2 - 5,h/2 - 5)) # a green A
    elif rand2 == 3 and inputTrue == True:
        Left = False
        Right = True
        screen.blit(leftB, (w/2 - 5,h/2 - 5)) # a green B
    elif rand2 == 4 and inputTrue == True:
        Left = True
        Right = False
        screen.blit(rightB, (w/2 - 5,h/2 - 5)) # a red B

    #questions
    if questionnumber == 0 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))
    elif questionnumber == 1 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))
    elif questionnumber == 2 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))
    elif questionnumber == 3 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 4 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        timecounter = questionnumber+1
        Right = True
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 5 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 6 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 7 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 8 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 9 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 10 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 11 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 12 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 13 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 14 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 15 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 16 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 17 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = False
        Right = True
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 18 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        timecounter = questionnumber+1
        screen.blit(blitquestion,(x,100))

    elif questionnumber == 19 and questiontrue == True:
        blitquestion = myfont.render(questionquestion[questionnumber],1,(white))
        Left = True
        Right = False
        screen.blit(blitquestion,(x,100))

    if time <= 0:
        health -= 1
        time = timearray[timecounter]

    #input: left/right keys, restart/next level key
    for event in pygame.event.get():
        if event.type == USEREVENT+1 and inputTrue == True and startmenu == False and challenge == False and health > 0:
            time -= 1
        if inputTrue == True or questiontrue == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and Left == True:
                if inputTrue == True:
                    rand = True
                    counter += 1
                elif questiontrue == True:
                    health += 2
                    questionnumber += 1
                    inputTrue = True
                    startmenu = False
                    rand = True
                    questiontrue = False
                    showquestion = False
                    challengecounter += 1
                    time = timearray[timecounter]
                elif levelcounter == 6 and counter == 2:
                    levelcount = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and Left == True:
                if inputTrue == True:
                    health -= 1
                    rand = True
                elif questiontrue == True:
                    inputTrue = True
                    startmenu = False
                    rand = True
                    questiontrue = False
                    showquestion = False
                    questionnumber += 1
                    challengecounter += 1
                    time = timearray[timecounter]
                elif levelcounter == 6 and counter == 2:
                    levelcount = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and Right == True:
                if inputTrue == True:
                    counter += 1
                    rand = True
                elif questiontrue == True:
                    health += 2
                    inputTrue = True
                    startmenu = False
                    rand = True
                    questiontrue = False
                    questionnumber += 1
                    challengecounter += 1
                    time = timearray[timecounter]
                    showquestion = False
                elif levelcounter == 6 and counter == 2:
                    levelcount = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and Right == True:
                if inputTrue == True:
                    health -= 1
                    rand = True
                elif questiontrue == True:
                    inputTrue = True
                    startmenu = False
                    rand = True
                    time = timearray[timecounter]
                    questionnumber += 1
                    questiontrue = False
                    showquestion = False
                    challengecounter += 1
                elif levelcounter == 6 and counter == 2:
                    levelcount = 2

        if challengecounter == 9 or event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            challengecounter = 9
            level2 = True
            challenge = False
            inputTrue = False
            rand = False
            startmenu = False
            showquestion = False
            questiontrue = False
            counter = 0
            if event.type == pygame.KEYDOWN and event.key >= 65 and event.key <= 122:
                playername += chr(event.key)

        if counter == levelcounter:
            inputTrue = False
            rand = False
            challenge = True
            startmenu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and level2 == False:
                counter = 0
                challenge = False
                inputTrue = False
                rand = False
                startmenu = False
                showquestion = True
                questiontrue = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and inputTrue == False and challenge == False and questiontrue == False and showintro == False and showintro2 == False and showinstruct == False and showinstruct2 == False and health > 0 and level2 == False:
            showintro = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and inputTrue == False and challenge == False and questiontrue == False and showintro == True and showinstruct == False and showinstruct2 == False and level2 == False:
            showintro = False
            showintro2 = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and highscoremenu == False and inputTrue == False and challenge == False and questiontrue == False and startmenu == True:
            showinstruct = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and showinstruct == True and startmenu == False and showintro == False and showintro2 == False:
            showinstruct = False
            showinstruct2 = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and showinstruct2 == True and startmenu == False and showintro == False and showintro2 == False:
            showinstruct2 = False
            startmenu = True

        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and inputTrue == False and challenge == False and questiontrue == False and showintro == False and showintro2 == True and showinstruct == False and showinstruct2 == False) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and inputTrue == False and challenge == False and questiontrue == False and health == 0):
            health = 5
            inputTrue = True
            startmenu = False
            rand = True
            showintro2 = False
            counter = 0
            levelcounter = 5
            levelcount = 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and highscoremenu == False and inputTrue == False and challenge == False and questiontrue == False and rand == False and level2 == True and levelcounter == 5 and challengecounter == 9 and levelcount == 1:
            inputTrue = True
            rand = True
            level2 = False
            startmenu = False
            counter = 0
            levelcounter = 6
            levelcount = 2
            challengecounter = 0

        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and inputTrue == False and challenge == False and questiontrue == False and rand == False and level2 == True and levelcounter == 6 and challengecounter == 9 and levelcount == 2):
            counter = 0
            file = open('highscore.txt','r')
            challengecounter = 0
            highscoremenu = True
            level2 = False
            levelcounter = 5
            levelcount = 1
            highscoretext = False

            playerlen = len(playername)
            filearray = file.readlines()
            del filearray[0:1]
            file.close()
            file=open("highscore.txt",'w')
            file.writelines(filearray)
            file.write(playername+"         "+str(health)+"\n")
            file.close()
            file=open("highscore.txt",'r')
            filearray = file.readlines()
            for i in range (0,len(filearray)):
                if filearray[i].endswith('\n'):
                    filearray[i] = (filearray[i])[:-1]
            file.close()


        elif highscoremenu == True and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            highscoremenu = False
            startmenu = True
    #highscoremenu
        if highscoremenu == True and startmenu == False:
            for i in range (7,len(filearray)):
                highscorestext = myfont.render(filearray[i],1,(white))
                screen.blit(highscorestext,(x,45 + (i-7)*20))
            yourscore = myfont.render("Your Score:"+str(health),1,(yellow))
            screen.blit(questiongui,(x,280))
            screen.blit(highscoregui,(50,10))
            screen.blit(yourscore, (x,250))

        if event.type == pygame.QUIT:
            mainloop = False
    pygame.display.flip()
pygame.quit()
quit()