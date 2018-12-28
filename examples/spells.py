from mcpi.minecraft import Minecraft
import math
import time

mc = Minecraft.create('10.0.0.101')

# mc.postToChat('yo mama')

players = mc.getPlayerEntityIds()
me = players[1]
you = players[0]

x,y,z = mc.entity.getPos(me)
xx, yy, zz = mc.entity.getPos(you)

def launchYou():
    mc.entity.setPos(you, xx, yy+40, zz+0)

def moveMe():
    for i in range(1,50):
        mc.entity.setPos(me, x,y,z+i)
        time.sleep(0.2)

#moveMe()

def moveYou():
    for i in range(1,50):
        mc.entity.setPos(you, x,y,z+i)
        time.sleep(0.1)

moveYou()

# mc.setBlock(x,y,z,2)