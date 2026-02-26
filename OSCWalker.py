from pythonosc.udp_client import SimpleUDPClient
import time 
import pygame
pygame.init()
screen = pygame.display.set_mode((200,200))
running = True
clock = pygame.time.Clock()

ip = "127.0.0.1"
port = 9000

client = SimpleUDPClient(ip, port)  # Create client

right = True
left = True

movingAmount = 40 # Change for moving duration

moving = 0

steps = 0



# Movement
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys=pygame.key.get_pressed()
    screen.fill("orange")

    #Code for alternating steps

    if keys[pygame.K_F13] and left == True:
        steps += 1
        moving = movingAmount
        left = False
        client.send_message("/input/MoveForward", 1)   # Move forward
        right = True
        print(steps)

    if keys[pygame.K_F14] and right == True:
        steps += 1
        moving = movingAmount
        right = False
        client.send_message("/input/MoveForward", 1)   # Move forward
        left = True
        print(steps)

    #Constant move forward code with grace period to allow non-stop steps.

    if moving == 0:
        client.send_message("/input/MoveForward", 0)
    else:
        moving -= 1

    pygame.display.flip()

    clock.tick(100)