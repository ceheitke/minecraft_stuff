from mcpi.minecraft import Minecraft
import math
import time

# mc = Minecraft.create('10.0.0.101')
mc = Minecraft.create()

# mc.postToChat('yo mama')

players = mc.getPlayerEntityIds()
me = players[0]
you = players[0]

# x,y,z = mc.entity.getPos(me)
x = 240
y = 143
z = 38

xx, yy, zz = mc.entity.getPos(you)

mc.entity.setPos(me, x, y + 8, z)

courtXmin = x
courtZmin = z-1
courtXmax = x + 26
courtZmax = z - 1 + 22
courtY = y

def makeCourt():
    mc.camera.setFollow(me)

    # walls
    mc.setBlocks(courtXmin - 1, courtY, courtZmin - 1, courtXmax + 1, courtY + 3, courtZmax + 1, 17)
    mc.setBlocks(courtXmin, courtY, courtZmin, courtXmax, courtY + 3, courtZmax, 0)
    mc.setBlocks(courtXmin, courtY, courtZmin, courtXmax, courtY, courtZmax, [35, 13])

    # lines
    # vertical lines
    mc.setBlocks(courtXmin + 3, courtY, courtZmin + 3, courtXmax - 3, courtY, courtZmin + 3, [35, 0])
    mc.setBlocks(courtXmin + 3, courtY, courtZmin + 6, courtXmax - 3, courtY, courtZmin + 6, [35, 0])
    mc.setBlocks(courtXmin + 3, courtY, courtZmax - 3, courtXmax - 3, courtY, courtZmax - 3, [35, 0])
    mc.setBlocks(courtXmin + 3, courtY, courtZmax - 6, courtXmax - 3, courtY, courtZmax - 6, [35, 0])

    mc.setBlocks(courtXmin + 8, courtY, courtZmax - 11, courtXmax - 8, courtY, courtZmax - 11, [35, 0])
    mc.setBlocks(courtXmin + 4, courtY, courtZmax - 11, courtXmin + 4, courtY, courtZmax - 11, [35, 0])
    mc.setBlocks(courtXmax - 4, courtY, courtZmax - 11, courtXmax - 4, courtY, courtZmax - 11, [35, 0])

    # base lines
    mc.setBlocks(courtXmin + 3, courtY, courtZmin + 3, courtXmin + 3, courtY, courtZmax - 3, [35, 0])
    mc.setBlocks(courtXmin + 8, courtY, courtZmin + 6, courtXmin + 8, courtY, courtZmax - 6, [35, 0])
    mc.setBlocks(courtXmax - 8, courtY, courtZmin + 6, courtXmax - 8, courtY, courtZmax - 6, [35, 0])
    mc.setBlocks(courtXmax - 3, courtY, courtZmin + 3, courtXmax - 3, courtY, courtZmax - 3, [35, 0])
    
    # net
    mc.setBlocks(courtXmax - 13, courtY, courtZmin + 2, courtXmax - 13, courtY, courtZmax - 2, [35, 15])
    mc.setBlocks(courtXmax - 13, courtY, courtZmin + 3, courtXmax - 13, courtY, courtZmax - 3, [35, 0])

makeCourt()