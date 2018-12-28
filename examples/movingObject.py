from mcpi.minecraft import Minecraft
from threading import Thread
import math
import time

mc = Minecraft.create('10.0.0.101')

players = mc.getPlayerEntityIds()
me = players[0]
you = players[1]
x,y,z = mc.entity.getPos(me)
xx, yy, zz = mc.entity.getPos(you)

# vars
dir = "north"
speed = 1
objX = x
objY = y
objZ = z
objBlock = 1

def main():
    global dir
    while 1 != 0:
        cmd = input("cmd?")

        if cmd == "z":
            changeDir("left")
        if cmd == "x":
            changeDir("right")

def changeDir(newDir):
    global dir
    if newDir == "left":
        if dir == "north":
            dir = "west"
        elif dir == "east":
            dir = "north"
        elif dir == "south":
            dir = "east"
        elif dir == "west":
            dir == "south"
    else:
        if dir == "north":
            dir = "east"
        elif dir == "east":
            dir = "south"
        elif dir == "south":
            dir = "west"
        elif dir == "west":
            dir == "north"

def moveBlock():
    global speed, objX, objY, objZ, dir

    while 1 != 0:
        if speed > 0:
            mc.setBlock(objX, objY, objZ, 0)
            if dir == "north":
                objZ += speed
            elif dir == "east":
                objX -= speed
            elif dir == "south":
                objZ -= speed
            elif dir == "west":
                objX += speed
            else:
                continue
            mc.setBlock(objX, objY, objZ, objBlock)
        time.sleep(1)

thread1 = Thread(target = main, args = ())
thread2 = Thread(target = moveBlock, args = ())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
