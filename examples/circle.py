from mcpi.minecraft import Minecraft
import math
import time

mc = Minecraft.create('10.0.0.101')

mc.setting("world_immutable", False)

players = mc.getPlayerEntityIds()
me = players[1]
you = players[0]
x,y,z = mc.entity.getPos(me)
xx, yy, zz = mc.entity.getPos(you)

def drawCircle():
    mc.entity.setPos(me, x,y,z+50)

    r = 15

    for q in range(1,4):
        for i in range(0,r*6):
            j = float(i)/(r*3)

            blockXPos = r*math.cos(j*math.pi)
            blockZPos = r*math.sin(j*math.pi)

            mc.setBlock(blockXPos+x, y+q, blockZPos+z,1)

drawCircle()