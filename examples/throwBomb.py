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
        for i in range(1,6):
                mc.setBlock(x,y+math.sin(i-1)*3,z+((i-1)*2),[0,0])
                mc.setBlock(x,y+math.sin(i)*3,z+(i*2),[46,1])
                time.sleep(0.2)
                
                        
castSpell()