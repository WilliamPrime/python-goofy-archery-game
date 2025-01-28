
#s(t) = -gt + vt + h
# this works when s(t) is the hight (Y)  at any given time (t)
# g is the gravitational constant, i will use 9.81ms^-2
# v is the intial velocity of the projectile
# h is the initial starting height of the projectile

#for the vertical axis
# a = -9.81
# v = -9.81t + c        where c is the starting velocity
#   


#im making this project for fun and to test how fisable this is to do as a project for a school examination

#since for this project im not allowed to use any libraries other than random,time,math im doing to all my graphics with ascii art

import math
import time
import random

initialTime=0
gravity=9.81  #i aim to add different planets so gravity as a variable will be helpful
initialVelocity=0
launchAngle=0
pi=math.pi
#find the x and y components of the initial velocity


#projectileRange=0
def physicsCalc(g,velo,angle):
    #global projectileRange
    try:
        global initialX
        global initialY
        initialX=math.cos((angle/180)*pi)*velo
        initialY=math.sin((angle/180)*pi)*velo
        #print(initialX, "x velocity at t==0")
        #print(initialY, "y velocity at t==0")
        return initialX,initialY
    except:
        print("uh oh the maths didnt work")
    
physicsCalc(gravity,initialVelocity,launchAngle)
    
def yFinder(x,initialX,initialY):
    time=float(x)/float(initialX)
    y=-((gravity/2)*(time**2))+initialY*time
    return y



########################################################################################################################################################################## 
##########################################################################################################################################################################
##########################################################################################################################################################################
########## these decide how the graphics part of the programme displays stuff#############################################################################################
emptyCell="."
fullCell="#"
upCell="\u2215"
levelCell="-"
downCell="\u29F5"
target="|"
dynamicProjectile="o"

#BOARD STYLE
boardColumns=120
boardRows=30   #20:9 is square aspect ratio for ascii


#TARGET INFO
targetCentre=[60,6] #if location= set  this is exactly the centre of where the target is, if this is random, its completely random and this is ignored, if its algorthm it places somewhere up or down 90% down the board
targetHeight=5 #how many up and down of the centre are also target
targetLocation="random"   #set to "random" or "set"  


########################################################################################################################################################################## 
########################################################################################################################################################################## 
########################################################################################################################################################################## 
########################################################################################################################################################################## 

def upOrDown(x,initialX,initialY):
    global dynamicProjectile
    lower_threshold=-0.3
    upper_threshold=0.3
    time=float(x)/float(initialX)
    velocity=(initialY-time*gravity)
    #print(velocity)
    if velocity>upper_threshold:
        dynamicProjectile=upCell
    elif velocity<lower_threshold:
        dynamicProjectile=downCell
    else:
        dynamicProjectile=levelCell
    return dynamicProjectile



class renderer():
    def __init__(self,columns,rows):
        self.content = [[emptyCell]*rows for _ in range(columns)]

    def makeCleanBoard(self,columns,rows):
        self.content = [[emptyCell]*rows for _ in range(columns)]

    def showBoard(self):
        print("shwoing board")
        for j in range(0,len(self.content[0])):
            line=""
            for i in range(0,len(self.content)):
                line=line+str(self.content[i][j])
            print(line)

    def editSquare(self,x,y,newValue):
        #print("marking ",x,",",y," ",newValue)      # line was here to debug
        if x in range(0,boardColumns) and (boardRows-y) in range(0,boardRows):
            self.content[x][boardRows-y]=newValue
    def returnCell(self,x,y):
        try:
            return self.content[x][boardRows-y]
        except:
            pass
        #just returns the cell value


oRenderer=renderer(boardColumns,boardRows)


def plotter(initialX,initialY):
    for i in range(0,boardColumns):
        oRenderer.editSquare(i,(round(yFinder(i,initialX,initialY))),upOrDown(i,initialX,initialY))




def targetPlacer(center,size,type):
    size=round(size)
    #print(targetLocation) # more internal data checking
    if type=="set":
        global targetX
        global targetY
        targetX=center[0]
        targetY=center[1]
        center=[targetX,targetY]
        #print(center)
        for x in range(1,size+1):
            #print(x)
            #print(x) monitoring how the data worked
            #oRenderer.editSquare(targetX,targetX,target)
            if x%2==0:
                oRenderer.editSquare((center[0]),(center[1]-x) +x//2,target)
                print("top")
            if x%2==1:
                oRenderer.editSquare((center[0]),(center[1]+x -(x//2) -1),target)
                print("bottom")
            oRenderer.editSquare((center[0]-1),(center[1]),"@")  # debugging lines to place and @ symbol one to the left of the centre to check the centre is where i think it is
            print()


    elif type=="random":
        #print("haiii")

        targetX=random.randint(round(boardColumns*0.7),boardColumns-1)
        targetY=random.randint(0,boardRows-1)

        center=[targetX,targetY]
        #print(center)
        for x in range(1,size+1):
            #print(x)
            #print(x) monitoring how the data worked
            #oRenderer.editSquare(targetX,targetX,target)
            if x%2==0:
                oRenderer.editSquare((center[0]),(center[1]-x) +x//2,target)
            if x%2==1:
                oRenderer.editSquare((center[0]),(center[1]+x -(x//2) -1),target)
            oRenderer.editSquare((center[0]-1),(center[1]),"@")  # debugging lines to place and @ symbol one to the left of the centre to check the centre is where i think it is


#returns true if one the values isnt what it was looking for
# i can use this for hit detection            
def checker(centerX,centerY,size,checkFor):
    center=[centerX,centerY]
    for x in range(1,size+1):
        #print(x)
        #print(x) monitoring how the data worked
            #oRenderer.editSquare(targetX,targetX,target)
        if x%2==0:
            if oRenderer.returnCell((center[0]),(center[1]-x) +x//2)!=checkFor:
                return True
        elif x%2==1:
            if oRenderer.returnCell((center[0]),(center[1]+x -(x//2) -1),) !=checkFor:
                return True
    return False
        
        



#targetPlacer(targetCentre,targetHeight,targetLocation,boardColumns,boardRows)
#oRenderer.showBoard()
#plotter(initialX,initialY)        
#oRenderer.showBoard()

for l in range(0,10):
    oRenderer.makeCleanBoard(boardColumns,boardRows)
    targetPlacer(targetCentre,targetHeight,targetLocation,)
    oRenderer.showBoard()   
    userVelocity=float(input("please enter the speed"))
    userLaunchAngle=float(input("please enter the launch angle"))
    initialX=physicsCalc(gravity,userVelocity,userLaunchAngle)[0]
    initialY=physicsCalc(gravity,userVelocity,userLaunchAngle)[1]
    plotter(initialX,initialY)
    oRenderer.showBoard()
    
    if checker(targetX,targetY,targetHeight,target)==True:
        print("you hit the target well done")
    elif checker(targetX,targetY,targetHeight,target)==False:
        print("welp, you missed the target")
    else:
        print("uh ohh buddy you messed up")
    time.sleep(10)

#user1=float(input("user1"))
#user2=float(input("user2"))
#physicsCalc(gravity,user1,user2)


def mainMenu():
    pass

menu="mainMenu"
inMenu=True
while inMenu==True:
    if menu=="mainMenu":
        pass
    elif menu != "mainMenu":
        pass

