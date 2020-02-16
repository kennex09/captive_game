#kennex

import os, pygame, sys
from settings import Settings
import gf
import puzzles
from inventory import Inventory
from objects import GameObjects
from stable_items import Stable_Items
from control_panel import Control_Panel
from room import Room
from pygame.locals import *

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.mixer.pre_init(44100,-16,2, 2048)
    pygame.init()
    clock = pygame.time.Clock()
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height), HWSURFACE | DOUBLEBUF) # add ability to resize window
    pygame.display.set_caption("Escape the Room | Kennex")

    gf.generate_codes(gs) # generates numbers for problems and puzzles

    stable_item_blocks = Stable_Items(gs, screen)
    room_view = Room(gs, screen, stable_item_blocks)
    inventory = Inventory(gs, screen, room_view)
    game_objects = GameObjects(gs, screen, inventory)
    cp = Control_Panel(gs, screen)

    gs.text = "Where am I?"


    while True:
        gf.check_events(gs, screen, inventory, room_view, game_objects, stable_item_blocks, cp)
        gf.update_screen(gs, screen, inventory, room_view, game_objects, stable_item_blocks, cp)
        gf.game_clock(gs, screen, clock)
        
        if gs.sleeperticks:
            pygame.time.wait(100)  # Leave this at 100 or less
            

run_game()


"""
TO DO LIST

7. Need to create additional screens, where necessary (such as for the side of the tv stand).
8. Need to create a logo for Kennex for the beginning.
9. Need to figure out what is going to go at the bottom of the inventory window.
10. Need to figure out how to do mouseovers (for text).
11. Need to write all the text and figure out how it's going to work.
12. Text needs to be unique to each item, place, and thing.
13. 
14. Need to create an intro.
15. Need to create an outro.
16. Need to add sounds.
17. Need to figure out what is going on with the chair manual and the camera manual.
18. Need to add curtains and they should probably retract.
19. Need to figure out scaling in inventory.
20. Need to figure out if scaling the entire game is possible based on how it's drawn.
21. Need to figure out how items will interact.


"""
# todo make credits
# todo make what happens after you click open door / outro
# todo make intro
# todo create stats tracker (i.e. how many times played, hours played, times escaped, etc.)
# todo add text
# todo add music
# todo figure out what other channels are needed
# todo figure out if you can scale the whole game
# todo add sound control to the remote
# todo are there ways to quickly optimize?
# todo figure out a title
# todo create a title logo
# todo create kennex logo
# todo fix everything that the tv is saying for the text below. everything is currently there no matter what else is clicked in both views




