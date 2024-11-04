##Developed by DEVICHARAN

import threading
import random
import pygame 
import time
import math
import sys
import os


#Reiterating recursion depth limit
sys.setrecursionlimit(1000000000)


#Positioning the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(225,100)
pygame.init()


#-----------------------------------------------General Variables-----------------------------------------
#RESOLUTIONS FOR OPENING SCREEN AND ITS EXTENSION
res1 = (400,600)
res2=(1200,600)

#Switch Variables
SwitchMain=True
SwitchOne=False
SwitchTwo=False
SwitchThree=False

#COLORS
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
brown=(150,75,0)
blue=(0,191,255)
yellow=(255,255,0)
green=(0,255,0)
orange=(255,95,31)

#------------FIRST SCREEN INPUTS--------------------
InputNumberOfRows = '' 
InputNumberOfColumns = ''
status_start=[False,False]
status_goal=[False,False]
status_search=[False,False]
#-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------General Settings-----------------------------------------
#FPS SETTINGS
clock=pygame.time.Clock()
clock.tick(120)

#DEFINING A FONT
smallsmallsmallfont = pygame.font.SysFont('consolas',12)
smallsmallfont = pygame.font.SysFont('consolas',18)
smallfont = pygame.font.SysFont('consolas',20)
bigfont = pygame.font.SysFont('consolas',35)
bigbigfont = pygame.font.SysFont('consolas',55)
base_font = pygame.font.Font(None, 70)
bigbigfont = pygame.font.SysFont('consolas',80)
bigbigbigfont = pygame.font.SysFont('consolas',100)


#----------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------FIRST SCREEN----------------------------------------------------------------------
#------------FIRST SCREEN ELEMENTS-------------------------
#BACKGROUND IMAGES
bg_image1 = pygame.image.load('RED.png')
bg_image2=pygame.image.load('BLUE.png')


#ERROR ELEMENTS
Error0='ERROR -> NO ERROR'
Error1='ERROR -> ENTER VALID NUMBER IN GIVEN RANGE'
Error2='ERROR -> ENTER A NUMBER, NOT A STRING'
Error3='ERROR -> CHOOSE A START OPTION'
Error4='ERROR -> CHOOSE A GOAL OPTION'
Error5='ERROR -> CHOOSE A SEARCH OPTION'


#BUTTON LABELS
textError=smallfont.render(Error0, True , white)
text1 = bigfont.render('START' , True , white)
text2 = bigfont.render('QUIT' , True , white)
text3_1 = smallfont.render('Single', True , white)
text3_2 = smallfont.render('start', True , white)
text3_3 = smallfont.render('point', True , white)
text4_1 = smallfont.render('Single' , True , white)
text4_2 = smallfont.render('goal' , True , white)
text4_3 = smallfont.render('point' , True , white)
text5_1 = smallfont.render('Blind' , True , white)
text5_2 = smallfont.render('search' , True , white)
text6_1 = smallfont.render('Multiple' , True , white)
text6_2 = smallfont.render('start' , True , white)
text6_3 = smallfont.render('points' , True , white)
text7_1 = smallfont.render('Multiple' , True , white)
text7_2 = smallfont.render('goal' , True , white)
text7_3 = smallfont.render('points' , True , white)
text8_1 = smallfont.render('UnBlind' , True , white)
text8_2 = smallfont.render('search' , True , white)
text9_1 = smallfont.render('min=2,max=40' , True , white)
text9_2 = smallfont.render('min=2,max=40' , True , white)
text10 = base_font.render('START THE GAME' , True , black)

#---------------------------------------------------------------------------
#------------FIRST SCREEN FUNCTIONING--------------------
def FirstScreen():
    global SwitchMain
    global SwitchOne
    global screen
    global InputNumberOfRows 
    global InputNumberOfColumns 
    global status_start
    global status_goal
    global status_search

    #SCREEN INITIATION
    screen = pygame.display.set_mode(res1)
    width = screen.get_width() 
    height = screen.get_height()
    pygame.display.set_caption('Track Trek.IO')


    runningFirstScreen=True
    while runningFirstScreen:
        mouse = pygame.mouse.get_pos()
        mx,my=pygame.mouse.get_pos()

        for ev in pygame.event.get():
            
            #To quit the screen
            if ev.type == pygame.QUIT:
                pygame.quit()

            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                #If mouse clicks on Start Button
                if 100 <= mouse[0] <= 300 and 100 <= mouse[1] <= 200:
                    
                    #Extend the screen size and update its background image
                    screen = pygame.display.set_mode(res2)
                    screen.blit(bg_image2, (400, 0))
                    
                    #Extended screen's buttons
                    ##single start point button
                    pygame.draw.rect(screen,black,[480,55,145,60])
                    screen.blit(text3_1 , (520,60))
                    screen.blit(text3_2 , (525,75))
                    screen.blit(text3_3 , (525,90))
                    ##single goal point button
                    pygame.draw.rect(screen,black,[715,55,145,60])
                    screen.blit(text4_1 , (755,60))
                    screen.blit(text4_2 , (765,75))
                    screen.blit(text4_3 , (760,90))
                    ##blind search button
                    pygame.draw.rect(screen,black,[930,55,145,60])
                    screen.blit(text5_1 , (970,65))
                    screen.blit(text5_2 , (970,85))
                    ##multiple start point button
                    pygame.draw.rect(screen,black,[480,230,145,60])
                    screen.blit(text6_1 , (510,235))
                    screen.blit(text6_2 , (525,250))
                    screen.blit(text6_3 , (520,265))
                    ##multiple goal points button
                    pygame.draw.rect(screen,black,[705,230,145,60])
                    screen.blit(text7_1 , (740,235))
                    screen.blit(text7_2 , (755,250))
                    screen.blit(text7_3 , (745,265))
                    ##unblind search button
                    pygame.draw.rect(screen,black,[930,230,145,60])
                    screen.blit(text8_1 , (965,240))
                    screen.blit(text8_2 , (970,260))
                    ##input for number of rows
                    pygame.draw.rect(screen,black,[605,385,145,60])
                    screen.blit(text9_1 , (610,450))
                    ##input for number of columns
                    pygame.draw.rect(screen,black,[805,385,145,60])
                    screen.blit(text9_1 , (810,450))
                    ##start the game button
                    pygame.draw.rect(screen,yellow,[480,500,600,60])
                    screen.blit(text10 , (570,510))

            
                #If mouse clicks on Quit Button
                if 100 <= mouse[0] <= 300 and 400 <= mouse[1] <= 500:
                    SwitchMain=False
                    pygame.quit()

                #if mouse clicks on Start Points Buttons
                if 480<mouse[0]<625 and 55<mouse[1]<105:
                    if status_start[0]==True:
                        status_start[0]=False
                    else:
                        status_start[0]=True
                        status_start[1]=False
                elif 480<mouse[0]<625 and 230<mouse[1]<290:
                    if status_start[1]==True:
                        status_start[1]=False
                    else:
                        status_start[1]=True
                        status_start[0]=False
                        if status_search[0]==True:
                            status_search[0]=False

                #if mouse clicks on Goal points Buttons
                if 715<mouse[0]<860 and 55<mouse[1]<105:
                    if status_goal[0]==True:
                        status_goal[0]=False
                    else:
                        status_goal[0]=True
                        status_goal[1]=False
                elif 705<mouse[0]<850 and 230<mouse[1]<290:
                    if status_goal[1]==True:
                        status_goal[1]=False
                    else:
                        status_goal[1]=True
                        status_goal[0]=False
                        if status_search[0]==True:
                            status_search[0]=False

                #if mouse clicks on List search Buttons
                if 930<mouse[0]<1075 and 55<mouse[1]<105:
                    if status_search[0]==True:
                        status_search[0]=False
                        status_search[1]=True
                    else:
                        status_search[0]=True
                        status_search[1]=False
                        if status_goal[1]==True:
                            status_goal[1]=False
                        status_goal[0]=True
                        if status_start[1]==True:
                            status_start[1]=False
                        status_start[0]=True
                elif 930<mouse[0]<1075 and 230<mouse[1]<290:
                    if status_search[1]==True:
                        status_search[1]=False
                    else:
                        status_search[1]=True
                        status_search[0]=False

                #if mouse clicks on START THE GAME Button
                if 480<mouse[0]<1080 and 500<mouse[1]<560:
                    if (status_start[0]==True or status_start[1]==True) and (status_goal[0]==True or status_goal[1]==True) and (status_search[0]==True or status_search[1]==True):
                        if InputNumberOfRows.isdigit()==True and InputNumberOfRows.isdigit()==True:
                            if (2<=int(InputNumberOfRows)<=40) and (2<=int(InputNumberOfColumns)<=40):
                                runningFirstScreen=False
                            else:
                                pygame.draw.rect(screen,black,[480,560,600,30])
                                textError=smallfont.render(Error1, True , white)
                                screen.blit(textError , (550,560))
                        else:
                            pygame.draw.rect(screen,black,[480,560,600,30])
                            textError=smallfont.render(Error2, True , white)
                            screen.blit(textError , (560,560))
                    else:
                        if (status_start[0]==True or status_start[1]==True)==True:
                            pass
                        else:
                            pygame.draw.rect(screen,black,[480,560,600,30])
                            textError=smallfont.render(Error3, True , white)
                            screen.blit(textError , (590,560))
                        if (status_goal[0]==True or status_goal[1]==True)==True:
                            pass
                        else:
                            pygame.draw.rect(screen,black,[480,560,600,30])
                            textError=smallfont.render(Error4, True , white)
                            screen.blit(textError , (590,560))
                        if (status_search[0]==True or status_search[1]==True)==True:
                            pass
                        else:
                            pygame.draw.rect(screen,black,[480,560,600,30])
                            textError=smallfont.render(Error5, True , white)
                            screen.blit(textError , (590,560))


            ###HOVERING MECHANISM###
            #if mouse is over first input box
            if 605<mx<750 and 385<my<445:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:
                        InputNumberOfRows = InputNumberOfRows[:-1]
                    else:
                        InputNumberOfRows += ev.unicode
        
            #if mouse is over second input box
            if 805<mx<950 and 385<my<445:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:
                        InputNumberOfColumns = InputNumberOfColumns[:-1]
                    else:
                        InputNumberOfColumns += ev.unicode


            #if mouse is over start the game button
            if 480<mx<1080 and 500<my<560:
                pygame.draw.rect(screen,green,[480,500,600,60])
                screen.blit(text10 , (570,510))
            else:
                pygame.draw.rect(screen,yellow,[480,500,600,60])
                screen.blit(text10 , (570,510))
                
        
        #Refresh the button colors
        if status_start[0]==True:
            pygame.draw.rect(screen,green,[480,55,145,60])
            screen.blit(text3_1 , (520,60))
            screen.blit(text3_2 , (525,75))
            screen.blit(text3_3 , (525,90))     
        else:
            pygame.draw.rect(screen,black,[480,55,145,60])
            screen.blit(text3_1 , (520,60))
            screen.blit(text3_2 , (525,75))
            screen.blit(text3_3 , (525,90))
                
        if status_start[1]==True:
            pygame.draw.rect(screen,green,[480,230,145,60])
            screen.blit(text6_1 , (510,235))
            screen.blit(text6_2 , (525,250))
            screen.blit(text6_3 , (520,265))
        else:
            pygame.draw.rect(screen,black,[480,230,145,60])
            screen.blit(text6_1 , (510,235))
            screen.blit(text6_2 , (525,250))
            screen.blit(text6_3 , (520,265))

        if status_goal[0]==True:
            pygame.draw.rect(screen,green,[715,55,145,60])
            screen.blit(text4_1 , (755,60))
            screen.blit(text4_2 , (765,75))
            screen.blit(text4_3 , (760,90))
        else:
            pygame.draw.rect(screen,black,[715,55,145,60])
            screen.blit(text4_1 , (755,60))
            screen.blit(text4_2 , (765,75))
            screen.blit(text4_3 , (760,90))

        if status_goal[1]==True:
            pygame.draw.rect(screen,green,[705,230,145,60])
            screen.blit(text7_1 , (740,235))
            screen.blit(text7_2 , (755,250))
            screen.blit(text7_3 , (745,265))
        else:
            pygame.draw.rect(screen,black,[705,230,145,60])
            screen.blit(text7_1 , (740,235))
            screen.blit(text7_2 , (755,250))
            screen.blit(text7_3 , (745,265))

        if status_search[0]==True:
            pygame.draw.rect(screen,green,[930,55,145,60])
            screen.blit(text5_1 , (970,65))
            screen.blit(text5_2 , (970,85))
        else:
            pygame.draw.rect(screen,black,[930,55,145,60])
            screen.blit(text5_1 , (970,65))
            screen.blit(text5_2 , (970,85))

        if status_search[1]==True:
            pygame.draw.rect(screen,green,[930,230,145,60])
            screen.blit(text8_1 , (965,240))
            screen.blit(text8_2 , (970,260))
        else:
            pygame.draw.rect(screen,black,[930,230,145,60])
            screen.blit(text8_1 , (965,240))
            screen.blit(text8_2 , (970,260))
        
                
        #BackGround
        screen.blit(bg_image1, (0, 0))

        #Start Button
        pygame.draw.rect(screen,black,[100,100,200,100])
        screen.blit(text1 , (150,130))

        #Quit Button
        pygame.draw.rect(screen,black,[100,400,200,100])
        screen.blit(text2 , (150,430))

        #Rows and Column Input reader
        pygame.draw.rect(screen, black, [605,385,145,60])
        text_surface = base_font.render(InputNumberOfRows, True, (255, 255, 255))
        screen.blit(text_surface, (655, 395))

        pygame.draw.rect(screen, black, [805,385,145,60])
        text_surface = base_font.render(InputNumberOfColumns, True, (255, 255, 255))
        screen.blit(text_surface, (855, 395))

        clock.tick(120)
        pygame.display.update()
        
    if runningFirstScreen==False:
        SwitchOne=True
#---------------------------------------------------------------------------
#-------------------------------------------------------------END OF FIRST SCREEN---------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------SECOND SCREEN------------------------------------------------------------
#-----------SECOND SCREEN ELEMENTS----------------------
#SCREEN DIMENSIONS
SCREEN_WIDTH=1200
SCREEN_HEIGHT=800

#STORAGE VARIABLES
NumberOfRows=0
NumberOfColumns=0
EachBlockWeight=0
EachBlockHeight=0
StartList=[]
GoalList=[]
ObsticleList=[]
MountainList=[]
WaterList=[]
MountainCost=""
WaterCost=""
GreenCost=""

#BACKGROUND IMAGES
bg_image3=pygame.image.load('BLACK.png')
bg_image4=pygame.image.load('BLACK_800x800.png')
bg_image5=pygame.image.load('GREEN_800x800.png')

#ERROR ELEMENTS
Error6='ERROR -> PLEASE SELECT A START POINT'
Error7='ERROR -> PLEASE SELECT A GOAL POINT'
Error8='ERROR -> ENTER APPROPRIATE MOUNTAIN COST'
Error9='ERROR -> ENTER APPROPRIATE WATER COST'
Error10='ERROR -> ENTER APPROPRIATE GREENARY COST'


#BUTTON LABELS
textErrortwo=smallfont.render(Error0, True , white)
textB1 = bigbigfont.render('LABELS ' , True , black)
textB1_1 = smallfont.render('OBSTICLE ' , True , black)
textB1_2 = smallfont.render('MOUNTAIN ' , True , black)
textB1_3 = smallfont.render('WATER' , True , black)
textB1_4 = smallfont.render('GREENARY ' , True , black)
textB1_5 = smallfont.render('START POINT ' , True , black)
textB1_6 = smallfont.render('GOAL POINT ' , True , black)
textB2 = bigbigfont.render('COSTS ' , True , black)
textB2_1 = smallfont.render('MOUNTAIN COST ' , True , white)
textB2_2 = smallfont.render('WATER COST ' , True , white)
textB2_3 = smallfont.render('GREENARY COST ' , True , white)
textB3 = bigbigbigfont.render('START ' , True , black)
textB4_1 = smallsmallsmallfont.render('ALL GREEN' , True , black)
textB4_2 = smallsmallsmallfont.render('ALL OBSTICLE ' , True , black)


#----------------------------------------------------------------------------

#------------SECOND SCREEN FUNCTIONING----------------5
def SecondScreen():
    global SwitchTwo
    global NumberOfRows
    global NumberOfColumns
    global EachBlockWeight
    global EachBlockHeight
    global MountainCost
    global WaterCost
    global GreenCost
    global StartList
    global GoalList
    global ObsticleList
    global MountainList
    global WaterList

    #SCREEN INITIATION
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
    pygame.display.set_caption('Track Trek.IO') 
    screen.fill(green)

    #SECTIONING OF SCREEN
    pygame.draw.line(screen, black, (800, 0), (800, 800), 10)
    pygame.display.update()

    #VARIABLES UPDATE
    NumberOfRows=int(InputNumberOfRows)
    NumberOfColumns=int(InputNumberOfColumns)
    EachBlockWeight=800//NumberOfRows
    EachBlockHeight=800//NumberOfColumns
    start_pointer=False
    goal_pointer=False
    obsticle_pointer=False
    mountain_pointer=False
    water_pointer=False
    green_pointer=False
    goal_pointer_numbering=1


    #Resizing the grid to avoid misplaced boxes
    if NumberOfRows >=10 and NumberOfColumns>=10:
        if NumberOfRows*EachBlockWeight>=800:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight-5
        else:
            if NumberOfRows%2==1:
                temp_width=NumberOfRows*EachBlockWeight-20
            else:
                temp_width=NumberOfRows*EachBlockWeight-5

            if NumberOfColumns%2==1:
                temp_height=NumberOfColumns*EachBlockHeight-5
            else:
                temp_height=NumberOfColumns*EachBlockHeight-5
    else:
        if NumberOfRows*EachBlockWeight>=800:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight
        else:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight

    #To draw the grid of boxes onto the screen
    def drawGrid(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight):
        for i in range(NumberOfRows):
            for j in range(NumberOfColumns):
                if (i*EachBlockWeight)<=SCREEN_WIDTH and (j*EachBlockHeight)<=SCREEN_HEIGHT:
                    rect = pygame.Rect(i*EachBlockWeight, j*EachBlockHeight,EachBlockWeight, EachBlockHeight)
                    pygame.draw.rect(screen, black, rect,1)

    #To draw the grid of obsticles onto the screen
    def drawGridForObsticle(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight):
        global list_
        for i in range(NumberOfRows):
            for j in range(NumberOfColumns):
                if (i*EachBlockWeight)<=SCREEN_WIDTH and (j*EachBlockHeight)<=SCREEN_HEIGHT:
                    rect = pygame.Rect(i*EachBlockWeight, j*EachBlockHeight,EachBlockWeight, EachBlockHeight)
                    pygame.draw.rect(screen, black, rect)
                    temp=[i*EachBlockWeight, j*EachBlockHeight]
                    ObsticleList.append(temp)


    #Background image
    screen.blit(bg_image3, (800, 0))  

    runningSecondScreen=True

    while runningSecondScreen:
        drawGrid(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
        mouse = pygame.mouse.get_pos()
        mx,my=pygame.mouse.get_pos()
        textgoalindex=smallfont.render(str(goal_pointer_numbering) , True , black)
        if len(GoalList)==0:
            goal_pointer_numbering=1


        for event in pygame.event.get():

            ###if left mouse button is clicked###
            if pygame.mouse.get_pressed()[0]:
                mx,my=pygame.mouse.get_pos()
                mpos_x=(mx//EachBlockWeight)*EachBlockWeight
                mpos_y=(my//EachBlockHeight)*EachBlockHeight

                #if we click on ALL GREEN Button
                if 805<=mouse[0]<=895 and 150<=mouse[1]<=170:
                    screen.blit(bg_image5, (0, 0))
                    StartList=[]
                    GoalList=[]
                    ObsticleList=[]
                    MountainList=[]
                    WaterList=[]
                    drawGrid(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)

                #if we click on ALL OBSTICLE Button
                if 805<=mouse[0]<=895 and 225<=mouse[1]<=245:
                    screen.blit(bg_image4, (0, 0))
                    drawGridForObsticle(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
                    StartList=[]
                    GoalList=[]
                    MountainList=[]
                    WaterList=[]
                    

                #If we click on Start Button
                if 800<=mouse[0]<=1200 and 720<=mouse[1]<=800:
                    if len(StartList)!=0 and len(GoalList)!=0:
                        if MountainCost.isdigit()==False:
                            textErrortwo=smallsmallfont.render(Error8, True , white)
                            pygame.draw.rect(screen,black,[800,700,400,30])
                            screen.blit(textErrortwo , (800,700))
                        elif WaterCost.isdigit()==False:
                            textErrortwo=smallsmallfont.render(Error9, True , white)
                            pygame.draw.rect(screen,black,[800,700,400,30])
                            screen.blit(textErrortwo , (800,700))
                        elif GreenCost.isdigit()==False:
                            textErrortwo=smallsmallfont.render(Error10, True , white)
                            pygame.draw.rect(screen,black,[800,700,400,30])
                            screen.blit(textErrortwo , (800,700))
                        else:
                            runningSecondScreen=False
                    else:
                        if len(StartList)==0:
                            textErrortwo=smallfont.render(Error6, True , white)
                            pygame.draw.rect(screen,black,[800,700,400,30])
                            screen.blit(textErrortwo , (800,700))
                        elif len(GoalList)==0:
                            textErrortwo=smallfont.render(Error7, True , white)
                            pygame.draw.rect(screen,black,[800,700,400,30])
                            screen.blit(textErrortwo , (800,700))                         
                            
                            

                #If we click on Label Elements
                if 900<mouse[0]<1100 and 102<mouse[1]<122:
                    start_pointer=True
                    goal_pointer=False
                    obsticle_pointer=False
                    mountain_pointer=False
                    water_pointer=False
                    green_pointer=False
                elif 900<mouse[0]<1100 and 142<mouse[1]<162:
                    start_pointer=False
                    goal_pointer=True
                    obsticle_pointer=False
                    mountain_pointer=False
                    water_pointer=False
                    green_pointer=False
                elif 900<mouse[0]<1100 and 182<mouse[1]<202:
                    start_pointer=False
                    goal_pointer=False
                    obsticle_pointer=True
                    mountain_pointer=False
                    water_pointer=False
                    green_pointer=False
                elif 900<mouse[0]<1100 and 222<mouse[1]<242:
                    start_pointer=False
                    goal_pointer=False
                    obsticle_pointer=False
                    mountain_pointer=True
                    water_pointer=False
                    green_pointer=False
                elif 900<mouse[0]<1100 and 262<mouse[1]<282:
                    start_pointer=False
                    goal_pointer=False
                    obsticle_pointer=False
                    mountain_pointer=False
                    water_pointer=True
                    green_pointer=False
                elif 900<mouse[0]<1100 and 302<mouse[1]<322:
                    start_pointer=False
                    goal_pointer=False
                    obsticle_pointer=False
                    mountain_pointer=False
                    water_pointer=False
                    green_pointer=True
                    
                #For Terrain editing changes
                if 0<=mx<=temp_width and 0<=my<=temp_height:
                    if start_pointer==True:
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in GoalList:
                            GoalList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in ObsticleList:
                            ObsticleList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in MountainList:
                            MountainList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in WaterList:
                            WaterList.remove([mpos_x,mpos_y])
                        if status_start[0]==True:
                            for i,j in StartList:
                                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                                pygame.draw.rect(screen, green, rect)
                                StartList.remove([i,j])
                            rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                            pygame.draw.rect(screen, white, rect)
                            StartList.append([mpos_x,mpos_y])
                        else:
                            if [mpos_x,mpos_y] not in StartList:
                                rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                                pygame.draw.rect(screen, white, rect)
                                StartList.append([mpos_x,mpos_y])


                    elif goal_pointer==True:
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in ObsticleList:
                            ObsticleList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in MountainList:
                            MountainList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in WaterList:
                            WaterList.remove([mpos_x,mpos_y])
                        if status_goal[0]==True:
                            for i,j in GoalList:
                                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                                pygame.draw.rect(screen, green, rect)
                                GoalList.remove([i,j])
                            rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                            pygame.draw.rect(screen, yellow, rect)
                            GoalList.append([mpos_x,mpos_y])
                        else:
                            if [mpos_x,mpos_y] not in GoalList:
                                rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                                pygame.draw.rect(screen, yellow, rect)
                                screen.blit(textgoalindex , (mpos_x,mpos_y))
                                GoalList.append([mpos_x,mpos_y])
                                goal_pointer_numbering+=1
                            else:
                                continue

                    elif obsticle_pointer==True:
                        rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                        pygame.draw.rect(screen, black, rect)
                        if [mpos_x,mpos_y] not in ObsticleList:
                            ObsticleList.append([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in GoalList:
                            GoalList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in MountainList:
                            MountainList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in WaterList:
                            WaterList.remove([mpos_x,mpos_y])

                    elif mountain_pointer==True:
                        rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                        pygame.draw.rect(screen, brown, rect)
                        if [mpos_x,mpos_y] not in MountainList:
                            MountainList.append([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in GoalList:
                            GoalList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in ObsticleList:
                            ObsticleList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in WaterList:
                            WaterList.remove([mpos_x,mpos_y])

                    elif water_pointer==True:
                        rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                        pygame.draw.rect(screen, blue, rect)
                        if [mpos_x,mpos_y] not in WaterList:
                            WaterList.append([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in GoalList:
                            GoalList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in ObsticleList:
                            ObsticleList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in MountainList:
                            MountainList.remove((mpos_x,mpos_y))
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])

                    elif green_pointer==True:
                        rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                        pygame.draw.rect(screen, green, rect)
                        if [mpos_x,mpos_y] in StartList:
                            StartList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in GoalList:
                            GoalList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in ObsticleList:
                            ObsticleList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in MountainList:
                            MountainList.remove([mpos_x,mpos_y])
                        if [mpos_x,mpos_y] in WaterList:
                            WaterList.remove([mpos_x,mpos_y])
                    
                else:
                    continue
                
            ###if middle mouse button is clicked###
            elif pygame.mouse.get_pressed()[1]:       
                pass

            ###if right mouse button is clicked###
            elif pygame.mouse.get_pressed()[2]:
                mx,my=pygame.mouse.get_pos()
                mpos_x=(mx//EachBlockWeight)*EachBlockWeight
                mpos_y=(my//EachBlockHeight)*EachBlockHeight
                rect = pygame.Rect(mpos_x, mpos_y, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, green, rect)
                if [mpos_x,mpos_y] in StartList:
                    StartList.remove([mpos_x,mpos_y])
                if [mpos_x,mpos_y] in GoalList:
                    GoalList.remove([mpos_x,mpos_y])
                if [mpos_x,mpos_y] in ObsticleList:
                    ObsticleList.remove([mpos_x,mpos_y])
                if [mpos_x,mpos_y] in MountainList:
                    MountainList.remove([mpos_x,mpos_y])
                if [mpos_x,mpos_y] in WaterList:
                    WaterList.remove([mpos_x,mpos_y])
            
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            pygame.display.update()

            if 900<mx<1100 and 460<my<510:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        MountainCost = MountainCost[:-1]
                    else:
                        MountainCost += event.unicode

            if 900<mouse[0]<1100 and 555<mouse[1]<605:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        WaterCost = WaterCost[:-1]
                    else:
                        WaterCost += event.unicode

            if 900<mouse[0]<1100 and 645<mouse[1]<695:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        GreenCost = GreenCost[:-1]
                    else:
                        GreenCost += event.unicode
            

            
        #if mouse is over START Button
        if 800<=mouse[0]<=1200 and 720<=mouse[1]<=800:
            pygame.draw.rect(screen,green,[800,720,400,100])
            screen.blit(textB3 , (850,715))
        else:
            pygame.draw.rect(screen,orange,[800,720,400,100])
            screen.blit(textB3 , (850,715))

        #if mouse is over Label elements
        ##Start Label and Symbol
        if 900<=mouse[0]<=1100 and 102<=mouse[1]<=122:
            pygame.draw.rect(screen,green,[900,102,200,20])
            screen.blit(textB1_5 , (930,105))
            pygame.draw.rect(screen,white,[1050,105,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,102,200,20])
            screen.blit(textB1_5 , (930,105))
            pygame.draw.rect(screen,white,[1050,105,15,15])
        ##Goal Label and Symbol
        if 900<=mouse[0]<=1100 and 142<=mouse[1]<=162:
            pygame.draw.rect(screen,green,[900,142,200,20])
            screen.blit(textB1_6 , (930,145))
            pygame.draw.rect(screen,yellow,[1050,145,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,142,200,20])
            screen.blit(textB1_6 , (930,145))
            pygame.draw.rect(screen,yellow,[1050,145,15,15])
        ##Obsticle Label and Symbol
        if 900<=mouse[0]<=1100 and 182<=mouse[1]<=202:
            pygame.draw.rect(screen,green,[900,182,200,20])
            screen.blit(textB1_1 , (930,185))
            pygame.draw.rect(screen,black,[1050,185,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,182,200,20])
            screen.blit(textB1_1 , (930,185))
            pygame.draw.rect(screen,black,[1050,185,15,15])
        ##Mountain Label and Symbol
        if 900<=mouse[0]<=1100 and 222<=mouse[1]<=242:
            pygame.draw.rect(screen,green,[900,222,200,20])
            screen.blit(textB1_2 , (930,225))
            pygame.draw.rect(screen,brown,[1050,225,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,222,200,20])
            screen.blit(textB1_2 , (930,225))
            pygame.draw.rect(screen,brown,[1050,225,15,15])
        ##Water Label and Symbol
        if 900<=mouse[0]<=1100 and 262<=mouse[1]<=282:
            pygame.draw.rect(screen,green,[900,262,200,20])
            screen.blit(textB1_3 , (950,265))
            pygame.draw.rect(screen,blue,[1050,265,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,262,200,20])
            screen.blit(textB1_3 , (950,265))
            pygame.draw.rect(screen,blue,[1050,265,15,15])
        ##Greenary Label and Symbol
        if 900<=mouse[0]<=1100 and 302<=mouse[1]<=322:
            pygame.draw.rect(screen,green,[900,302,200,20])
            screen.blit(textB1_4 , (930,305))
            pygame.draw.rect(screen,green,[1050,305,15,15])
        else:
            pygame.draw.rect(screen,orange,[900,302,200,20])
            screen.blit(textB1_4 , (930,305))
            pygame.draw.rect(screen,green,[1050,305,15,15])


        #ALL GREENARY
        pygame.draw.rect(screen,orange,[805,150,90,20])
        screen.blit(textB4_1 , (805,150))

        #ALL OBSTICLES
        pygame.draw.rect(screen,orange,[805,225,90,20])
        screen.blit(textB4_2 , (805,225))

        #Label Heading
        pygame.draw.rect(screen,orange,[800,0,400,80])
        screen.blit(textB1 , (850,10))
        

        #Cost Heading
        pygame.draw.rect(screen,orange,[800,350,400,80])
        screen.blit(textB2 , (875,360))
        ##Mountain cost Label
        screen.blit(textB2_1 , (925,440))
        ##Water cost Label
        screen.blit(textB2_2 , (940,535))
        ##Greenary cost Label
        screen.blit(textB2_3 , (925,625))
        ##Costs input reader
        pygame.draw.rect(screen, orange, [900,460,200,50])
        text_surface = base_font.render(MountainCost, True, black)
        screen.blit(text_surface, (975, 460))

        pygame.draw.rect(screen, orange, [900,555,200,50])
        text_surface = base_font.render(WaterCost, True, black)
        screen.blit(text_surface, (975,555))

        pygame.draw.rect(screen, orange, [900,645,200,50])
        text_surface = base_font.render(GreenCost, True, black)
        screen.blit(text_surface, (975,645))

        pygame.display.update()
        if runningSecondScreen==False:
            SwitchTwo=True
            

#----------------------------------------------------------------------------
#-------------------------------------------------------------END OF SECOND SCREEN---------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#COMMON FUNCTIONS
def partition(array1,array2, low, high):
    pivot=array1[high]
    i=low-1
    for j in range(low,high):
        if array1[j]<=pivot:
            i=i+1
            (array1[i],array1[j])=(array1[j],array1[i])
            (array2[i],array2[j])=(array2[j],array2[i])
    array1[i+1],array1[high]=array1[high],array1[i+1]
    array2[i+1],array2[high]=array2[high],array2[i+1]
    return i+1

def quicksort(array1,array2,low,high):
    if low<high:
        pi=partition(array1,array2,low,high)
        quicksort(array1,array2,low,pi-1)
        quicksort(array1,array2,pi+1,high)


def drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight):
        for i in range(NumberOfRows):
            for j in range(NumberOfColumns):
                rect = pygame.Rect(i*EachBlockWeight, j*EachBlockHeight,EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, black, rect, 1)

def DrawMultiplePath(array,EachBlockWeight,EachBlockHeight):
    present_x=array[0][0]
    present_y=array[0][1]
    aligned_present_x=present_x+int(EachBlockWeight/2)
    aligned_present_y=present_y+int(EachBlockHeight/2)
    for index in range(1,len(array)):
        next_x=array[index][0]
        next_y=array[index][1]
        aligned_next_x=next_x+int(EachBlockWeight/2)
        aligned_next_y=next_y+int(EachBlockHeight/2)
        pygame.draw.line(screen,red,(aligned_present_x,aligned_present_y),(aligned_next_x,aligned_next_y),6)
        aligned_present_x=aligned_next_x
        aligned_present_y=aligned_next_y
    pygame.display.update()

def BackGround():
    global temp_running
    global status_1x
    global status_2x
    global status_5x
    global status_10x
    global status_BestPath
    global status_AllPath
    global left_pointer
    global right_pointer
    global left_pointer_active
    global right_pointer_active
    global temp_running
    global sleep_time
    x=time.perf_counter()+sleep_time
    while time.perf_counter()<x:
        mx,my=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                #if 1x Button is pressed
                if 850<=mx<=895 and 70<=my<=115:
                    if status_1x==True:
                        status_1x=False
                    else:
                        status_1x=True
                        status_2x=False
                        status_5x=False
                        status_10x=False
                #if 2x Button is pressed
                if 920<=mx<=965 and 70<=my<=115:                 
                    if status_2x==True:
                        status_2x=False
                    else:
                        status_2x=True
                        status_1x=False
                        status_5x=False
                        status_10x=False
                #if 5x Button is pressed
                if 990<=mx<=1035 and 70<=my<=115:
                    if status_5x==True:
                        status_5x=False
                    else:
                        status_5x=True
                        status_1x=False
                        status_2x=False
                        status_10x=False
                #if 10x Button is pressed
                if 1060<=mx<=1130 and 70<=my<=115:
                    if status_10x==True:
                        status_10x=False
                    else:
                        status_10x=True
                        status_1x=False
                        status_2x=False
                        status_5x=False
                #if Best Path Button is pressed
                if 850<=mx<=1150 and 475<=my<=545:
                    if status_BestPath==True:
                        status_BestPath=False
                    else:
                        status_BestPath=True
                        status_AllPath=False
                        left_pointer=False
                        right_pointer=False                
                #if All path Button is pressed
                if 850<=mx<=1150 and 575<=my<=645:
                    if status_AllPath==True:
                        status_AllPath=False
                    else:
                        status_AllPath=True
                        status_BestPath=False
                        left_pointer=True
                        right_pointer=True
                
            ##1x Button becomes green
            if status_1x==True:
                pygame.draw.rect(screen,green,[850,70,45,45])
                screen.blit(textC1_1 , (850,70))
            else:
                pygame.draw.rect(screen,orange,[850,70,45,45])
                screen.blit(textC1_1 , (850,70))

            #2x Button becomes green
            if status_2x==True:
                pygame.draw.rect(screen,green,[920,70,45,45])
                screen.blit(textC1_2 , (920,70))
            else:
                pygame.draw.rect(screen,orange,[920,70,45,45])
                screen.blit(textC1_2 , (920,70))

            #5x Button becomes green
            if status_5x==True:
                pygame.draw.rect(screen,green,[990,70,45,45])
                screen.blit(textC1_3 , (990,70))
            else:
                pygame.draw.rect(screen,orange,[990,70,45,45])
                screen.blit(textC1_3 , (990,70))

            #10x Button becomes green
            if status_10x==True:
                pygame.draw.rect(screen,green,[1060,70,70,45])
                screen.blit(textC1_4 , (1060,70))
            else:
                pygame.draw.rect(screen,orange,[1060,70,70,45])
                screen.blit(textC1_4 , (1060,70))

            #Best path button becomes green
            if status_BestPath==True:
                pygame.draw.rect(screen,green,[850,475,300,70])
                screen.blit(textC6 , (850,475))
            else:
                pygame.draw.rect(screen,orange,[850,475,300,70])
                screen.blit(textC6 , (850,475))
    
            #All path button becomes green
            if status_AllPath==True:
                pygame.draw.rect(screen,green,[850,575,300,70])
                screen.blit(textC5 , (865,575))
            else:
                pygame.draw.rect(screen,orange,[850,575,300,70])
                screen.blit(textC5 , (865,575))        
                
    
def DrawSinglePath(array,EachBlockWeight,EachBlockHeight):
    global status_1x
    global status_2x
    global status_5x
    global status_10x
    global status_BestPath
    global status_AllPath
    global left_pointer
    global right_pointer
    global left_pointer_active
    global right_pointer_active
    global temp_running
    global sleep_time
    present_x=array[0][0]
    present_y=array[0][1]
    aligned_present_x=present_x+int(EachBlockWeight/2)
    aligned_present_y=present_y+int(EachBlockHeight/2)
    for index in range(1,len(array)):
        if status_1x==True:
            sleep_time=0.9
        if status_2x==True:
            sleep_time=0.3
        if status_5x==True:
            sleep_time=0.1
        if status_10x==True:
            sleep_time=0.01
        if status_BestPath==False:
             break
        if status_AllPath==True:
            screen.fill(green)
            drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
            Imprint_the_elements()
            break
        next_x=array[index][0]
        next_y=array[index][1]
        aligned_next_x=next_x+int(EachBlockWeight/2)
        aligned_next_y=next_y+int(EachBlockHeight/2)
        pygame.draw.line(screen,red,(aligned_present_x,aligned_present_y),(aligned_next_x,aligned_next_y),6)
        aligned_present_x=aligned_next_x
        aligned_present_y=aligned_next_y
        pygame.display.update()
        time.sleep(sleep_time)
        BackGround()
    temp_running=False

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#FUNCTION ONE -------> FOR SINGLE START AND SINGLE GOAL
#_______________________________________________________
#FUNCTION ONE VARIABLES
single_start1=[]
SingleGoal1=[]

BestCost1=float('inf')
BestPath1=[]
AllCost1=[]
AllPath1=[]
TotalPath1=0

#FUNCTIONS
def UnBlindedSearch_SingleStart_SingleGoal(CurrentPos1,SingleGoal1,CurrentCost1,CurrentPath1,ObsticleList,MountainList,WaterList):
    global BestCost1
    global BestPath1
    global AllCost1
    global AllPath1
    global TotalPath1

    ###Condition To Terminate the Recursive Function
    #First Condition: If we reach the goal
    if CurrentPos1==SingleGoal1:
        #If we find the best path so far
        if BestCost1>CurrentCost1:
            BestCost1=CurrentCost1
            BestPath1=CurrentPath1[:]
        #To add to solution space
        AllCost1.append(CurrentCost1)
        AllPath1.append(CurrentPath1)
        TotalPath1+=1
        return
    
    #Second Condition: If we get too many solutions then we remove worst half solutions
    if len(AllCost1)>=100:
        n1=len(AllCost1)
        n2=len(AllPath1)
        quicksort(AllCost1,AllPath1,0,n1-1)
        AllCost1=AllCost1[:n1//2]
        AllPath1=AllPath1[:n2//2]

    #Third Condition: we if check more than 100 paths then we can stop the search
    if TotalPath1>100:
        return

    ###To calculate the Heuristic for all possible moves
    Heuristic_Right_Move=float('inf')
    Heuristic_Bottom_Right_Move=float('inf')
    Heuristic_Bottom_Move=float('inf')
    Heuristic_Bottom_Left_Move=float('inf')
    Heuristic_Left_Move=float('inf')
    Heuristic_Top_Left_Move=float('inf')
    Heuristic_Top_Move=float('inf')
    Heuristic_Top_Right_Move=float('inf')
    list_Heuristic_Values=[float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
    list_Heuristic_Index=[1,2,3,4,5,6,7,8]
    
    #####Move cost calculation
    #Right_Move
    if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+0] not in ObsticleList and (0<=(CurrentPos1[0]+EachBlockWeight)) and ((CurrentPos1[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]+0)) and ((CurrentPos1[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Right_Move=math.sqrt((SingleGoal1[0]-(CurrentPos1[0]+EachBlockWeight))**2+((SingleGoal1[1]-(CurrentPos1[1]+0)))**2)
        #if next position is a mountain
        if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+0] in MountainList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+0] in WaterList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[0]=Heuristic_Right_Move+GreenCost
            
    #Bottom_Right_Move
    if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]+EachBlockWeight)) and ((CurrentPos1[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]+EachBlockHeight)) and ((CurrentPos1[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Right_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]+EachBlockWeight)))**2+((SingleGoal1[1]-(CurrentPos1[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+GreenCost
            
    #Bottom_Move
    if [CurrentPos1[0]+0,CurrentPos1[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]+0)) and ((CurrentPos1[0]+0)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]+EachBlockHeight)) and ((CurrentPos1[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]+0)))**2+((SingleGoal1[1]-(CurrentPos1[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in MountainList:
           list_Heuristic_Values[2]=Heuristic_Bottom_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+GreenCost

    #Bottom_Left_Move
    if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]-EachBlockWeight)) and ((CurrentPos1[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]+EachBlockHeight)) and ((CurrentPos1[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Left_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]-EachBlockWeight)))**2+((SingleGoal1[1]-(CurrentPos1[1]+EachBlockHeight)))**2)
        list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move
        #if next position is a mountain
        if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+GreenCost

    #Left_Move
    if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+0] not in ObsticleList and (0<=(CurrentPos1[0]-EachBlockWeight)) and ((CurrentPos1[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]+0)) and ((CurrentPos1[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Left_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]-EachBlockWeight)))**2+((SingleGoal1[1]-(CurrentPos1[1]+0)))**2)
        list_Heuristic_Values[4]=Heuristic_Left_Move
        #if next position is a mountain
        if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+0] in MountainList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]+0] in WaterList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[4]=Heuristic_Left_Move+GreenCost

    #Top_Left_Move
    if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]-EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]-EachBlockWeight)) and ((CurrentPos1[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]-EachBlockHeight)) and ((CurrentPos1[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Left_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]-EachBlockWeight)))**2+((SingleGoal1[1]-(CurrentPos1[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[5]=Heuristic_Top_Left_Move
        #if next position is a mountain
        if [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]-EachBlockWeight,CurrentPos1[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+GreenCost

    #Top_Move
    if [CurrentPos1[0]-0,CurrentPos1[1]-EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]-0)) and ((CurrentPos1[0]-0)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]-EachBlockHeight)) and ((CurrentPos1[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]-0)))**2+((SingleGoal1[1]-(CurrentPos1[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[6]=Heuristic_Top_Move
        #if next position is a mountain
        if [CurrentPos1[0]-0,CurrentPos1[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]-0,CurrentPos1[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[6]=Heuristic_Top_Move+GreenCost

    #Top_Right_Move
    if [CurrentPos1[0]+EachBlockWeight,CurrentPos1[1]-EachBlockHeight] not in ObsticleList and (0<=(CurrentPos1[0]+EachBlockWeight)) and ((CurrentPos1[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos1[1]-EachBlockHeight)) and ((CurrentPos1[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Right_Move=math.sqrt(((SingleGoal1[0]-(CurrentPos1[0]+EachBlockWeight)))**2+((SingleGoal1[1]-(CurrentPos1[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[7]=Heuristic_Top_Right_Move
        #if next position is a mountain
        if [CurrentPos1[0]-0,CurrentPos1[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos1[0]-0,CurrentPos1[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+GreenCost
        

    ###Sortin of Heuristic values by using selection sort in Ascending Order
    for i in range(len(list_Heuristic_Values)):
        key=i
        for j in range(i+1,len(list_Heuristic_Index)):
            if list_Heuristic_Values[key]>list_Heuristic_Values[j]:
                key=j
        list_Heuristic_Values[i],list_Heuristic_Values[key]=list_Heuristic_Values[key],list_Heuristic_Values[i]
        list_Heuristic_Index[i],list_Heuristic_Index[key]=list_Heuristic_Index[key],list_Heuristic_Index[i]


    ###Calling the next three best recursive functions for next three best positions
    times=0
    for move in range(len(list_Heuristic_Index)):


        ##Conditions to Break the Loop
        #Conditon 1: If we iterater through the loop for 3 times
        if times==3:
            break
        times+=1
        #Conditon 2: If we encounter infinite value for heuristic
        if list_Heuristic_Values[move]==float('inf'):
            break
        
        #Prepare Variables for Recursive calls
        NewCurrentPos1=CurrentPos1[:]
        NewCurrentCost1=CurrentCost1
        NewCurrentPath1=CurrentPath1[:]


        #If Right_Move is Best Move:
        if list_Heuristic_Index[move]==1:
            NewCurrentPos1[0]=CurrentPos1[0]+EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)

        #If Right_Bottom_Move is Best Move 
        elif list_Heuristic_Index[move]==2:
            NewCurrentPos1[0]=CurrentPos1[0]+EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==3:
            NewCurrentPos1[0]=CurrentPos1[0]+0
            NewCurrentPos1[1]=CurrentPos1[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Left_Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==4:
            NewCurrentPos1[0]=CurrentPos1[0]-EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Left_Move is Best Move
        elif list_Heuristic_Index[move]==5:
            NewCurrentPos1[0]=CurrentPos1[0]-EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Left_Top_Move is Best Move
        elif list_Heuristic_Index[move]==6:
            NewCurrentPos1[0]=CurrentPos1[0]-EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Top_Move is Best Move
        elif list_Heuristic_Index[move]==7:
            NewCurrentPos1[0]=CurrentPos1[0]-0
            NewCurrentPos1[1]=CurrentPos1[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)
        #If Right_Top_Move is Best Move
        elif list_Heuristic_Index[move]==8:
            NewCurrentPos1[0]=CurrentPos1[0]+EachBlockWeight
            NewCurrentPos1[1]=CurrentPos1[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos1 in NewCurrentPath1:
                continue
            else:
                NewCurrentPath1.append(NewCurrentPos1)
                #if next position is a mountain
                if NewCurrentPos1 in MountainList:
                    NewCurrentCost1=NewCurrentCost1+MountainCost
                #if next postion is water 
                elif NewCurrentPos1 in WaterList:
                    NewCurrentCost1=NewCurrentCost1+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost1=NewCurrentCost1+GreenCost
                UnBlindedSearch_SingleStart_SingleGoal(NewCurrentPos1,SingleGoal1,NewCurrentCost1,NewCurrentPath1,ObsticleList,MountainList,WaterList)


def Pre_Requisite_UnBlindedSearch_SingleStart_SingleGoal(StartList,GoalList,EachBlockWeight,EachBlockHeight):
    temp_start=StartList[:]
    temp_goal=GoalList[:]
    single_start1=temp_start[0]
    SingleGoal1=temp_goal[0]
    CurrentPos1=[single_start1[0],single_start1[1]]
    CurrentPath1=[[CurrentPos1[0],CurrentPos1[1]]]
    CurrentCost1=0
    UnBlindedSearch_SingleStart_SingleGoal(CurrentPos1,SingleGoal1,CurrentCost1,CurrentPath1,ObsticleList,MountainList,WaterList)


def Post_Requisite_UnBlindedSearch_SingleStart_SingleGoal():
    global AllCost1
    global AllPath1
    ###Sorting of All Solutions is descending order
    quicksort(AllCost1,AllPath1,0,len(AllCost1)-1)


"""
#Driver_Code
Pre_Requisite_UnBlindedSearch_SingleStart_SingleGoal(single_start1,SingleGoal1,EachBlockWeight,EachBlockHeight)
Post_Requisite_UnBlindedSearch_SingleStart_SingleGoal()
screen.fill(green)
drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
DrawSinglePath1(BestPath1,EachBlockWeight,EachBlockHeight)
"""


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#FUNCTION SECOND -------> FOR SINGLE START AND MULTIPLE GOAL
#_______________________________________________________
#FUNCTION ONE VARIABLES
single_start2=[]
multiple_goal2=[]

BestCost2=float('inf')
BestPath2=[]
AllCost2=[]
AllPath2=[]
Temp_AllCost2_Main=[]
Temp_AllPath2_Main=[]
Temp_AllCost2_Middle=[]
Temp_AllPath2_Middle=[]
CurrentPath_so_far2=[]
TotalPath2=0

#FUNCTIONS
def UnBlindedSearch_SingleStart_MultipleGoal(CurrentPos2,SingleGoal2,CurrentCost2,CurrentPath2,ObsticleList,MountainList,WaterList):
    global BestCost2
    global BestPath2
    global AllCost2
    global AllPath2
    global Temp_AllCost2_Main
    global Temp_AllPath2_Main
    global TotalPath2
    global Temp_AllCost2_Middle
    global Temp_AllPath2_Middle
    global CurrentPath_so_far2
    global single_start2
    global multipe_goal2

    ###Condition to Terminate the Recursive Function
    #First condition : if we reach the goal
    if CurrentPos2==SingleGoal2:
        Temp_AllCost2_Middle.append(CurrentCost2)
        Temp_AllPath2_Middle.append(CurrentPath2)
        TotalPath2+=1

    #Reduce this value to less than 10 for more optimial time 
    if len(Temp_AllPath2_Middle)>3:
        return
    #Reduce least deserving 50 percent paths
    if len(AllPath2)>=1000:
        n1=len(AllCost2)
        n2=len(AllPath2)
        quicksort(AllCost2,AllPath2,0,n1-1)
        AllCost2=AllCost2[:n1//2]
        AllPath2=AllPath2[:n2//2]



    ###To calculate the Heuristic for all possible moves
    Heuristic_Right_Move=float('inf')
    Heuristic_Bottom_Right_Move=float('inf')
    Heuristic_Bottom_Move=float('inf')
    Heuristic_Bottom_Left_Move=float('inf')
    Heuristic_Left_Move=float('inf')
    Heuristic_Top_Left_Move=float('inf')
    Heuristic_Top_Move=float('inf')
    Heuristic_Top_Right_Move=float('inf')
    list_Heuristic_Values=[float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
    list_Heuristic_Index=[1,2,3,4,5,6,7,8]
    #Move cost calculation
    #Right_Move
    if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+0] not in ObsticleList and [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+0] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]+EachBlockWeight)) and ((CurrentPos2[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]+0)) and ((CurrentPos2[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Right_Move=math.sqrt((SingleGoal2[0]-(CurrentPos2[0]+EachBlockWeight))**2+((SingleGoal2[1]-(CurrentPos2[1]+0)))**2)
        #if next position is a mountain
        if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+0] in MountainList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+0] in WaterList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[0]=Heuristic_Right_Move+GreenCost
            
    #Bottom_Right_Move
    if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] not in ObsticleList and [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]+EachBlockWeight)) and ((CurrentPos2[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]+EachBlockHeight)) and ((CurrentPos2[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Right_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]+EachBlockWeight)))**2+((SingleGoal2[1]-(CurrentPos2[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+GreenCost
            
    #Bottom_Move
    if [CurrentPos2[0]+0,CurrentPos2[1]+EachBlockHeight] not in ObsticleList and [CurrentPos2[0]+0,CurrentPos2[1]+EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]+0)) and ((CurrentPos2[0]+0)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]+EachBlockHeight)) and ((CurrentPos2[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]+0)))**2+((SingleGoal2[1]-(CurrentPos2[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in MountainList:
           list_Heuristic_Values[2]=Heuristic_Bottom_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+GreenCost

    #Bottom_Left_Move
    if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+EachBlockHeight] not in ObsticleList and [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]-EachBlockWeight)) and ((CurrentPos2[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]+EachBlockHeight)) and ((CurrentPos2[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Left_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]-EachBlockWeight)))**2+((SingleGoal2[1]-(CurrentPos2[1]+EachBlockHeight)))**2)
        list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move
        #if next position is a mountain
        if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+GreenCost

    #Left_Move
    if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+0] not in ObsticleList and [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+0] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]-EachBlockWeight)) and ((CurrentPos2[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]+0)) and ((CurrentPos2[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Left_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]-EachBlockWeight)))**2+((SingleGoal2[1]-(CurrentPos2[1]+0)))**2)
        list_Heuristic_Values[4]=Heuristic_Left_Move
        #if next position is a mountain
        if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+0] in MountainList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]+0] in WaterList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[4]=Heuristic_Left_Move+GreenCost

    #Top_Left_Move
    if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]-EachBlockHeight] not in ObsticleList and [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]-EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]-EachBlockWeight)) and ((CurrentPos2[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]-EachBlockHeight)) and ((CurrentPos2[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Left_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]-EachBlockWeight)))**2+((SingleGoal2[1]-(CurrentPos2[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[5]=Heuristic_Top_Left_Move
        #if next position is a mountain
        if [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]-EachBlockWeight,CurrentPos2[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+GreenCost

    #Top_Move
    if [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] not in ObsticleList and [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]-0)) and ((CurrentPos2[0]-0)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]-EachBlockHeight)) and ((CurrentPos2[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]-0)))**2+((SingleGoal2[1]-(CurrentPos2[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[6]=Heuristic_Top_Move
        #if next position is a mountain
        if [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[6]=Heuristic_Top_Move+GreenCost

    #Top_Right_Move
    if [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]-EachBlockHeight] not in ObsticleList and [CurrentPos2[0]+EachBlockWeight,CurrentPos2[1]-EachBlockHeight] not in CurrentPath_so_far2 and (0<=(CurrentPos2[0]+EachBlockWeight)) and ((CurrentPos2[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos2[1]-EachBlockHeight)) and ((CurrentPos2[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Right_Move=math.sqrt(((SingleGoal2[0]-(CurrentPos2[0]+EachBlockWeight)))**2+((SingleGoal2[1]-(CurrentPos2[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[7]=Heuristic_Top_Right_Move
        #if next position is a mountain
        if [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos2[0]-0,CurrentPos2[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+GreenCost
        
        

    ###Sorting of Heuristic values by using selection sort in Ascending Order
    for i in range(len(list_Heuristic_Values)):
        key=i
        for j in range(i+1,len(list_Heuristic_Index)):
            if list_Heuristic_Values[key]>list_Heuristic_Values[j]:
                key=j
        list_Heuristic_Values[i],list_Heuristic_Values[key]=list_Heuristic_Values[key],list_Heuristic_Values[i]
        list_Heuristic_Index[i],list_Heuristic_Index[key]=list_Heuristic_Index[key],list_Heuristic_Index[i]


    ###Calling the next three best recursive functions for next three best positions
    times=0
    for move in range(len(list_Heuristic_Index)):

        ##Conditions to Break the Loop
        #Conditon 1: If we iterater through the loop for 3 times
        if times==3:
            break
        times+=1
        #Conditon 2: If we encounter infinite value for heuristic
        if list_Heuristic_Values[move]==float('inf'):
            break

        #Prepare Variables for Recursive calls
        NewCurrentPos42=CurrentPos2[:]
        NewCurrentCost2=CurrentCost2
        NewCurrentPath2=CurrentPath2[:]

        #If Right_Move is Best Move:
        if list_Heuristic_Index[move]==1:
            NewCurrentPos42[0]=CurrentPos2[0]+EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)

        #If Right_Bottom_Move is Best Move 
        elif list_Heuristic_Index[move]==2:
            NewCurrentPos42[0]=CurrentPos2[0]+EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==3:
            NewCurrentPos42[0]=CurrentPos2[0]+0
            NewCurrentPos42[1]=CurrentPos2[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Left_Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==4:
            NewCurrentPos42[0]=CurrentPos2[0]-EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Left_Move is Best Move
        elif list_Heuristic_Index[move]==5:
            NewCurrentPos42[0]=CurrentPos2[0]-EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Left_Top_Move is Best Move
        elif list_Heuristic_Index[move]==6:
            NewCurrentPos42[0]=CurrentPos2[0]-EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Top_Move is Best Move
        elif list_Heuristic_Index[move]==7:
            NewCurrentPos42[0]=CurrentPos2[0]-0
            NewCurrentPos42[1]=CurrentPos2[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)
        #If Right_Top_Move is Best Move
        elif list_Heuristic_Index[move]==8:
            NewCurrentPos42[0]=CurrentPos2[0]+EachBlockWeight
            NewCurrentPos42[1]=CurrentPos2[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos42 in NewCurrentPath2:
                continue
            else:
                NewCurrentPath2.append(NewCurrentPos42)
                #if next position is a mountain
                if NewCurrentPos42 in MountainList:
                    NewCurrentCost2=NewCurrentCost2+MountainCost
                #if next postion is water 
                elif NewCurrentPos42 in WaterList:
                    NewCurrentCost2=NewCurrentCost2+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost2=NewCurrentCost2+GreenCost
                UnBlindedSearch_SingleStart_MultipleGoal(NewCurrentPos42,SingleGoal2,NewCurrentCost2,NewCurrentPath2,ObsticleList,MountainList,WaterList)





def Pre_Requisite_UnBlindedSearch_SingleStart_MultipleGoal(StartList,GoalList,EachBlockWeight,EachBlockHeight):
    global BestCost2
    global BestPath2
    global AllCost2
    global AllPath2
    global Temp_AllCost2_Main
    global Temp_AllPath2_Main
    global Temp_AllCost2_Middle
    global Temp_AllPath2_Middle
    global CurrentPath_so_far2
    firstTime=True
    multiple_goal2=GoalList[:]
    CurrentPos2=[StartList[0],StartList[1]]
    for single_temp_goal2 in multiple_goal2:
        Temp_AllCost2_Middle=[]
        Temp_AllPath2_Middle=[]
        SingleGoal2=single_temp_goal2[:]
        #For starting goal
        if firstTime==True:
            firstTime=False
            CurrentPath_so_far2=[]
            CurrentCost2=0
            CurrentPath2=[CurrentPos2]
            UnBlindedSearch_SingleStart_MultipleGoal(CurrentPos2,SingleGoal2,CurrentCost2,CurrentPath2,ObsticleList,MountainList,WaterList)
            Temp_AllCost2_Main=Temp_AllCost2_Middle[:]
            Temp_AllPath2_Main=Temp_AllPath2_Middle[:]
            AllCost2=Temp_AllCost2_Main[:]
            AllPath2=Temp_AllPath2_Main[:]
        else:
            if len(AllPath2)==0 or len(AllCost2)==0:
                break
            Temp_AllCost2_Middle=[]
            Temp_AllPath2_Middle=[]
            Temp_AllCost2_Main=[]
            Temp_AllPath2_Main=[]
            CurrentPath_so_far2=[]
            CurrentCost2=0
            CurrentPath2=[CurrentPos2]
            UnBlindedSearch_SingleStart_MultipleGoal(CurrentPos2,SingleGoal2,CurrentCost2,CurrentPath2,ObsticleList,MountainList,WaterList)

            for i in range(len(AllPath2)):
                t1_path=AllPath2[i]
                t1_cost=AllCost2[i]
                for j in range(len(Temp_AllPath2_Middle)):
                    t2_path=Temp_AllPath2_Middle[j][:]
                    t2_cost=Temp_AllCost2_Middle[j]
                    t_path=t1_path+t2_path
                    t_cost=t1_cost+t2_cost
                    Temp_AllPath2_Main.append(t_path)
                    Temp_AllCost2_Main.append(t_cost)
            AllCost2=Temp_AllCost2_Main[:]
            AllPath2=Temp_AllPath2_Main[:]
        CurrentPos2=single_temp_goal2
        
                    
def Post_Requisite_UnBlindedSearch_SingleStart_MultipleGoal():
    global AllCost2
    global AllPath2
    global BestPath2
    global BestCost2
    
    ###Sorting of All Solutions is descending order
    quicksort(AllCost2,AllPath2,0,len(AllCost2)-1)
    for index in range(len(AllCost2)):
        if BestCost2>AllCost2[index]:
            BestCost2=AllCost2[index]
            BestPath2=AllPath2[index]
            

"""
#Driver_Code
Pre_Requisite_UnBlindedSearch_SingleStart_MultipleGoal(single_start2,multiple_goal2,EachBlockWeight,EachBlockHeight)
Post_Requisite_UnBlindedSearch_SingleStart_MultipleGoal()
screen.fill(green)
drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
DrawSinglePath1(BestPath2,EachBlockWeight,EachBlockHeight)
"""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#FUNCTION THIRD -------> FOR MULTIPLE START AND SINGLE GOAL
#_______________________________________________________
#FUNCTION ONE VARIABLES
multiple_start3=[]
SingleGoal3=[]

BestCost3=float('inf')
BestPath3=[]
AllCost3=[]
AllPath3=[]
Temp_AllCost3=[]
Temp_AllPath3=[]
TotalPath3=0

#FUNCTIONS  
def UnBlindedSearch_MultipleStart_SingleGoal(CurrentPos3,SingleGoal3,CurrentCost3,CurrentPath3,ObsticleList,MountainList,WaterList):
    global BestCost3
    global BestPath3
    global AllCost3
    global AllPath3
    global Temp_AllCost3
    global Temp_AllPath3
    global TotalPath3

    ###Condition to Terminate the Recursive Function
    #First condition : if we reach the goal
    if CurrentPos3==SingleGoal3:
        Temp_AllPath3.append(CurrentPath3)
        Temp_AllCost3.append(CurrentCost3)
        return

    if len(Temp_AllPath3)>=3:
        return

    ###To calculate the Heuristic for all possible moves
    Heuristic_Right_Move=float('inf')
    Heuristic_Bottom_Right_Move=float('inf')
    Heuristic_Bottom_Move=float('inf')
    Heuristic_Bottom_Left_Move=float('inf')
    Heuristic_Left_Move=float('inf')
    Heuristic_Top_Left_Move=float('inf')
    Heuristic_Top_Move=float('inf')
    Heuristic_Top_Right_Move=float('inf')
    list_Heuristic_Values=[float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
    list_Heuristic_Index=[1,2,3,4,5,6,7,8]
    
    #######Move cost calculation
    #Right_Move
    if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+0] not in ObsticleList and (0<=(CurrentPos3[0]+EachBlockWeight)) and ((CurrentPos3[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]+0)) and ((CurrentPos3[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Right_Move=math.sqrt((SingleGoal3[0]-(CurrentPos3[0]+EachBlockWeight))**2+((SingleGoal3[1]-(CurrentPos3[1]+0)))**2)
        #if next position is a mountain
        if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+0] in MountainList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+0] in WaterList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[0]=Heuristic_Right_Move+GreenCost
            
    #Bottom_Right_Move
    if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos3[0]+EachBlockWeight)) and ((CurrentPos3[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]+EachBlockHeight)) and ((CurrentPos3[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Right_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]+EachBlockWeight)))**2+((SingleGoal3[1]-(CurrentPos3[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+GreenCost
            
    #Bottom_Move
    if [CurrentPos3[0]+0,CurrentPos3[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos3[0]+0)) and ((CurrentPos3[0]+0)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]+EachBlockHeight)) and ((CurrentPos3[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]+0)))**2+((SingleGoal3[1]-(CurrentPos3[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in MountainList:
           list_Heuristic_Values[2]=Heuristic_Bottom_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+GreenCost

    #Bottom_Left_Move
    if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+EachBlockHeight] not in ObsticleList and (0<=(CurrentPos3[0]-EachBlockWeight)) and ((CurrentPos3[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]+EachBlockHeight)) and ((CurrentPos3[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Left_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]-EachBlockWeight)))**2+((SingleGoal3[1]-(CurrentPos3[1]+EachBlockHeight)))**2)
        list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move
        #if next position is a mountain
        if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+GreenCost

    #Left_Move
    if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+0] not in ObsticleList and (0<=(CurrentPos3[0]-EachBlockWeight)) and ((CurrentPos3[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]+0)) and ((CurrentPos3[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Left_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]-EachBlockWeight)))**2+((SingleGoal3[1]-(CurrentPos3[1]+0)))**2)
        list_Heuristic_Values[4]=Heuristic_Left_Move
        #if next position is a mountain
        if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+0] in MountainList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]+0] in WaterList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[4]=Heuristic_Left_Move+GreenCost

    #Top_Left_Move
    if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]-EachBlockHeight] not in ObsticleList  and (0<=(CurrentPos3[0]-EachBlockWeight)) and ((CurrentPos3[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]-EachBlockHeight)) and ((CurrentPos3[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Left_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]-EachBlockWeight)))**2+((SingleGoal3[1]-(CurrentPos3[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[5]=Heuristic_Top_Left_Move
        #if next position is a mountain
        if [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]-EachBlockWeight,CurrentPos3[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+GreenCost

    #Top_Move
    if [CurrentPos3[0]-0,CurrentPos3[1]-EachBlockHeight] not in ObsticleList and (0<=(CurrentPos3[0]-0)) and ((CurrentPos3[0]-0)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]-EachBlockHeight)) and ((CurrentPos3[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]-0)))**2+((SingleGoal3[1]-(CurrentPos3[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[6]=Heuristic_Top_Move
        #if next position is a mountain
        if [CurrentPos3[0]-0,CurrentPos3[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]-0,CurrentPos3[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[6]=Heuristic_Top_Move+GreenCost

    #Top_Right_Move
    if [CurrentPos3[0]+EachBlockWeight,CurrentPos3[1]-EachBlockHeight] not in ObsticleList and (0<=(CurrentPos3[0]+EachBlockWeight)) and ((CurrentPos3[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos3[1]-EachBlockHeight)) and ((CurrentPos3[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Right_Move=math.sqrt(((SingleGoal3[0]-(CurrentPos3[0]+EachBlockWeight)))**2+((SingleGoal3[1]-(CurrentPos3[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[7]=Heuristic_Top_Right_Move
        #if next position is a mountain
        if [CurrentPos3[0]-0,CurrentPos3[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos3[0]-0,CurrentPos3[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+GreenCost
        
        

    ###Sorting of Heuristic values by using selection sort in Ascending Order
    for i in range(len(list_Heuristic_Values)):
        key=i
        for j in range(i+1,len(list_Heuristic_Index)):
            if list_Heuristic_Values[key]>list_Heuristic_Values[j]:
                key=j
        list_Heuristic_Values[i],list_Heuristic_Values[key]=list_Heuristic_Values[key],list_Heuristic_Values[i]
        list_Heuristic_Index[i],list_Heuristic_Index[key]=list_Heuristic_Index[key],list_Heuristic_Index[i]


    ###Calling the next three best recursive functions for next three best positions
    times=0
    for move in range(len(list_Heuristic_Index)):

        ##Conditions to Break the Loop
        #Conditon 1: If we iterater through the loop for 3 times
        if times==3:
            break
        times+=1
        #Conditon 2: If we encounter infinite value for heuristic
        if list_Heuristic_Values[move]==float('inf'):
            break

        #Prepare Variables for Recursive calls
        NewCurrentPos43=CurrentPos3[:]
        NewCurrentCost3=CurrentCost3
        NewCurrentPath3=CurrentPath3[:]

        #If Right_Move is Best Move:
        if list_Heuristic_Index[move]==1:
            NewCurrentPos43[0]=CurrentPos3[0]+EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)

        #If Right_Bottom_Move is Best Move 
        elif list_Heuristic_Index[move]==2:
            NewCurrentPos43[0]=CurrentPos3[0]+EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==3:
            NewCurrentPos43[0]=CurrentPos3[0]+0
            NewCurrentPos43[1]=CurrentPos3[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Left_Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==4:
            NewCurrentPos43[0]=CurrentPos3[0]-EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Left_Move is Best Move
        elif list_Heuristic_Index[move]==5:
            NewCurrentPos43[0]=CurrentPos3[0]-EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Left_Top_Move is Best Move
        elif list_Heuristic_Index[move]==6:
            NewCurrentPos43[0]=CurrentPos3[0]-EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Top_Move is Best Move
        elif list_Heuristic_Index[move]==7:
            NewCurrentPos43[0]=CurrentPos3[0]-0
            NewCurrentPos43[1]=CurrentPos3[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)
        #If Right_Top_Move is Best Move
        elif list_Heuristic_Index[move]==8:
            NewCurrentPos43[0]=CurrentPos3[0]+EachBlockWeight
            NewCurrentPos43[1]=CurrentPos3[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos43 in NewCurrentPath3:
                continue
            else:
                NewCurrentPath3.append(NewCurrentPos43)
                #if next position is a mountain
                if NewCurrentPos43 in MountainList:
                    NewCurrentCost3=NewCurrentCost3+MountainCost
                #if next postion is water 
                elif NewCurrentPos43 in WaterList:
                    NewCurrentCost3=NewCurrentCost3+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost3=NewCurrentCost3+GreenCost
                UnBlindedSearch_MultipleStart_SingleGoal(NewCurrentPos43,SingleGoal3,NewCurrentCost3,NewCurrentPath3,ObsticleList,MountainList,WaterList)


def Pre_Requisite_UnBlindedSearch_MultipleStart_SingleGoal(multiple_start3,SingleGoal3,EachBlockWeight,EachBlockHeight):
    global BestCost3
    global BestPath3
    global AllCost3
    global AllPath3
    global Temp_AllCost3
    global Temp_AllPath3
    for index in range(len(multiple_start3)):
        Temp_AllCost3=[]
        Temp_AllPath3=[]
        CurrentCost3=0
        CurrentPos3=multiple_start3[index]
        CurrentPath3=[CurrentPos3]
        
        UnBlindedSearch_MultipleStart_SingleGoal(CurrentPos3,SingleGoal3,CurrentCost3,CurrentPath3,ObsticleList,MountainList,WaterList)
        for i in range(len(Temp_AllCost3)):
            if BestCost3>Temp_AllCost3[i]:
                BestCost3=Temp_AllCost3[i]
                BestPath3=Temp_AllPath3[i]
                
        quicksort(Temp_AllCost3,Temp_AllPath3,0,len(Temp_AllCost3)-1)
        for j in range(len(Temp_AllCost3)//2):
            AllCost3.append(Temp_AllCost3[j])
            AllPath3.append(Temp_AllPath3[j])

        if len(AllCost3)>1000:
            quicksort(AllCost3,AllPath3,0,len(AllCost3)-1)
            AllCost3=AllCost3[:500]
            AllPath3=AllPath3[:500]
        
    
                    
def Post_Requisite_UnBlindedSearch_MultipleStart_SingleGoal():
    global AllCost3
    global AllPath3
    global BestPath3
    global BestCost3
    ###Sorting of All Solutions is descending order
    quicksort(AllCost3,AllPath3,0,len(AllCost3)-1)

"""
Driver_Code
Pre_Requisite_UnBlindedSearch_MultipleStart_SingleGoal(multiple_start3,SingleGoal3,EachBlockWeight,EachBlockHeight)
Post_Requisite_UnBlindedSearch_MultipleStart_SingleGoal()
screen.fill(green)
drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
DrawSinglePath1(BestPath3,EachBlockWeight,EachBlockHeight)
"""
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#FUNCTION FOURTH -------> FOR MULTIPLE START AND MULTIPLE GOAL
#_______________________________________________________
#FUNCTION ONE VARIABLES
multiple_start4=[]
multiple_goal4=[]

BestCost4=float('inf')
BestPath4=[]
AllCost4=[]
AllPath4=[]
Temp_AllCost4_Main=[]
Temp_AllPath4_Main=[]
Temp_AllCost4_Middle=[]
Temp_AllPath4_Middle=[]
CurrentPath_so_far4=[]
Final_Cost4=[]
Final_Path4=[]
TotalPath4=0

#FUNCTION
def UnBlindedSearch_MultipleStart_MultipleGoal(CurrentPos4,SingleGoal4,CurrentCost4,CurrentPath4,ObsticleList,MountainList,WaterList):
    global BestCost4
    global BestPath4
    global AllCost4
    global AllPath4
    global Temp_AllCost4_Main
    global Temp_AllPath4_Main
    global TotalPath4
    global Temp_AllCost4_Middle
    global Temp_AllPath4_Middle
    global CurrentPath_so_far4
    global Final_Cost4
    global Final_Path4

    ###Condition to Terminate the Recursive Function
    #First condition : if we reach the goal
    if CurrentPos4==SingleGoal4:
        Temp_AllCost4_Middle.append(CurrentCost4)
        Temp_AllPath4_Middle.append(CurrentPath4)
        TotalPath4+=1

    #Reduce this value to less than 10 for more optimial time 
    if len(Temp_AllPath4_Middle)>2:
        return
    
    #Reduce least deserving 50 percent paths
    if len(AllPath4)>=100:
        n1=len(AllCost4)
        n2=len(AllPath4)
        quicksort(AllCost4,AllPath4,0,n1-1)
        AllCost4=AllCost4[:n1//2]
        AllPath4=AllPath4[:n2//2]
        
    #Reduce least deserving finished answer
    if len(Final_Cost4)>10:
        return
        """
        n1=len(Final_Cost4)
        n2=len(Final_Path4)
        quicksort(Final_Cost4,Final_Path4,0,n1-1)
        Final_Cost4=Final_Cost4[:n1//2]
        Final_Path4=Final_Path4[:n2//2]
        """



    ###To calculate the Heuristic for all possible moves
    Heuristic_Right_Move=float('inf')
    Heuristic_Bottom_Right_Move=float('inf')
    Heuristic_Bottom_Move=float('inf')
    Heuristic_Bottom_Left_Move=float('inf')
    Heuristic_Left_Move=float('inf')
    Heuristic_Top_Left_Move=float('inf')
    Heuristic_Top_Move=float('inf')
    Heuristic_Top_Right_Move=float('inf')
    list_Heuristic_Values=[float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
    list_Heuristic_Index=[1,2,3,4,5,6,7,8]
    #Move cost calculation
    #Right_Move
    if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+0] not in ObsticleList and [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+0] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]+EachBlockWeight)) and ((CurrentPos4[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]+0)) and ((CurrentPos4[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Right_Move=math.sqrt((SingleGoal4[0]-(CurrentPos4[0]+EachBlockWeight))**2+((SingleGoal4[1]-(CurrentPos4[1]+0)))**2)
        #if next position is a mountain
        if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+0] in MountainList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+0] in WaterList:
            list_Heuristic_Values[0]=Heuristic_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[0]=Heuristic_Right_Move+GreenCost
            
    #Bottom_Right_Move
    if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] not in ObsticleList and [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]+EachBlockWeight)) and ((CurrentPos4[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]+EachBlockHeight)) and ((CurrentPos4[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Right_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]+EachBlockWeight)))**2+((SingleGoal4[1]-(CurrentPos4[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[1]=Heuristic_Bottom_Right_Move+GreenCost
            
    #Bottom_Move
    if [CurrentPos4[0]+0,CurrentPos4[1]+EachBlockHeight] not in ObsticleList and [CurrentPos4[0]+0,CurrentPos4[1]+EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]+0)) and ((CurrentPos4[0]+0)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]+EachBlockHeight)) and ((CurrentPos4[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]+0)))**2+((SingleGoal4[1]-(CurrentPos4[1]+EachBlockHeight)))**2)
        #if next position is a mountain
        if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in MountainList:
           list_Heuristic_Values[2]=Heuristic_Bottom_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[2]=Heuristic_Bottom_Move+GreenCost

    #Bottom_Left_Move
    if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+EachBlockHeight] not in ObsticleList and [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]-EachBlockWeight)) and ((CurrentPos4[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]+EachBlockHeight)) and ((CurrentPos4[1]+EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Bottom_Left_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]-EachBlockWeight)))**2+((SingleGoal4[1]-(CurrentPos4[1]+EachBlockHeight)))**2)
        list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move
        #if next position is a mountain
        if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in MountainList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+EachBlockHeight] in WaterList:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[3]=Heuristic_Bottom_Left_Move+GreenCost

    #Left_Move
    if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+0] not in ObsticleList and [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+0] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]-EachBlockWeight)) and ((CurrentPos4[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]+0)) and ((CurrentPos4[1]+0)<=(800-EachBlockHeight)):
        Heuristic_Left_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]-EachBlockWeight)))**2+((SingleGoal4[1]-(CurrentPos4[1]+0)))**2)
        list_Heuristic_Values[4]=Heuristic_Left_Move
        #if next position is a mountain
        if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+0] in MountainList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]+0] in WaterList:
            list_Heuristic_Values[4]=Heuristic_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[4]=Heuristic_Left_Move+GreenCost

    #Top_Left_Move
    if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]-EachBlockHeight] not in ObsticleList and [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]-EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]-EachBlockWeight)) and ((CurrentPos4[0]-EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]-EachBlockHeight)) and ((CurrentPos4[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Left_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]-EachBlockWeight)))**2+((SingleGoal4[1]-(CurrentPos4[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[5]=Heuristic_Top_Left_Move
        #if next position is a mountain
        if [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]-EachBlockWeight,CurrentPos4[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[5]=Heuristic_Top_Left_Move+GreenCost

    #Top_Move
    if [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] not in ObsticleList and [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]-0)) and ((CurrentPos4[0]-0)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]-EachBlockHeight)) and ((CurrentPos4[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]-0)))**2+((SingleGoal4[1]-(CurrentPos4[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[6]=Heuristic_Top_Move
        #if next position is a mountain
        if [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[6]=Heuristic_Top_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[6]=Heuristic_Top_Move+GreenCost

    #Top_Right_Move
    if [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]-EachBlockHeight] not in ObsticleList and [CurrentPos4[0]+EachBlockWeight,CurrentPos4[1]-EachBlockHeight] not in CurrentPath_so_far4 and (0<=(CurrentPos4[0]+EachBlockWeight)) and ((CurrentPos4[0]+EachBlockWeight)<=(800-EachBlockWeight)) and (0<=(CurrentPos4[1]-EachBlockHeight)) and ((CurrentPos4[1]-EachBlockHeight)<=(800-EachBlockHeight)):
        Heuristic_Top_Right_Move=math.sqrt(((SingleGoal4[0]-(CurrentPos4[0]+EachBlockWeight)))**2+((SingleGoal4[1]-(CurrentPos4[1]-EachBlockHeight)))**2)
        list_Heuristic_Values[7]=Heuristic_Top_Right_Move
        #if next position is a mountain
        if [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] in MountainList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+MountainCost
        #if next position is water
        elif [CurrentPos4[0]-0,CurrentPos4[1]-EachBlockHeight] in WaterList:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+WaterCost
        #if next position is greenary
        else:
            list_Heuristic_Values[7]=Heuristic_Top_Right_Move+GreenCost
        
        

    ###Sorting of Heuristic values by using selection sort in Ascending Order
    for i in range(len(list_Heuristic_Values)):
        key=i
        for j in range(i+1,len(list_Heuristic_Index)):
            if list_Heuristic_Values[key]>list_Heuristic_Values[j]:
                key=j
        list_Heuristic_Values[i],list_Heuristic_Values[key]=list_Heuristic_Values[key],list_Heuristic_Values[i]
        list_Heuristic_Index[i],list_Heuristic_Index[key]=list_Heuristic_Index[key],list_Heuristic_Index[i]


    ###Calling the next three best recursive functions for next three best positions
    times=0
    for move in range(len(list_Heuristic_Index)):

        ##Conditions to Break the Loop
        #Conditon 1: If we iterater through the loop for 3 times
        if times==3:
            break
        times+=1
        #Conditon 2: If we encounter infinite value for heuristic
        if list_Heuristic_Values[move]==float('inf'):
            break

        #Prepare Variables for Recursive calls
        NewCurrentPos44=CurrentPos4[:]
        NewCurrentCost4=CurrentCost4
        NewCurrentPath4=CurrentPath4[:]

        #If Right_Move is Best Move:
        if list_Heuristic_Index[move]==1:
            NewCurrentPos44[0]=CurrentPos4[0]+EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)

        #If Right_Bottom_Move is Best Move 
        elif list_Heuristic_Index[move]==2:
            NewCurrentPos44[0]=CurrentPos4[0]+EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==3:
            NewCurrentPos44[0]=CurrentPos4[0]+0
            NewCurrentPos44[1]=CurrentPos4[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Left_Bottom_Move is Best Move
        elif list_Heuristic_Index[move]==4:
            NewCurrentPos44[0]=CurrentPos4[0]-EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]+EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Left_Move is Best Move
        elif list_Heuristic_Index[move]==5:
            NewCurrentPos44[0]=CurrentPos4[0]-EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]+0
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Left_Top_Move is Best Move
        elif list_Heuristic_Index[move]==6:
            NewCurrentPos44[0]=CurrentPos4[0]-EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Top_Move is Best Move
        elif list_Heuristic_Index[move]==7:
            NewCurrentPos44[0]=CurrentPos4[0]-0
            NewCurrentPos44[1]=CurrentPos4[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)
        #If Right_Top_Move is Best Move
        elif list_Heuristic_Index[move]==8:
            NewCurrentPos44[0]=CurrentPos4[0]+EachBlockWeight
            NewCurrentPos44[1]=CurrentPos4[1]-EachBlockHeight
            #If we go back in same path, then we terminate the function calling
            if NewCurrentPos44 in NewCurrentPath4:
                continue
            else:
                NewCurrentPath4.append(NewCurrentPos44)
                #if next position is a mountain
                if NewCurrentPos44 in MountainList:
                    NewCurrentCost4=NewCurrentCost4+MountainCost
                #if next postion is water 
                elif NewCurrentPos44 in WaterList:
                    NewCurrentCost4=NewCurrentCost4+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost4=NewCurrentCost4+GreenCost
                UnBlindedSearch_MultipleStart_MultipleGoal(NewCurrentPos44,SingleGoal4,NewCurrentCost4,NewCurrentPath4,ObsticleList,MountainList,WaterList)





def Pre_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal(multiple_start4,multiple_goal4,EachBlockWeight,EachBlockHeight):
    global BestCost4
    global BestPath4
    global AllCost4
    global AllPath4
    global Temp_AllCost4_Main
    global Temp_AllPath4_Main
    global Temp_AllCost4_Middle
    global Temp_AllPath4_Middle
    global CurrentPath_so_far4
    global Final_Cost4
    global Final_Path4
    for single_temp_start4 in multiple_start4:
        CurrentPos4=[single_temp_start4[0],single_temp_start4[1]]
        firstTime=True
        for single_temp_goal4 in multiple_goal4:
            Temp_AllCost4_Middle=[]
            Temp_AllPath4_Middle=[]
            SingleGoal4=single_temp_goal4
            #For starting goal
            if firstTime==True:
                firstTime=False
                CurrentPath_so_far4=[]
                CurrentCost4=0
                CurrentPath4=[CurrentPos4]
                UnBlindedSearch_MultipleStart_MultipleGoal(CurrentPos4,SingleGoal4,CurrentCost4,CurrentPath4,ObsticleList,MountainList,WaterList)
                Temp_AllCost4_Main=Temp_AllCost4_Middle[:]
                Temp_AllPath4_Main=Temp_AllPath4_Middle[:]
                AllCost4=Temp_AllCost4_Main[:]
                AllPath4=Temp_AllPath4_Main[:]
            else:
                if len(AllPath4)==0 or len(AllCost4)==0:
                    break
                Temp_AllCost4_Middle=[]
                Temp_AllPath4_Middle=[]
                Temp_AllCost4_Main=[]
                Temp_AllPath4_Main=[]
                CurrentPath_so_far4=[]
                CurrentCost4=0
                CurrentPath4=[CurrentPos4]
                UnBlindedSearch_MultipleStart_MultipleGoal(CurrentPos4,SingleGoal4,CurrentCost4,CurrentPath4,ObsticleList,MountainList,WaterList)

                for i in range(len(AllPath4)):
                    t1_path=AllPath4[i]
                    t1_cost=AllCost4[i]
                    for j in range(len(Temp_AllPath4_Middle)):
                        t2_path=Temp_AllPath4_Middle[j][:]
                        t2_cost=Temp_AllCost4_Middle[j]
                        t_path=t1_path+t2_path
                        t_cost=t1_cost+t2_cost
                        Temp_AllPath4_Main.append(t_path)
                        Temp_AllCost4_Main.append(t_cost)
                AllCost4=Temp_AllCost4_Main[:]
                AllPath4=Temp_AllPath4_Main[:]
            CurrentPos4=single_temp_goal4
        for x in range(len(Temp_AllCost4_Main)):
            Final_Cost4.append(Temp_AllCost4_Main[x])
            Final_Path4.append(Temp_AllPath4_Main[x])
            
        Temp_AllCost4_Main=[]
        Temp_AllPath4_Main=[]
        Temp_AllCost4_Middle=[]
        Temp_AllPath4_Middle=[]
        AllPath4=[]
        AllCost4=[]
                    
def Post_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal():
    global AllCost4
    global AllPath4
    global BestPath4
    global BestCost4
    global Final_Cost4
    global Final_Path4
    
    ###Sorting of All Solutions is descending order
    quicksort(Final_Cost4,Final_Path4,0,len(Final_Cost4)-1)
    for index in range(len(Final_Cost4)):
        if BestCost4 > Final_Cost4[index]:
            BestCost4=Final_Cost4[index]
            BestPath4=Final_Path4[index]

"""
Driver_Code
Pre_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal(multiple_start4,multiple_goal4,EachBlockWeight,EachBlockHeight)
Post_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal()
screen.fill(green)
drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
DrawSinglePath1(BestPath4,EachBlockWeight,EachBlockHeight)
"""


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#FUNCTION FIFTH -------> BLINDED SEARCH ------> SINGLE START AND SINGLE GOAL
#_______________________________________________________
#FUNCTION ONE VARIABLES
single_start5=[]
SingleGoal5=[]

ans="Not Found"
order=random.sample(range(8),8)
Solution_Set_Path5=[]
Solution_Set_Cost5=[]

#FUNCTIONS
def BlindedSearch(CurrentPos5,SingleGoal5,CurrentCost5,CurrentPath5,ObsticleList,MountainList,WaterList):
    global Solution_Set_Path5
    global Solution_Set_Cost5
    global ans

    ##Conditions to Terminate the recursive calls
    if CurrentPos5==SingleGoal5:
        Solution_Set_Path5.append(CurrentPath5)
        Solution_Set_Cost5.append(CurrentCost5)
        ans="Found"
    
    if ans=="Found":
        return

    no_of_choices=0
    for choice in order:
        
        #Variable for next recursive call
        NewCurrentPos5=CurrentPos5[:]
        NewCurrentCost5=CurrentCost5
        NewCurrentPath5=CurrentPath5[:]

        #Only top three moves are implemented
        if no_of_choices==3:
            break

        if ans=="Found":
            break
        #############################################################################################
        elif choice==0:
            #Right_Move
            NewCurrentPos5[0]=CurrentPos5[0]+EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]+0
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ##############################################################################################     
        elif choice==1:
            #Bottom_Right_Move
            NewCurrentPos5[0]=CurrentPos5[0]+EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]+EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        #############################################################################################
        elif choice==2:
            #Bottom_Move
            NewCurrentPos5[0]=CurrentPos5[0]+0
            NewCurrentPos5[1]=CurrentPos5[1]+EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ############################################################################################
        elif choice==3:
            #Bottom_Left_Move
            NewCurrentPos5[0]=CurrentPos5[0]-EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]+EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ##########################################################################################
        elif choice==4:
            #Left_Move
            NewCurrentPos5[0]=CurrentPos5[0]-EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]+0
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ###########################################################################################
        elif choice==5:
            #Top_Left_Move
            NewCurrentPos5[0]=CurrentPos5[0]-EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]-EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ############################################################################################
        elif choice==6:
            #Top_Move
            NewCurrentPos5[0]=CurrentPos5[0]-0
            NewCurrentPos5[1]=CurrentPos5[1]-EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ##############################################################################################
        elif choice==7:
            #Top_Right
            NewCurrentPos5[0]=CurrentPos5[0]+EachBlockWeight
            NewCurrentPos5[1]=CurrentPos5[1]-EachBlockHeight
            if NewCurrentPos5 in NewCurrentPath5:
                continue
            elif (NewCurrentPos5 in ObsticleList) or ((0<=NewCurrentPos5[0]<=800-EachBlockWeight)==False) or ((0<=NewCurrentPos5[1]<=800-EachBlockHeight)==False):
                if ans=="Found":
                    return
                else:
                    Solution_Set_Path5.append(NewCurrentPath5)
                    Solution_Set_Cost5.append(NewCurrentCost5)
                    continue
            else:
                NewCurrentPath5.append(NewCurrentPos5)
                #if next position is a mountain
                if NewCurrentPos5 in MountainList:
                    NewCurrentCost5=NewCurrentCost5+MountainCost
                #if next postion is water 
                elif NewCurrentPos5 in WaterList:
                    NewCurrentCost5=NewCurrentCost5+WaterCost
                #if next postion is greenary
                else:
                    NewCurrentCost5=NewCurrentCost5+GreenCost
                no_of_choices+=1
                BlindedSearch(NewCurrentPos5,SingleGoal5,NewCurrentCost5,NewCurrentPath5,ObsticleList,MountainList,WaterList)
        ###############################################################################################
        else:
            print("break")
            break


def Pre_Requisite_BlindedSearch(single_start5,SingleGoal5,EachBlockWeight,EachBlockHeight):
    global BestPath5
    global BestCost5
    CurrentPos5=single_start5[:]
    CurrentPath5=[CurrentPos5]
    CurrentCost5=0
    BlindedSearch(CurrentPos5,SingleGoal5,CurrentCost5,CurrentPath5,ObsticleList,MountainList,WaterList)
    BestPath5=Solution_Set_Path5[-1]
    BestCost5=Solution_Set_Cost5[-1]
    
"""
Driver_Code
Pre_Requisite_BlindedSearch(single_start5,SingleGoal5,EachBlockWeight,EachBlockHeight)
screen.fill(green)
drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
DrawSinglePath1(BestPath5,EachBlockWeight,EachBlockHeight)

"""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#------------------------------------------------------THIRD SCREEN----------------------------------------------------------------------
#------------THIRD SCREEN ELEMENTS-------------------------
#SCREEN DIMENSIONS
SCREEN_WIDTH=1200
SCREEN_HEIGHT=800

bg_image3=pygame.image.load('BLACK.png')

bigbigfont = pygame.font.SysFont('consolas',80)
bigbigsmallfont = pygame.font.SysFont('consolas',60)
bigbigsmallsmallfont = pygame.font.SysFont('consolas',40)
bigbigbigfont = pygame.font.SysFont('consolas',100)
smallfont = pygame.font.SysFont('consolas',20)



textC1 = bigbigsmallfont.render('SPEED ' , True , black)
textC1_1 = bigbigsmallsmallfont.render('1x ' , True , black)
textC1_2 = bigbigsmallsmallfont.render('2x ' , True , black)
textC1_3 = bigbigsmallsmallfont.render('5x ' , True , black)
textC1_4 = bigbigsmallsmallfont.render('10x ' , True , black)
textC2 = bigbigsmallfont.render('STATUS ' , True , black)
textC2_1 = smallfont.render('Path : ' , True , black)
textC2_2 = smallfont.render('Cost :' , True , black)
textC2_3 = smallfont.render('Total Paths : ' , True , black)
textC3 = bigbigsmallfont.render('FORCE FINISH ' , True , black)
textC4 = bigbigfont.render('FINISH ' , True , black)
textC5 = bigbigsmallfont.render('ALL PATH ' , True , black)
textC6 = bigbigsmallfont.render('BEST PATH ' , True , black)
textC7 = smallfont.render('previous ' , True , black)
textC8 = smallfont.render('next ' , True , black)

textError_Path=smallfont.render("No Path", True , black)
textError_Cost=smallfont.render("NULL", True , black)
textError_Empty=smallfont.render("", True , black)

goal_pointer_numbering_two=1
status_1x=False
status_2x=False
status_5x=False
status_10x=False
status_BestPath=False
status_AllPath=False
left_pointer=False
right_pointer=False
left_pointer_active=False
right_pointer_active=False
sleep_time=1
no_path_error=False
no_cost_error=False
has_path=False
has_cost=False
iterativeIndex=0
AllPath_Mode=False
#---------------------------------------------------------------------------
#------------THIRD SCREEN FUNCTIONING--------------------
def ThirdScreen():
    global SwitchThree
    global NumberOfRows
    global NumberOfColumns
    global EachBlockWeight
    global EachBlockHeight
    global MountainCost
    global WaterCost
    global GreenCost
    global ObsticleList
    global MountainList
    global WaterList
    global MountainCost
    global WaterCost
    global GreenCost
    global goal_pointer_numbering_two

    global status_1x
    global status_2x
    global status_5x
    global status_10x
    global status_BestPath
    global status_AllPath
    global left_pointer
    global right_pointer
    global left_pointer_active
    global right_pointer_active
    global no_path_error
    global no_cost_error
    global has_path
    global has_cost
    global iterativeIndex
    global AllPath_Mode

    #To convert from string to int
    MountainCost=int(MountainCost)
    WaterCost=int(WaterCost)
    GreenCost=int(GreenCost)

    #SCREEN INITIATION
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
    pygame.display.set_caption('Track Trek.IO') 
    screen.fill(green)

    #SECTIONING OF SCREEN
    pygame.draw.line(screen, black, (800, 0), (800, 800), 10)
    pygame.display.update()

    if NumberOfRows >=10 and NumberOfColumns>=10:
        if NumberOfRows*EachBlockWeight>=800:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight-5
        else:
            if NumberOfRows%2==1:
                temp_width=NumberOfRows*EachBlockWeight-20
            else:
                temp_width=NumberOfRows*EachBlockWeight-5

            if NumberOfColumns%2==1:
                temp_height=NumberOfColumns*EachBlockHeight-5
            else:
                temp_height=NumberOfColumns*EachBlockHeight-5
    else:
        if NumberOfRows*EachBlockWeight>=800:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight
        else:
            temp_width=NumberOfRows*EachBlockWeight-20
            temp_height=NumberOfColumns*EachBlockHeight

    def drawGrid(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight):
        for i in range(NumberOfRows):
            for j in range(NumberOfColumns):
                rect = pygame.Rect(i*EachBlockWeight, j*EachBlockHeight,EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, black, rect, 1)

    runningThirdScreen=True
    elementsImprint=False

    #Background image
    screen.blit(bg_image3, (800, 0))

    #Imprinting the elements on to the map
    def Imprint_the_elements():
        global goal_pointer_numbering_two
        goal_pointer_numbering_two=1
        if elementsImprint==False:
            elemetsImprint=True
            for i,j in StartList:
                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, white, rect)
            for i,j in GoalList:
                textgoalindextwo=smallfont.render(str(goal_pointer_numbering_two) , True , black)
                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, yellow, rect)
                screen.blit(textgoalindextwo , (i,j))
                goal_pointer_numbering_two+=1
            
            for i,j in ObsticleList:
                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, black, rect)
            for i,j in MountainList:
                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, brown, rect)
            for i,j in WaterList:
                rect = pygame.Rect(i, j, EachBlockWeight, EachBlockHeight)
                pygame.draw.rect(screen, blue, rect)

    Imprint_the_elements()


    #################################################################
    #FUNCTION CALLING AND CALCULATION
    BestOfAllPaths=[]
    BestOfAllCosts=[]
    AllOfAllPaths=[]
    AllOfAllCosts=[]
    
    #FOR BLIND SEARCH
    if status_search[0]==True and status_start[0]==True and status_goal[0]==True:
        Pre_Requisite_BlindedSearch(StartList[0],GoalList[0],EachBlockWeight,EachBlockHeight)
        BestOfAllPaths=BestPath5[:]
        BestOfAllCosts=BestCost5
        AllOfAllPaths=Solution_Set_Path5[:]
        AllOfAllCosts=Solution_Set_Cost5[:]
    #FOR UNBLIND SEARCH
    else:
        if status_start[0]==True and status_goal[0]==True:
            Pre_Requisite_UnBlindedSearch_SingleStart_SingleGoal(StartList,GoalList,EachBlockWeight,EachBlockHeight)
            Post_Requisite_UnBlindedSearch_SingleStart_SingleGoal()
            BestOfAllPaths=BestPath1[:]
            BestOfAllCosts=BestCost1
            AllOfAllPaths=AllPath1[:]
            AllOfAllCosts=AllCost1[:]

        elif status_start[0]==True and status_goal[1]==True:
            Pre_Requisite_UnBlindedSearch_SingleStart_MultipleGoal(StartList[0],GoalList,EachBlockWeight,EachBlockHeight)
            Post_Requisite_UnBlindedSearch_SingleStart_MultipleGoal()
            BestOfAllPaths=BestPath2[:]
            BestOfAllCosts=BestCost2
            AllOfAllPaths=AllPath2[:]
            AllOfAllCosts=AllCost2[:]

        elif status_start[1]==True and status_goal[0]==True:
            Pre_Requisite_UnBlindedSearch_MultipleStart_SingleGoal(StartList,GoalList[0],EachBlockWeight,EachBlockHeight)
            Post_Requisite_UnBlindedSearch_MultipleStart_SingleGoal()
            BestOfAllPaths=BestPath3[:]
            BestOfAllCosts=BestCost3
            AllOfAllPaths=AllPath3[:]
            AllOfAllCosts=AllCost3[:]

        elif status_start[1]==True and status_goal[1]==True:
            Pre_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal(StartList,GoalList,EachBlockWeight,EachBlockHeight)
            Post_Requisite_UnBlindedSearch_MultipleStart_MultipleGoal()
            BestOfAllPaths=BestPath4[:]
            BestOfAllCosts=BestCost4
            AllOfAllPaths=Final_Path4[:]
            AllOfAllCosts=Final_Cost4[:]

    ################################################################

    now=time.time()+0.5
    while runningThirdScreen:
        drawGrid(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
        mx,my=pygame.mouse.get_pos()

        for event in pygame.event.get():

            if pygame.mouse.get_pressed()[0]:
                
                #If Finish Button is pressed
                if  800<=mx<=1200 and 725<=my<=800 and now<time.time():
                    runningThirdScreen=False

                #if 1x Button is pressed
                if 850<=mx<=895 and 70<=my<=115:
                    if status_1x==True:
                        status_1x=False
                    else:
                        status_1x=True
                        status_2x=False
                        status_5x=False
                        status_10x=False
                        
                #if 2x Button is pressed
                if 920<=mx<=965 and 70<=my<=115:
                    if status_2x==True:
                        status_2x=False
                    else:
                        status_2x=True
                        status_1x=False
                        status_5x=False
                        status_10x=False
                #if 5x Button is pressed
                if 990<=mx<=1035 and 70<=my<=115:
                    if status_5x==True:
                        status_5x=False
                    else:
                        status_5x=True
                        status_1x=False
                        status_2x=False
                        status_10x=False
                #if 10x Button is pressed
                if 1060<=mx<=1130 and 70<=my<=115:
                    if status_10x==True:
                        status_10x=False
                    else:
                        status_10x=True
                        status_1x=False
                        status_2x=False
                        status_5x=False
                #if Best Path Button is pressed
                if 850<=mx<=1150 and 475<=my<=545:
                    if status_BestPath==True:
                        status_BestPath=False
                    else:
                        status_BestPath=True
                        status_AllPath=False
                        left_pointer=False
                        right_pointer=False
                        if len(BestOfAllPaths)==0:
                            no_path_error=True
                            no_cost_error=True
                        else:
                            if BestOfAllPaths[-1]!=GoalList[0]:
                                no_path_error=False
                                no_cost_error=False
                            else:
                                has_path=True
                                has_cost=True
                            #UPDATE THE STATUS FOR PATH
                            pygame.draw.rect(screen,orange,[825,200,350,40])
                            screen.blit(textC2_1 , (940,200))
                            noError1=smallfont.render("YES", True , black)
                            screen.blit(noError1 , (1020,200))
                            #UPDATE THE STATUS FOR COST
                            pygame.draw.rect(screen,orange,[825,260,350,40])
                            screen.blit(textC2_2 , (940,260))
                            x=BestOfAllCosts
                            noError2=smallfont.render(str(x), True , black)
                            screen.blit(noError2 , (1020,260))
                            pygame.draw.rect(screen,green,[0,0,800,800])
                            drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
                            Imprint_the_elements()
                            DrawSinglePath(BestOfAllPaths,EachBlockWeight,EachBlockHeight)
                            
                        
                #if All path Button is pressed
                if 850<=mx<=1150 and 575<=my<=645:
                    if status_AllPath==True:
                        status_AllPath=False
                    else:
                        status_AllPath=True
                        status_BestPath=False
                        left_pointer=True
                        right_pointer=True
                        AllPath_Mode=True


                #Left Pointer
                if 875<=mx<=975 and 660<=my<=690:
                    if left_pointer==True:
                        left_pointer_active=True
                        right_pointer_active=False
                    if iterativeIndex==0:
                        continue
                    else:
                        iterativeIndex-=1
                        
                #Right Pointer
                if 1025<=mx<=1125 and 660<=my<=690:
                    if right_pointer==True:
                        right_pointer_active=True
                        left_pointer_active=False
                    if iterativeIndex==len(AllOfAllCosts)-1:
                        continue
                    else:
                        iterativeIndex+=1


            if event.type == pygame.QUIT:
                pygame.quit()

            

        #########################################
        if AllPath_Mode==True:
            pygame.draw.rect(screen,green,[0,0,800,800])
            drawGrid1(NumberOfRows,NumberOfColumns,EachBlockWeight,EachBlockHeight)
            Imprint_the_elements()
            if len(AllOfAllPaths)!=0:
                DrawMultiplePath(AllOfAllPaths[iterativeIndex],EachBlockWeight,EachBlockHeight)
        
        #1x Button becomes green
        if status_1x==True:
            pygame.draw.rect(screen,green,[850,70,45,45])
            screen.blit(textC1_1 , (850,70))
        else:
            pygame.draw.rect(screen,orange,[850,70,45,45])
            screen.blit(textC1_1 , (850,70))

        #2x Button becomes green
        if status_2x==True:
            pygame.draw.rect(screen,green,[920,70,45,45])
            screen.blit(textC1_2 , (920,70))
        else:
            pygame.draw.rect(screen,orange,[920,70,45,45])
            screen.blit(textC1_2 , (920,70))

        #5x Button becomes green
        if status_5x==True:
            pygame.draw.rect(screen,green,[990,70,45,45])
            screen.blit(textC1_3 , (990,70))
        else:
            pygame.draw.rect(screen,orange,[990,70,45,45])
            screen.blit(textC1_3 , (990,70))

        #10x Button becomes green
        if status_10x==True:
            pygame.draw.rect(screen,green,[1060,70,70,45])
            screen.blit(textC1_4 , (1060,70))
        else:
            pygame.draw.rect(screen,orange,[1060,70,70,45])
            screen.blit(textC1_4 , (1060,70))

        #Best path button becomes green
        if status_BestPath==True:
            pygame.draw.rect(screen,green,[850,475,300,70])
            screen.blit(textC6 , (850,475))
        else:
            pygame.draw.rect(screen,orange,[850,475,300,70])
            screen.blit(textC6 , (850,475))

        #All path button becomes green
        if status_AllPath==True:
            pygame.draw.rect(screen,green,[850,575,300,70])
            screen.blit(textC5 , (865,575))
        else:
            pygame.draw.rect(screen,orange,[850,575,300,70])
            screen.blit(textC5 , (865,575))

        #Left pointer
        if left_pointer==True:
            if left_pointer_active==True:
                pygame.draw.rect(screen,green,[875,660,100,30])
                screen.blit(textC7 , (875,660))
            else:
                pygame.draw.rect(screen,orange,[875,660,100,30])
                screen.blit(textC7 , (875,660))
        else:
            pygame.draw.rect(screen,black,[875,660,100,30])
        #Right pointer
        if right_pointer==True:
            if right_pointer_active==True:
                pygame.draw.rect(screen,green,[1025,660,100,30])
                screen.blit(textC8 , (1045,660))
            else:
                pygame.draw.rect(screen,orange,[1025,660,100,30])
                screen.blit(textC8 , (1045,660))
        else:
            pygame.draw.rect(screen,black,[1025,660,100,30])

        #Speed Heading
        pygame.draw.rect(screen,orange,[800,0,400,50])
        screen.blit(textC1 , (900,0))

        #Status Heading
        pygame.draw.rect(screen,orange,[800,130,400,50])
        screen.blit(textC2 , (890,130))
        
        ##Path
        if AllPath_Mode==False:
            pygame.draw.rect(screen,orange,[825,200,350,40])
            screen.blit(textC2_1 , (940,200))
        else:
            #DISPLAY THAT IT HAS PATH
            pygame.draw.rect(screen,orange,[825,200,350,40])
            screen.blit(textC2_1 , (940,200))
            screen.blit(textError_Cost , (1020,260))

        if has_path==True and AllPath_Mode==False:
            pygame.draw.rect(screen,orange,[825,200,350,40])
            screen.blit(textC2_1 , (940,200))
            noError1=smallfont.render("YES", True , black)
            screen.blit(noError1 , (1020,200))
        else:
            if len(AllOfAllCosts)!=0:
                pygame.draw.rect(screen,orange,[825,200,350,40])
                screen.blit(textC2_1 , (940,200))
                noError1=smallfont.render("YES", True , black)
                screen.blit(noError1 , (1020,200))
            else:
                pygame.draw.rect(screen,orange,[825,200,350,40])
                screen.blit(textC2_1 , (940,200))
                screen.blit(textError_Cost , (1020,260))
        if no_path_error==True:
            pygame.draw.rect(screen,orange,[825,200,350,40])
            screen.blit(textC2_1 , (940,200))
            screen.blit(textError_Path , (1020,200))
                
            
        ##Cost
        if AllPath_Mode==False:
            pygame.draw.rect(screen,orange,[825,260,350,40])
            screen.blit(textC2_2 , (940,260))
        else:
            #DISPLAY THAT PATH'S COST
            if len(AllOfAllCosts)!=0:
                y=AllOfAllCosts[iterativeIndex]
                pygame.draw.rect(screen,orange,[825,260,350,40])
                screen.blit(textC2_2 , (940,260))
                noError2=smallfont.render(str(y), True , black)
                screen.blit(noError2 , (1020,260))
        if has_cost==True and AllPath_Mode==False:
            pygame.draw.rect(screen,orange,[825,260,350,40])
            x=BestOfAllCosts
            noError2=smallfont.render(str(x), True , black)
            screen.blit(noError2 , (1020,260))
        else:
            pygame.draw.rect(screen,orange,[825,260,350,40])
            screen.blit(textC2_2 , (940,260))
            if len(AllOfAllCosts)!=0:
                y=AllOfAllCosts[iterativeIndex]
                noError2=smallfont.render(str(y), True , black)
                screen.blit(noError2 , (1020,260))
        if no_cost_error==True:
            pygame.draw.rect(screen,orange,[825,260,350,40])
            screen.blit(textC2_2 , (940,260))
            screen.blit(textError_Cost , (1020,260))
            
        #Finish Heading
        pygame.draw.rect(screen,orange,[800,725,400,75])
        screen.blit(textC4 , (875,720))

        pygame.display.update()
        
        
        if runningThirdScreen==False:
            SwitchThree=True


    pygame.quit()
            
            
#---------------------------------------------------------------------------
#-------------------------------------------------------------END OF THIRD SCREEN---------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
def Reset():
    global SwitchOne
    global SwitchTwo
    global SwitchThree
    global status_start
    global status_goal
    global status_search
    global InputNumberOfRows
    global InputNumberOfColumns
    global NumberOfRows
    global NumberOfColumns
    global EachBlockWeight
    global EachBlockHeight
    global StartList
    global GoalList
    global ObsticleList
    global MountainList
    global WaterList
    global BestCost1
    global BestPath1
    global AllCost1
    global AllPath1
    global TotalPath1
    global BestCost2
    global BestPath2
    global AllCost2
    global AllPath2
    global Temp_AllCost2_Main
    global Temp_AllPath2_Main
    global Temp_AllCost2_Middle
    global Temp_AllPath2_Middle
    global CurrentPath_so_far2
    global TotalPath2
    global CurrentPath_so_far2
    global BestCost3
    global BestPath3
    global AllCost3
    global AllPath3
    global Temp_AllCost3
    global Temp_AllPath3
    global TotalPath3
    global BestCost4
    global BestPath4
    global AllCost4
    global AllPath4
    global Temp_AllCost4_Main
    global Temp_AllPath4_Main
    global Temp_AllCost4_Middle
    global Temp_AllPath4_Middle
    global CurrentPath_so_far4
    global Final_Cost4
    global Final_Path4
    global TotalPath4
    global ans
    global order
    global Solution_Set_Path5
    global Solution_Set_Cost5
    global BestPath5
    global BestCost5
    global goal_pointer_numbering_two
    global status_1x
    global status_2x
    global status_5x
    global status_10x
    global status_BestPath
    global status_AllPath
    global left_pointer
    global right_pointer
    global left_pointer_active
    global right_pointer_active
    global sleep_time
    global no_path_error
    global no_cost_error
    global has_path
    global has_cost
    global iterativeIndex
    global AllPath_Mode
    global BestOfAllPaths
    global BestOfAllCosts
    global AllOfAllPaths
    global AllOfAllCosts

    AllOfAllCosts=[]
    AllOfAllPaths=[]
    BestOfAllCosts=float('inf')
    BestOfAllPaths=[]
    SwitchOne=False
    SwitchTwo=False
    SwitchThree=False
    goal_pointer_numbering_two=1
    status_1x=False
    status_2x=False
    status_5x=False
    status_10x=False
    status_BestPath=False
    status_AllPath=False
    left_pointer=False
    right_pointer=False
    left_pointer_active=False
    right_pointer_active=False
    sleep_time=1
    no_path_error=False
    no_cost_error=False
    has_path=False
    has_cost=False
    iterativeIndex=0
    AllPath_Mode=False
    BestPath5=[]
    BestCost5=float('inf')
    ans="Not Found"
    order=random.sample(range(8),8)
    Solution_Set_Path5=[]
    Solution_Set_Cost5=[]
    BestCost4=float('inf')
    BestPath4=[]
    AllCost4=[]
    AllPath4=[]
    Temp_AllCost4_Main=[]
    Temp_AllPath4_Main=[]
    Temp_AllCost4_Middle=[]
    Temp_AllPath4_Middle=[]
    CurrentPath_so_far4=[]
    Final_Cost4=[]
    Final_Path4=[]
    TotalPath4=0
    BestCost3=float('inf')
    BestPath3=[]
    AllCost3=[]
    AllPath3=[]
    Temp_AllCost3=[]
    Temp_AllPath3=[]
    TotalPath3=0
    CurrentPath_so_far2=[]
    BestCost2=float('inf')
    BestPath2=[]
    AllCost2=[]
    AllPath2=[]
    Temp_AllCost2_Main=[]
    Temp_AllPath2_Main=[]
    Temp_AllCost2_Middle=[]
    Temp_AllPath2_Middle=[]
    CurrentPath_so_far2=[]
    TotalPath2=0
    BestCost1=float('inf')
    BestPath1=[]
    AllCost1=[]
    AllPath1=[]
    TotalPath1=0
    WaterList=[]
    MountainList=[]
    ObsticleList=[]
    GoalList=[]    
    StartList=[]
    EachBlockHeight=0
    EachBlockWeight=0
    NumberOfColumns=0
    NumberOfRows=0
    InputNumberOfColumns=""
    InputNumberOfRows=""
    status_start=[False,False]
    status_goal=[False,False]
    status_search=[False,False]
    
    



    
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#Driver code
"""
while True:
    if SwitchMain==True:
        FirstScreen()
        if SwitchOne==True:
            SecondScreen()
        if SwitchTwo==True:
            ThirdScreen()
        Reset()
    else:
        break
"""
if SwitchMain==True:
    FirstScreen()
    if SwitchOne==True:
        SecondScreen()
        print(StartList)
        print(GoalList)
        print(ObsticleList)
        print(MountainList)
        print(WaterList)
    if SwitchTwo==True:
        ThirdScreen()
    Reset()



#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

