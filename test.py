import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'. Replace with your own IP/name!
mc = minecraft.Minecraft.create(address="192.168.1.12", name="littlewizard0717")

 
active_spell = "teleport"
 
while True:
 
    for blockhit in mc.player.pollProjectileHits():
        if active_spell == "teleport":
            mc.player.setPos(blockhit.pos.x, blockhit.pos.y, blockhit.pos.z)
        elif active_spell == "lavapool":
            lava_block_id = 10
            mc.setBlocks(blockhit.pos.x+4, blockhit.pos.y-1, blockhit.pos.z+4,
                         blockhit.pos.x-4, blockhit.pos.y-1, blockhit.pos.z-4,
                         lava_block_id)
 
    for chatpost in mc.player.pollChatPosts():
        if chatpost.message.lower() == "lavapool":
            active_spell = "lavapool"
        elif chatpost.message.lower() == "teleport":
            active_spell = "teleport"
 
    time.sleep(.1)