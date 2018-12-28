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

def castSpell():
        mc.entity.setPos(me, x-10,y,z)
        for i in range(1,500):
                time.sleep(0.5)
                for l in range(1,50):
                        # mc.setBlock(x+l,y+math.sin(l+i-1)*3,z,0)
                        mc.setBlock(x+l,y+math.sin(l+i)*3,z,3)
                
                        

castSpell()