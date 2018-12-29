import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'. Replace with your own IP/name!
mc = minecraft.Minecraft.create(address="192.168.1.12", name="littlewizard0717")

mc.postToChat('hi vati')

#get my position
pos = mc.player.getPos()
my_block= 9

y_height = 5
x_width = 10
z_length = 6
player_x_offset = 3

for x in range(player_x_offset,z_length):
    for y in range(0,y_height):
        mc.setBlock(pos.x + x, pos.y + y, pos.z, my_block)

for x in range(player_x_offset,z_length):
    for y in range(0,y_height):
        mc.setBlock(pos.x + x, pos.y + y, pos.z + x_width, my_block)

for z in range(0,x_width):
    for y in range(0,y_height):
        mc.setBlock(pos.x + player_x_offset, pos.y + y, pos.z + z, my_block)
        
for z in range(0,x_width + 1):
    for y in range(0,y_height):
        mc.setBlock(pos.x + z_length, pos.y + y, pos.z + z, my_block)
        