from pythonosc.udp_client import SimpleUDPClient
from pynput import keyboard
import time 

ip = "127.0.0.1"
port = 9000

client = SimpleUDPClient(ip, port)  # Create client

right = True
left = True

movingAmount = 50 # Change for moving duration

moving = 0

steps = 0

# Main movement code

def on_press(key):

    # What am I doing...
    global steps, left, right, moving

    # If left step taken and right step was taken before
    if key == keyboard.Key.f13 and left == True:
        global steps
        steps += 1
        moving = movingAmount
        left = False
        client.send_message("/input/MoveForward", 1)   # Move forward
        right = True
        print(steps)
    # If right step taken and left step was taken before
    if key == keyboard.Key.f14 and right == True:
        steps += 1
        moving = movingAmount
        left = True
        client.send_message("/input/MoveForward", 1)   # Move forward
        right = False
        print(steps)

# I think this is right... it's working so far...

listener = keyboard.Listener(
    on_press=on_press,
)

#Start listening for keyboard inputs... I think... This is why you don't copy code kids
listener.start()


# Loop for moving grace period, essentially a timer before actually stopping movement
while True:
    if moving > 0:
        moving -= 1

        if moving == 0:
            client.send_message("/input/MoveForward", 0)
            print("Stopped moving")

    time.sleep(0.01)