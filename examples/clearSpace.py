from mcpi.minecraft import Minecraft
import math
import time

# mc = Minecraft.create('10.0.0.101')
mc = Minecraft.create()

# mc.postToChat('yo mama')

players = mc.getPlayerEntityIds()
me = players[0]
you = players[0]

x,y,z = mc.entity.getPos(me)
xx, yy, zz = mc.entity.getPos(you)

def clearSpace():
        mc.setBlocks(x+3,y+3,z+3,x-3,y-3,z-3,0)

clearSpace()