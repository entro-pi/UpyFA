#!/bin/env python3

import pygame
from subprocess import call
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [250, 250]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lockinator")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
            
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        name = joystick.get_name()
        # Should get the name and match it with the address here
        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            if i == 5 and button == 1:
                call(["loginctl", "unlock-session"])
            if i == 7 and button == 1:
                call(["loginctl", "lock-session"])
    
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
