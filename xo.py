from vpython import *
import numpy as np
import serial
import time
oBox = sphere(radius=0.93,color=color.red,pos=vector(0,0,0),opacity=0.001)
xBox1 = box(size=vector(2,0.3,1.2),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(0,0,0),opacity=0.001)
xBox2 = box(size=vector(2,0.3,1.2),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(0,0,0),opacity=0.001)
positions=[0,0,0,0,0,0,0,0,0]
oPos1 = sphere(radius=0.001,color=color.red,pos=vector(-2,2,0))
oPos2 = sphere(radius=0.001,color=color.red,pos=vector(0,2,0))
oPos3 = sphere(radius=0.001,color=color.red,pos=vector(2,2,0))
oPos4 = sphere(radius=0.001,color=color.red,pos=vector(-2,0,0))
oPos5 = sphere(radius=0.001,color=color.red,pos=vector(0,0,0))
oPos6 = sphere(radius=0.001,color=color.red,pos=vector(2,0,0))
oPos7 = sphere(radius=0.001,color=color.red,pos=vector(-2,-2,0))
oPos8 = sphere(radius=0.001,color=color.red,pos=vector(0,-2,0))
oPos9 = sphere(radius=0.001,color=color.red,pos=vector(2,-2,0))
xPos1 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(-2,2,0))
xpos1 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(-2,2,0))
xPos2 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(0,2,0))
xpos2 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(0,2,0))
xPos3 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(2,2,0))
xpos3 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(2,2,0))
xPos4 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(-2,0,0))
xpos4 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(-2,0,0))
xPos5 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(0,0,0))
xpos5 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(0,0,0))
xPos6 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(2,0,0))
xpos6 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(2,0,0))
xPos7 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(-2,-2,0))
xpos7 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(-2,-2,0))
xPos8 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(0,-2,0))
xpos8 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(0,-2,0))
xPos9 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(2,-2,0))
xpos9 = box(size=vector(0.001,0.001,0.001),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(2,-2,0))




def outerGrid():
    upperBoxWidth=6
    upperBoxLength=0.1
    upperBoxDepth=2

    lowerBoxWidth=6
    lowerBoxLength=0.1
    lowerBoxDepth=2

    rightBoxWidth=0.1
    rightBoxLength=6
    rightBoxDepth=2

    leftBoxWidth=0.1
    leftBoxLength=6
    leftBoxDepth=2

    upperGrid=box(size=vector(upperBoxWidth,upperBoxLength,upperBoxDepth),pos=vector(0,1,0))
    lowerGrid=box(size=vector(lowerBoxWidth,lowerBoxLength,lowerBoxDepth),pos=vector(0,-1,0))
    rightGrid=box(size=vector(rightBoxWidth,rightBoxLength,rightBoxDepth),pos=vector(1,0,0))
    leftGrid=box(size=vector(leftBoxWidth,leftBoxLength,leftBoxDepth),pos=vector(-1,0,0))

def selectionBox(x,y,z,chance,obj1,obj2,obj3):
    if str(chance%2) == "0":
        obj2.opacity=0.001
        obj3.opacity=0.001
        obj1.opacity=0.3
        obj1.pos=vector(x,y,z)

    else:
        obj1.opacity=0.001
        obj2.opacity=0.3
        obj3.opacity=0.3
        obj2.pos=vector(x,y,z)
        obj3.pos=vector(x,y,z)
    
def xcreation(position):
    if position == "1":
        xPos1.size=vector(2,0.3,1.2)
        xpos1.size=vector(2,0.3,1.2)

    if position == "2":
        xPos2.size=vector(2,0.3,1.2)
        xpos2.size=vector(2,0.3,1.2)

    if position == "3":
        xPos3.size=vector(2,0.3,1.2)
        xpos3.size=vector(2,0.3,1.2)

    if position == "4":
        xPos4.size=vector(2,0.3,1.2)
        xpos4.size=vector(2,0.3,1.2)

    if position == "5":
        xPos5.size=vector(2,0.3,1.2)
        xpos5.size=vector(2,0.3,1.2)

    if position == "6":
        xPos6.size=vector(2,0.3,1.2)
        xpos6.size=vector(2,0.3,1.2)

    if position == "7":
        xPos7.size=vector(2,0.3,1.2)
        xpos7.size=vector(2,0.3,1.2)

    if position == "8":
        xPos8.size=vector(2,0.3,1.2)
        xpos8.size=vector(2,0.3,1.2)

    if position == "9":
        xPos9.size=vector(2,0.3,1.2)
        xpos9.size=vector(2,0.3,1.2)

    if str(position) == "11":
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos1.pos=vector(-2,2,location)
            xpos1.pos=vector(-2,2,location)
        xPos1.color=vector(0.627,0.125,0.941)
        xpos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos2.pos=vector(0,2,location)
            xpos2.pos=vector(0,2,location)
        xPos2.color=vector(0.627,0.125,0.941)
        xpos2.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos3.pos=vector(2,2,location)
            xpos3.pos=vector(2,2,location)
        xPos3.color=vector(0.627,0.125,0.941)
        xpos3.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,2,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 12:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos4.pos=vector(-2,0,location)
            xpos4.pos=vector(-2,0,location)
        xPos4.color=vector(0.627,0.125,0.941)
        xpos4.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos5.pos=vector(0,0,location)
            xpos5.pos=vector(0,0,location)
        xPos5.color=vector(0.627,0.125,0.941)
        xpos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos6.pos=vector(2,0,location)
            xpos6.pos=vector(2,0,location)
        xPos6.color=vector(0.627,0.125,0.941)
        xpos6.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,0,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 13:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos7.pos=vector(-2,-2,location)
            xpos7.pos=vector(-2,-2,location)
        xPos7.color=vector(0.627,0.125,0.941)
        xpos7.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos8.pos=vector(0,-2,location)
            xpos8.pos=vector(0,-2,location)
        xPos8.color=vector(0.627,0.125,0.941)
        xpos8.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos9.pos=vector(2,-2,location)
            xpos9.pos=vector(2,-2,location)
        xPos9.color=vector(0.627,0.125,0.941)
        xpos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,-2,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 14:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos1.pos=vector(-2,2,location)
            xpos1.pos=vector(-2,2,location)
        xPos1.color=vector(0.627,0.125,0.941)
        xpos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos4.pos=vector(-2,0,location)
            xpos4.pos=vector(-2,0,location)
        xPos4.color=vector(0.627,0.125,0.941)
        xpos4.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos7.pos=vector(-2,-2,location)
            xpos7.pos=vector(-2,-2,location)
        xPos7.color=vector(0.627,0.125,0.941)
        xpos7.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-2,-3.2,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.9,1000):
            rate(900)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 15:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos2.pos=vector(0,2,location)
            xpos2.pos=vector(0,2,location)
        xPos2.color=vector(0.627,0.125,0.941)
        xpos2.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos5.pos=vector(0,0,location)
            xpos5.pos=vector(0,0,location)
        xPos5.color=vector(0.627,0.125,0.941)
        xpos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos8.pos=vector(0,-2,location)
            xpos8.pos=vector(0,-2,location)
        xPos8.color=vector(0.627,0.125,0.941)
        xpos8.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(0,-3.05,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.85,1000):
            rate(900)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 16:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos3.pos=vector(2,2,location)
            xpos3.pos=vector(2,2,location)
        xPos3.color=vector(0.627,0.125,0.941)
        xpos3.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos6.pos=vector(2,0,location)
            xpos6.pos=vector(2,0,location)
        xPos6.color=vector(0.627,0.125,0.941)
        xpos6.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos9.pos=vector(2,-2,location)
            xpos9.pos=vector(2,-2,location)
        xPos9.color=vector(0.627,0.125,0.941)
        xpos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(2,-3.05,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.85,1000):
            rate(900)
            piercing.length=location
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 17:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos1.pos=vector(-2,2,location)
            xpos1.pos=vector(-2,2,location)
        xPos1.color=vector(0.627,0.125,0.941)
        xpos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos5.pos=vector(0,0,location)
            xpos5.pos=vector(0,0,location)
        xPos5.color=vector(0.627,0.125,0.941)
        xpos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos9.pos=vector(2,-2,location)
            xpos9.pos=vector(2,-2,location)
        xPos9.color=vector(0.627,0.125,0.941)
        xpos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(3.5,-3.5,3),color=vector(1,0.898,0.706),axis=vector(3,-3,0))
        for location in np.linspace(0.5,9.89,1000):
            rate(900)
            piercing.length=location
            piercing.axis=vector(-(location/(2**(1/2))),(location/(2**(1/2))),0)
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 18:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            xPos3.pos=vector(2,2,location)
            xpos3.pos=vector(2,2,location)
        xPos3.color=vector(0.627,0.125,0.941)
        xpos3.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos5.pos=vector(0,0,location)
            xpos5.pos=vector(0,0,location)
        xPos5.color=vector(0.627,0.125,0.941)
        xpos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            xPos7.pos=vector(-2,-2,location)
            xpos7.pos=vector(-2,-2,location)
        xPos7.color=vector(0.627,0.125,0.941)
        xpos7.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.5,-3.5,3),color=vector(1,0.898,0.706),axis=vector(-3,-3,0))
        for location in np.linspace(0.5,9.89,1000):
            rate(900)
            piercing.length=location
            piercing.axis=vector((location/(2**(1/2))),(location/(2**(1/2))),0)
        text(text=('X - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass
    

def Draw():
    text(text=('MATCH IS DRAWN'),height=1,pos=vector(-5.5,-0.75,3),color=vector(0.627,0.125,0.941))
    while True:
        pass


def continueOrNot(positions):
    noProb=0
    for i in range(0,9,1):
        #print(" Value of I is",i)
        #print("Type of positions[i] is",type(positions[i]))
        if str(positions[i]) == "0":
            noProb = noProb+1
    if noProb>=1:
        return 0
    else:
        Draw()
  
def winOrNot():
    if(positions[0]=='x' and positions[1]=='x' and positions[2]=='x'):
        xcreation(11)
    elif(positions[3]=='x' and positions[4]=='x' and positions[5]=='x'):
        xcreation(12)
    elif(positions[6]=='x' and positions[7]=='x' and positions[8]=='x'):
        xcreation(13)
    elif(positions[0]=='x' and positions[3]=='x' and positions[6]=='x'):
        xcreation(14)
    elif(positions[1]=='x' and positions[4]=='x' and positions[7]=='x'):
        xcreation(15)
    elif(positions[2]=='x' and positions[5]=='x' and positions[8]=='x'):
        xcreation(16)
    elif(positions[0]=='x' and positions[4]=='x' and positions[8]=='x'):
        xcreation(17)
    elif(positions[2]=='x' and positions[4]=='x' and positions[6]=='x'):
        xcreation(18)
    elif(positions[0]=='o' and positions[1]=='o' and positions[2]=='o'):
        ocreation(11)
    elif(positions[3]=='o' and positions[4]=='o' and positions[5]=='o'):
        ocreation(12)
    elif(positions[6]=='o' and positions[7]=='o' and positions[8]=='o'):
        ocreation(13)
    elif(positions[0]=='o' and positions[3]=='o' and positions[6]=='o'):
        ocreation(14)
    elif(positions[1]=='o' and positions[4]=='o' and positions[7]=='o'):
        ocreation(15)
    elif(positions[2]=='o' and positions[5]=='o' and positions[8]=='o'):
        ocreation(16)
    elif(positions[0]=='o' and positions[4]=='o' and positions[8]=='o'):
        ocreation(17)
    elif(positions[2]=='o' and positions[4]=='o' and positions[6]=='o'):
        ocreation(18)
    else:
        return 0

def ocreation(position):

    if position == "1":
        oPos1.opacity=1
        oPos1.radius=0.93

    if position == "2":
        oPos2.opacity=1
        oPos2.radius=0.93

    if position == "3":
        oPos3.opacity=1
        oPos3.radius=0.93

    if position == "4":
        oPos4.opacity=1
        oPos4.radius=0.93    

    if position == "5":
        oPos5.opacity=1
        oPos5.radius=0.93

    if position == "6":
        oPos6.opacity=1
        oPos6.radius=0.93

    if position == "7":
        oPos7.opacity=1
        oPos7.radius=0.93

    if position == "8":
        oPos8.opacity=1
        oPos8.radius=0.93

    if position == "9":
        oPos9.opacity=1
        oPos9.radius=0.93
    
    if int(position) == 11:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos1.pos=vector(-2,2,location)
        oPos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos2.pos=vector(0,2,location)
        oPos2.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos3.pos=vector(2,2,location)
        oPos3.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,2,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 12:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos4.pos=vector(-2,0,location)
        oPos4.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos5.pos=vector(0,0,location)
        oPos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos6.pos=vector(2,0,location)
        oPos6.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,0,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 13:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos7.pos=vector(-2,-2,location)
        oPos7.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos8.pos=vector(0,-2,location)
        oPos8.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos9.pos=vector(2,-2,location)
        oPos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.7,-2,3),color=vector(1,0.898,0.706))
        for location in np.linspace(0.5,7.3,1000):
            rate(800)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 14:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos1.pos=vector(-2,2,location)
        oPos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos4.pos=vector(-2,0,location)
        oPos4.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos7.pos=vector(-2,-2,location)
        oPos7.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-2,-3.2,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.9,1000):
            rate(900)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5,0),height=1)
        while True:
            pass

    if int(position) == 15:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos2.pos=vector(0,2,location)
        oPos2.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos5.pos=vector(0,0,location)
        oPos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos8.pos=vector(0,-2,location)
        oPos8.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(0,-3.05,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.85,1000):
            rate(900)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 16:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos3.pos=vector(2,2,location)
        oPos3.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos6.pos=vector(2,0,location)
        oPos6.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos9.pos=vector(2,-2,location)
        oPos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(2,-3.05,3),color=vector(1,0.898,0.706),axis=vector(0,1,0))
        for location in np.linspace(0.5,6.85,1000):
            rate(900)
            piercing.length=location
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 17:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos1.pos=vector(-2,2,location)
        oPos1.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos5.pos=vector(0,0,location)
        oPos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos9.pos=vector(2,-2,location)
        oPos9.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(3.5,-3.5,3),color=vector(1,0.898,0.706),axis=vector(3,-3,0))
        for location in np.linspace(0.5,9.89,1000):
            rate(900)
            piercing.length=location
            piercing.axis=vector(-(location/(2**(1/2))),(location/(2**(1/2))),0)
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

    if int(position) == 18:
        oBox.opacity=0.01
        xBox1.opacity=0.01
        xBox2.opacity=0.01
        for location in np.linspace(0,3,300):
            rate(250)
            oPos3.pos=vector(2,2,location)
        oPos3.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos5.pos=vector(0,0,location)
        oPos5.color=vector(0.627,0.125,0.941)
        for location in np.linspace(0,3,300):
            rate(250)
            oPos7.pos=vector(-2,-2,location)
        oPos7.color=vector(0.627,0.125,0.941)
        piercing=arrow(length=0.5,shaftwidth=0.15,pos=vector(-3.5,-3.5,3),color=vector(1,0.898,0.706),axis=vector(-3,-3,0))
        for location in np.linspace(0.5,9.89,1000):
            rate(900)
            piercing.length=location
            piercing.axis=vector((location/(2**(1/2))),(location/(2**(1/2))),0)
        text(text=('O - WON'),color=vector(1,0.898,0.706),pos=vector(-2.4,-5.3,0),height=1)
        while True:
            pass

boxWidth=boxLength=boxDepth=2
msgBox=box(size=vector(7,1,2),pos=vector(0,-4.45,0),color=color.white,opacity=0.2)
invalidMsg1=text(text=('INVALID MOVE'),color=color.orange,pos=vector(-3.5,-5,0),height=0.8,opacity=0.001)
outerGrid()
x=0
y=0
z=0
chance=1
position=5
positions=[0,0,0,0,0,0,0,0,0]
variable='x'
oldSwitchPosition=1
switchPosition=0
mark=0
arduinoData = serial.Serial('com3',9600)
time.sleep(1)
while True:
    rate(200)
    while (arduinoData.inWaiting()==0):
        pass
    dataReceived=arduinoData.readline()
    dataReceived=str(dataReceived,'utf-8')
    dataReceived=dataReceived.strip('\r\n')
    trueData=dataReceived.split(",")
    position=trueData[0]
    oldSwitchPosition=switchPosition
    switchPosition=trueData[1]
    continueOrNot(positions)
    winOrNot()
    if (position == "1"):
        x=-2
        y=2
    if (position == "2"):
        x=0
        y=2
    if (position == "3"):
        x=2
        y=2
    if (position == "4"):
        x=-2
        y=0
    if (position == "5"):
        x=0
        y=0
    if (position == "6"):
        x=2
        y=0
    if (position == "7"):
        x=-2
        y=-2
    if position == "8":
        x=0
        y=-2
    if position == "9":
        x=2
        y=-2 
    selectionBox(x,y,z,chance,oBox,xBox1,xBox2)
    if (oldSwitchPosition == "1") and (switchPosition == "0"):
        tempMark=int(position)-1
        if str(positions[tempMark]) != "0":
            invalidMsg1.opacity=1 
        else:
            invalidMsg1.opacity=0.001
            if int(chance%2) == 0:
                ocreation(position)
                variable='o'
            if int(chance%2) == 1:
                xcreation(position)
                variable='x'
        
            chance=chance+1
            mark=int(position)-1
            positions[int(mark)]=variable   