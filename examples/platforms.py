from mcpi.minecraft import Minecraft
import math
import time

mc = Minecraft.create('10.0.0.101')
# mc = Minecraft.create()

# mc.postToChat('yo mama')

players = mc.getPlayerEntityIds()
me = players[0]
you = players[0]

x,y,z = mc.entity.getPos(me)
xx, yy, zz = mc.entity.getPos(you)

pX = int(x)
pY = int(y)-1
pZ = int(z)
y -= 1

trigger = 0

def setPlatform():
        global trigger
        mc.entity.setPos(me, x-10,y+1,z)
        mc.setBlocks(x+1,y,z+1,x-1,y,z-1,4)
        mc.setBlock(x,y,z,5)
        trigger = mc.getBlock(x,y,z)

def gameLoop():
        global trigger

        while 0 != 1:
                a,b,c = mc.player.getPos()
                if int(a) == pX and (int(b)-1) == pY and int(c) == pZ:
                        throwBomb()


        # castSpell()
        # print('done')
                
def throwBomb():
        for i in range(1,6):
                mc.setBlock(x,y+math.sin(i-1)*3,z+((i-1)*2),[0,0])
                mc.setBlock(x,y+math.sin(i)*3,z+(i*2),[46,1])
                time.sleep(0.2)

def castSpell():
        
        for i in range(1,500):
                time.sleep(0.5)
                for l in range(1,50):
                        # mc.setBlock(x+l,y+math.sin(l+i-1)*3,z,0)
                        mc.setBlock(x+l,y+math.sin(l+i)*3,z,3)
                
                        
setPlatform()
gameLoop()