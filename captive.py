#kennex

import pygame, sys#, datetime, os
from settings import Settings
import gf
from inventory import Inventory
from objects import GameObjects
from stable_items import Stable_Items
from control_panel import Control_Panel
from room import Room
from pygame.locals import *
from pygame import FULLSCREEN
from pygame.rect import Rect
from steamworks import STEAMWORKS
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


"""
UNCOMMENT THIS FOR STEAM ACHIEVEMENTS AND STEAMWORKS ABILITIES
"""

# Declare the steamworks variable and create a new instance of the Steamworks class
steamworks = STEAMWORKS()

# Initialize Steam
steamworks.initialize()


# Initialize pygame, settings, and screen object.
pygame.mixer.pre_init(44100,-16,2, 2048)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
gs = Settings()

#screen = pygame.display.set_mode((gs.screen_width, gs.screen_height), HWSURFACE | DOUBLEBUF)
pygame.display.set_mode((gs.screen_width, gs.screen_height), OPENGL | DOUBLEBUF | HWSURFACE) # Code to add OpenGL
pygame.display.init()
info = pygame.display.Info()


screen = pygame.Surface((info.current_w, info.current_h))  # Make 'Off-Screen' Pygame Surface
screen_rect = screen.get_rect()

pygame.display.set_caption("Captive | Kennex Software")
icon = pygame.image.load('images/key_icon.ico') # should be 32 x 32
game_logo = pygame.image.load('images/key_logo.png')
pygame.display.set_icon(icon)
stable_item_blocks = Stable_Items(gs, screen)
room_view = Room(gs, screen, stable_item_blocks)
inventory = Inventory(gs, screen, room_view)
game_objects = GameObjects(gs, screen, inventory)
cp = Control_Panel(gs, screen)

intro_music = pygame.mixer.Sound('sounds/intro.wav')
credits_music = pygame.mixer.Sound('sounds/credits.wav')

game_version = gs.verdana16.render(str(gs.game_version), True, gs.black)
game_version_rect = game_version.get_rect()

# Basic OpenGL Configuration
glViewport(0, 0, info.current_w, info.current_h)
glDepthRange(0, 1)
glMatrixMode(GL_PROJECTION)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glShadeModel(GL_SMOOTH)
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(5.0)
glDisable(GL_DEPTH_TEST)
glDisable(GL_LIGHTING)
glDepthFunc(GL_LEQUAL)
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
glEnable(GL_BLEND)

###
### Function to convert a PyGame Surface to an OpenGL Texture
### Maybe it's not necessary to perform each of these operations
### every time.
### todo review this for optimization
###

global texID
texID = glGenTextures(1)

# prepare to render the texture-mapped rectangle

glLoadIdentity()
glDisable(GL_LIGHTING)
glDisable(GL_TEXTURE_1D)
glDisable(GL_TEXTURE_3D)
glEnable(GL_TEXTURE_2D)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glBindTexture(GL_TEXTURE_2D, texID)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)



def open_gl_code_to_run(screen):
    glClearColor(0, 0, 0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(-1, 1)
    glTexCoord2f(0, 1); glVertex2f(-1, -1)
    glTexCoord2f(1, 1); glVertex2f(1, -1)
    glTexCoord2f(1, 0); glVertex2f(1, 1)
    glEnd()

    # draw texture openGL Texture
    rgb_surface = pygame.image.tostring(screen, 'RGB')

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, screen_rect.width, screen_rect.height, 0, GL_RGB, GL_UNSIGNED_BYTE, rgb_surface)
    glGenerateMipmap(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, 0)



def fullscreen_fix(game_height):
    """ Sets full screen display mode and draws a square in the top left """
    # Set the display mode to the current screen resolution
    screen = pygame.display.set_mode((0, 0), FULLSCREEN)

    # create a square pygame surface
    game_surface = pygame.Surface((game_height, game_height))
    game_surface.fill((255, 255, 255))

    # draw a square in the top left
    pygame.draw.rect(game_surface, (0, 0, 0), Rect(10, 10, 200, 200))

    # make the largest square surface that will fit on the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    smallest_side = min(screen_width, screen_height)
    screen_surface = pygame.Surface((smallest_side, smallest_side))

    # scale the game surface up to the larger surface
    pygame.transform.scale(
        game_surface,  # surface to be scaled
        (smallest_side, smallest_side),  # scale up to (width, height)
        screen_surface)  # surface that game_surface will be scaled onto

    # place the larger surface in the centre of the screen
    screen.blit(
        screen_surface,
        ((screen_width - smallest_side) // 2,  # x pos
        (screen_height - smallest_side) // 2))  # y pos

    pygame.display.flip()
    wait_for_keypress()

def total_time():


    while True:

        screen.fill((gs.white))
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    game_menu()

        display_text = ['YOUR ESCAPE TIME:',
                        '',
                        str(gs.end_time),
                        '',
                        '',
                        'CLICK TO CONTINUE']

        line_spacing = 200
        text_height = gs.arial60.get_height()

        for item in display_text:
            text_image = gs.arial60.render(item, True, gs.black)
            text_image_rect = text_image.get_rect()
            text_image_rect.centerx = gs.screen_width // 2
            screen.blit(text_image, (text_image_rect[0], 0+line_spacing))
            line_spacing += text_height

        open_gl_code_to_run(screen)

        # Update
        pygame.display.flip()
        clock.tick(60)

def credits():
    title = gs.arial60.render('to be continued...', True, gs.black)
    alpha_title_surface = pygame.Surface(title.get_size(), pygame.SRCALPHA)
    alpha_t = 0
    start_ticks = pygame.time.get_ticks()
    max_alpha_reached = False
    run_tbc = True
    run_credits = True
    credits_full ="""
Coding, Artwork, and Writing By:
Kennex

Music By:
Gnarski


Thank you to the Play Testers:
Ami <3
Gnarski
BigHeadBrett
Rappican
Mr. Green
Josh


A Special Thanks To:
Takagism for making the Crimson Room
No Starch Press for teaching me to code
Tech With Tim for inspiring me to code
Gramps for SteakworksPy
Kingsley for OpenGL Support
Happy Chuck Programming for help with Scrolling Text
Ted Klein Bergman for help with the TV Static
The Stackoverflow Community
The Python Community
The Python Subreddits


And a Big Thanks to YOU!
Thank You For Playing.

I hope you enjoyed the game as much as I
enjoyed making it and learning how to code.







CAPTIVE
    """
    scrolling_centerx, scrolling_centery = screen.get_rect().centerx, screen.get_rect().centery
    delta = scrolling_centery


    while gs.won_game:

        pygame.mixer.Sound.play(credits_music, 0)
        screen.fill((gs.white))
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not run_tbc:
                        run_credits = False
                        pygame.time.wait(1000)
                        pygame.mixer.Sound.stop(credits_music)
                        total_time()
                        #game_menu()
                    if run_tbc:
                        run_tbc = False
                        run_credits = True




        seconds = (pygame.time.get_ticks() - start_ticks)/1000

        if seconds > 2 and run_tbc:
            if not max_alpha_reached:
                if alpha_t >= 0 and alpha_t <= 254:
                    alpha_t = max(alpha_t+2, 0)
                    title_surface = title.copy()
                    alpha_title_surface.fill((0, 0, 0, alpha_t))
                    title_surface.blit(alpha_title_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                    if alpha_t >= 254:
                        alpha_t = 255
                        max_alpha_reached = True

            if max_alpha_reached:
                alpha_t = max(alpha_t-2, 0)
                title_surface = title.copy()
                alpha_title_surface.fill((0, 0, 0, alpha_t))
                title_surface.blit(alpha_title_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                if alpha_t <= 1:
                    alpha_t = 0


            screen.blit(title_surface, (gs.screen_width//2, gs.screen_height//2))

        if seconds > 12 and run_tbc:
            run_tbc = False

        if not run_tbc and run_credits:
            delta -= 1
            gf.scrolling_credits(gs, screen, credits_full, scrolling_centerx, scrolling_centery, delta)


        else:
            pass


        open_gl_code_to_run(screen)


        # Update
        pygame.display.flip()
        clock.tick(60)

def title_menu():

    title = gs.cambria90.render('CAPTIVE', True, gs.black)
    author = gs.verdana32.render('Kennex Presents:', True, gs.black)
    alpha_title_surface = pygame.Surface(title.get_size(), pygame.SRCALPHA)
    alpha_author_surface = pygame.Surface(author.get_size(), pygame.SRCALPHA)
    alpha_a = 0
    alpha_t = 0
    start_ticks = pygame.time.get_ticks()

    while True:
        # Events
        pygame.mixer.Sound.play(intro_music, -1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    game_menu()

        # Draw Menu

        screen.fill((gs.white))
        seconds = (pygame.time.get_ticks() - start_ticks)/1000

        if seconds > 2:
            if alpha_a >= 0 and alpha_a <= 254:
                alpha_a = max(alpha_a+2, 0)
                author_surface = author.copy()
                alpha_author_surface.fill((0, 0, 0, alpha_a))
                author_surface.blit(alpha_author_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                if alpha_a >= 254:
                    alpha_a = 255

            screen.blit(author_surface, (350, 290))


        if seconds > 7:

            if alpha_t >= 0 and alpha_t <= 254:
                alpha_t = max(alpha_t+2, 0)
                title_surface = title.copy()
                alpha_title_surface.fill((0, 0, 0, alpha_t))
                title_surface.blit(alpha_title_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                if alpha_t >= 254:
                    alpha_t = 255


            screen.blit(title_surface, (gs.screen_width//2, gs.screen_height//2))



        if seconds > 16:
            game_menu()

        open_gl_code_to_run(screen)

        # Update
        pygame.display.flip()
        clock.tick(60)

def game_menu():
    game_title = gs.cambria150.render('CAPTIVE', True, gs.black)
    game_title_rect = game_title.get_rect()
    game_title_rect.centerx = gs.screen_width//2
    game_logo_rect = game_logo.get_rect()
    game_logo_rect.centerx = gs.screen_width//2

    button_color1 = gs.gray
    button_color2 = gs.gray
    button_color3 = gs.gray
    button_color4 = gs.gray
    button_color5 = gs.gray

    button1 = pygame.Rect(0, 600, 190, 80)
    button1.centerx = gs.screen_width//2
    button2 = button1.move(-button1.width - 30, 0)
    button3 = button2.move(-button2.width - 30, 0)
    button4 = button1.move(button1.width + 30, 0)
    button5 = button4.move(button4.width + 30, 0)

    gs.new_game = True

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button1.collidepoint(event.pos):
                        print('scores')
                    if button2.collidepoint(event.pos):
                        print('load game')
                        gf.load_settings(gs)
                        pygame.time.wait(500)
                        gs.options_menu_up = False
                        pygame.mixer.Sound.stop(intro_music)
                        gs.game_started = True
                        run_game()
                    if button3.collidepoint(event.pos):
                        print('run game')
                        pygame.time.wait(2000)
                        pygame.mixer.Sound.stop(intro_music)
                        gs.game_started = True
                        run_game()
                    if button4.collidepoint(event.pos):
                        print('settings')
                        settings_menu()
                    if button5.collidepoint(event.pos):
                        sys.exit()



        screen.fill((gs.bg_color))

        screen.blit(game_version, (0,0))

        screen.blit(game_logo, (game_logo_rect.x, game_title_rect.bottom + 175))
        screen.blit(game_title, (game_title_rect.x, 175))

        pygame.draw.rect(screen, button_color1, button1)
        pygame.draw.rect(screen, button_color2, button2)
        pygame.draw.rect(screen, button_color3, button3)
        pygame.draw.rect(screen, button_color4, button4)
        pygame.draw.rect(screen, button_color5, button5)

        pygame.draw.rect(screen, gs.black, button1, 3)
        pygame.draw.rect(screen, gs.black, button2, 3)
        pygame.draw.rect(screen, gs.black, button3, 3)
        pygame.draw.rect(screen, gs.black, button4, 3)
        pygame.draw.rect(screen, gs.black, button5, 3)

        b1_text = gs.arial32.render('PLAY', True, gs.black)
        b2_text = gs.arial32.render('LOAD', True, gs.black)
        b3_text = gs.arial32.render('SCORES', True, gs.black)
        b4_text = gs.arial32.render('SETTINGS', True, gs.black)
        b5_text = gs.arial32.render('QUIT', True, gs.black)

        b1_text_rect = b1_text.get_rect(center = button3.center)
        b2_text_rect = b2_text.get_rect(center = button2.center)
        b3_text_rect = b3_text.get_rect(center = button1.center)
        b4_text_rect = b4_text.get_rect(center = button4.center)
        b5_text_rect = b5_text.get_rect(center = button5.center)

        screen.blit(b1_text, b1_text_rect)
        screen.blit(b2_text, b2_text_rect)
        screen.blit(b3_text, b3_text_rect)
        screen.blit(b4_text, b4_text_rect)
        screen.blit(b5_text, b5_text_rect)

        if button1.collidepoint(pygame.mouse.get_pos()):
            button_color1 = gs.dark_gray
            button_color2 = gs.gray
            button_color3 = gs.gray
            button_color4 = gs.gray
            button_color5 = gs.gray
        elif button2.collidepoint(pygame.mouse.get_pos()):
            button_color2 = gs.dark_gray
            button_color1 = gs.gray
            button_color3 = gs.gray
            button_color4 = gs.gray
            button_color5 = gs.gray
        elif button3.collidepoint(pygame.mouse.get_pos()):
            button_color3 = gs.dark_gray
            button_color2 = gs.gray
            button_color1 = gs.gray
            button_color4 = gs.gray
            button_color5 = gs.gray
        elif button4.collidepoint(pygame.mouse.get_pos()):
            button_color4 = gs.dark_gray
            button_color2 = gs.gray
            button_color3 = gs.gray
            button_color1 = gs.gray
            button_color5 = gs.gray
        elif button5.collidepoint(pygame.mouse.get_pos()):
            button_color5 = gs.dark_gray
            button_color2 = gs.gray
            button_color3 = gs.gray
            button_color4 = gs.gray
            button_color1 = gs.gray
        else:
            button_color1 = gs.gray
            button_color2 = gs.gray
            button_color3 = gs.gray
            button_color4 = gs.gray
            button_color5 = gs.gray


        open_gl_code_to_run(screen)




        # Update
        pygame.display.flip()
        clock.tick(60)

def options_menu():
    gs.options_menu_up = True
    game_title = gs.cambria90.render('OPTIONS', True, gs.black)

    game_title_rect = game_title.get_rect()
    game_title_rect.centerx = gs.screen_width//2

    quit_menu = pygame.Rect(400, 325, 600, 200)
    quit_menu.centerx = gs.screen_width//2

    button_color1 = gs.gray
    button_color2 = gs.gray
    button_color3 = gs.gray
    button_color4 = gs.gray
    button_color5 = gs.gray
    q_button_save_color = gs.gray
    q_button_quit_color = gs.gray

    button1 = pygame.Rect(0, 600, 190, 80)
    button1.centerx = gs.screen_width//2
    button2 = button1.move(-button1.width - 30, 0)
    button3 = button2.move(-button2.width - 30, 0)
    button4 = button1.move(button1.width + 30, 0)
    button5 = button4.move(button4.width + 30, 0)

    b1_text = gs.arial32.render('BACK', True, gs.black)
    b2_text = gs.arial32.render('SAVE', True, gs.black)
    b3_text = gs.arial32.render('LOAD', True, gs.black)
    b4_text = gs.arial32.render('SETTINGS', True, gs.black)
    b5_text = gs.arial32.render('QUIT', True, gs.black)

    b1_text_rect = b1_text.get_rect(center = button3.center)
    b2_text_rect = b2_text.get_rect(center = button2.center)
    b3_text_rect = b3_text.get_rect(center = button1.center)
    b4_text_rect = b4_text.get_rect(center = button4.center)
    b5_text_rect = b5_text.get_rect(center = button5.center)

    q_button_save = pygame.Rect(0, 410, 190, 80)
    q_button_save.centerx = quit_menu.centerx - ((q_button_save.width // 2) + 15)
    q_button_quit = q_button_save.move(q_button_save.width + 30, 0)
    ask_to_save_text = gs.verdana18.render('Are you sure you want to quit without saving?', True, gs.black)
    ask_to_save_text_rect = ask_to_save_text.get_rect(center = (quit_menu.centerx, quit_menu.y + 40))
    q_save_text_rect = b2_text.get_rect(center = q_button_save.center)
    q_quit_text_rect = b5_text.get_rect(center = q_button_quit.center)


    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gs.options_menu_up = False
                    gs.resume_time = pygame.time.get_ticks()
                    gs.stoppage_time = gs.stoppage_time + (gs.resume_time - gs.pause_time)
                    gs.game_started = True
                    run_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not gs.quit_menu_up:
                    if button1.collidepoint(event.pos):
                        print('load game')
                        gf.load_settings(gs)
                        pygame.time.wait(500)
                        gs.options_menu_up = False
                        gs.resume_time = pygame.time.get_ticks()
                        gs.stoppage_time = gs.stoppage_time + (gs.resume_time - gs.pause_time)
                        if gs.start_game_from_load:
                            gs.game_started = True
                            run_game()
                    if button2.collidepoint(event.pos):
                        print('save game')
                        gs.resume_time = pygame.time.get_ticks()
                        gs.stoppage_time = gs.stoppage_time + (gs.resume_time - gs.pause_time)
                        gf.save_settings(gs)
                        pygame.time.wait(500)
                        gs.options_menu_up = False
                        gs.game_started = True
                        run_game()
                    if button3.collidepoint(event.pos):
                        print('run game')
                        gs.options_menu_up = False
                        gs.resume_time = pygame.time.get_ticks()
                        gs.stoppage_time = gs.stoppage_time + (gs.resume_time - gs.pause_time)
                        gs.game_started = True
                        run_game()
                    if button4.collidepoint(event.pos):
                        settings_menu()
                        print('settings')
                    if button5.collidepoint(event.pos):
                        gs.quit_menu_up = True
                        print('show quit menu')
                if event.button == 1 and gs.quit_menu_up:
                    print('quit menu up')
                    if q_button_save.collidepoint(event.pos):
                        print('save game')
                        gs.resume_time = pygame.time.get_ticks()
                        gs.stoppage_time = gs.stoppage_time + (gs.resume_time - gs.pause_time)
                        gf.save_settings(gs)
                        pygame.time.wait(500)
                        gs.options_menu_up = False
                        gs.quit_menu_up = False
                        gs.game_started = True
                        run_game()
                    if q_button_quit.collidepoint(event.pos):
                        gs.options_menu_up = False
                        gs.quit_menu_up = False
                        game_menu()


        screen.fill((gs.bg_color))
        screen.blit(game_title, (game_title_rect.x, 200))

        screen.blit(game_version, (0,0))

        pygame.draw.rect(screen, button_color1, button1)
        pygame.draw.rect(screen, button_color2, button2)
        pygame.draw.rect(screen, button_color3, button3)
        pygame.draw.rect(screen, button_color4, button4)
        pygame.draw.rect(screen, button_color5, button5)

        pygame.draw.rect(screen, gs.black, button1, 3)
        pygame.draw.rect(screen, gs.black, button2, 3)
        pygame.draw.rect(screen, gs.black, button3, 3)
        pygame.draw.rect(screen, gs.black, button4, 3)
        pygame.draw.rect(screen, gs.black, button5, 3)

        screen.blit(b1_text, b1_text_rect)
        screen.blit(b2_text, b2_text_rect)
        screen.blit(b3_text, b3_text_rect)
        screen.blit(b4_text, b4_text_rect)
        screen.blit(b5_text, b5_text_rect)

        if not gs.quit_menu_up:
            if button1.collidepoint(pygame.mouse.get_pos()):
                button_color1 = gs.dark_gray
                button_color2 = gs.gray
                button_color3 = gs.gray
                button_color4 = gs.gray
                button_color5 = gs.gray
            elif button2.collidepoint(pygame.mouse.get_pos()):
                button_color2 = gs.dark_gray
                button_color1 = gs.gray
                button_color3 = gs.gray
                button_color4 = gs.gray
                button_color5 = gs.gray
            elif button3.collidepoint(pygame.mouse.get_pos()):
                button_color3 = gs.dark_gray
                button_color2 = gs.gray
                button_color1 = gs.gray
                button_color4 = gs.gray
                button_color5 = gs.gray
            elif button4.collidepoint(pygame.mouse.get_pos()):
                button_color4 = gs.dark_gray
                button_color2 = gs.gray
                button_color3 = gs.gray
                button_color1 = gs.gray
                button_color5 = gs.gray
            elif button5.collidepoint(pygame.mouse.get_pos()):
                button_color5 = gs.dark_gray
                button_color2 = gs.gray
                button_color3 = gs.gray
                button_color4 = gs.gray
                button_color1 = gs.gray
            else:
                button_color1 = gs.gray
                button_color2 = gs.gray
                button_color3 = gs.gray
                button_color4 = gs.gray
                button_color5 = gs.gray

        if gs.quit_menu_up:
            window_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            window_surface.fill(gs.white_alpha)
            screen.blit(window_surface, (0,0))

            pygame.draw.rect(screen, gs.bg_color, quit_menu)
            pygame.draw.rect(screen, gs.black, quit_menu, 4)
            screen.blit(ask_to_save_text, ask_to_save_text_rect)

            pygame.draw.rect(screen, q_button_save_color, q_button_save)
            pygame.draw.rect(screen, q_button_quit_color, q_button_quit)

            pygame.draw.rect(screen, gs.black, q_button_save, 3)
            pygame.draw.rect(screen, gs.black, q_button_quit, 3)

            screen.blit(b2_text, q_save_text_rect)
            screen.blit(b5_text, q_quit_text_rect)

            if q_button_save.collidepoint(pygame.mouse.get_pos()):
                q_button_save_color = gs.dark_gray
                q_button_quit_color = gs.gray
            elif q_button_quit.collidepoint(pygame.mouse.get_pos()):
                q_button_quit_color = gs.dark_gray
                q_button_save_color = gs.gray
            else:
                q_button_save_color = gs.gray
                q_button_quit_color = gs.gray

        open_gl_code_to_run(screen)

        # Update
        pygame.display.flip()
        clock.tick(60)

def settings_menu():
    gs.settings_menu_up = True
    game_title = gs.cambria90.render('SETTINGS', True, gs.black)

    game_title_rect = game_title.get_rect()
    game_title_rect.centerx = gs.screen_width//2

    button_color1 = gs.gray # Save
    button_color2 = gs.gray # Cancel

    button1 = pygame.Rect(0, 600, 190, 80)
    button1.centerx = gs.screen_width//2 - button1.width//2 - 15
    button2 = button1.move(button1.width + 30, 0)

    b1_text = gs.arial32.render('SAVE', True, gs.black)
    b2_text = gs.arial32.render('CANCEL', True, gs.black)

    b1_text_rect = b1_text.get_rect(center = button1.center)
    b2_text_rect = b2_text.get_rect(center = button2.center)

    setting1_text = gs.cambria30.render('FULLSCREEN', True, gs.black)
    #setting2_text = gs.cambria30.render('SETTING 2', True, gs.black)
    #setting3_text = gs.cambria30.render('SETTING 3', True, gs.black)

    #setting1_text_rect = setting1_text.get_rect()
    #setting2_text_rect = setting2_text.get_rect()
    #setting3_text_rect = setting3_text.get_rect()

    settings1_checkbox = pygame.Rect(490, 376, setting1_text.get_height() - 10, setting1_text.get_height() - 10)

    settings_checkmark = gs.cambria24.render('X', True, gs.black)
    settings_checkmark_rect = settings_checkmark.get_rect(center=settings1_checkbox.center)


    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if gs.options_menu_up:
                        options_menu()
                    else:
                        game_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)
                    if settings1_checkbox.collidepoint(event.pos):
                        gs.fullscreen_checked = not gs.fullscreen_checked
                    if button1.collidepoint(event.pos):
                        print('save settings')
                        if screen.get_flags() & FULLSCREEN and not gs.fullscreen_checked:
                            pygame.display.set_mode((gs.screen_width, gs.screen_height), HWSURFACE | DOUBLEBUF | OPENGL)
                        elif gs.fullscreen_checked:
                            pygame.display.set_mode((gs.screen_width, gs.screen_height), FULLSCREEN | HWSURFACE | DOUBLEBUF | OPENGL)


                    if button2.collidepoint(event.pos):
                        print('cancel settings')
                        if gs.options_menu_up:
                            options_menu()
                            gs.settings_menu_up = False
                        else:
                            game_menu()
                            gs.settings_menu_up = False


        screen.fill((gs.bg_color))
        screen.blit(game_version, (0,0))
        screen.blit(game_title, (game_title_rect.x, 200))

        pygame.draw.rect(screen, gs.white, settings1_checkbox)
        pygame.draw.rect(screen, gs.black, settings1_checkbox, 2)




        screen.blit(setting1_text, (530, 370))
        #screen.blit(setting2_text, (490, 410))
        #screen.blit(setting3_text, (490, 450))











        pygame.draw.rect(screen, button_color1, button1)
        pygame.draw.rect(screen, button_color2, button2)

        pygame.draw.rect(screen, gs.black, button1, 3)
        pygame.draw.rect(screen, gs.black, button2, 3)

        screen.blit(b1_text, b1_text_rect)
        screen.blit(b2_text, b2_text_rect)

        if gs.fullscreen_checked:
            screen.blit(settings_checkmark, settings_checkmark_rect)

        if button1.collidepoint(pygame.mouse.get_pos()):
            button_color1 = gs.dark_gray
            button_color2 = gs.gray
        elif button2.collidepoint(pygame.mouse.get_pos()):
            button_color2 = gs.dark_gray
            button_color1 = gs.gray
        else:
            button_color1 = gs.gray
            button_color2 = gs.gray

        open_gl_code_to_run(screen)

        # Update
        pygame.display.flip()
        clock.tick(60)

def run_game():

    allow_new_game = True
    if gs.new_game and allow_new_game:
        gf.default_settings(gs)
        gf.generate_codes(gs) # generates numbers for problems and puzzles
        gf.update_settings_dictionary(gs) # Generates the ability to save the settings generated in the generate codes
        gs.text = "What the...?  Where am I?"
        gs.game_start_time = pygame.time.get_ticks()
        gs.new_game = False
        print('starting completely new game')
    else:
        gs.game_start_time = pygame.time.get_ticks()
        gs.new_game = False

    while gs.game_started:
        gf.check_events(gs, screen, inventory, room_view, game_objects, stable_item_blocks, cp, steamworks)
        open_gl_code_to_run(screen)
        gf.update_screen(gs, screen, inventory, room_view, stable_item_blocks, cp, clock, game_objects)


        #if gs.sleeperticks:
        #    pygame.time.wait(100)  # Leave this at 100 or less

        gf.clock_timer(gs)

    while gs.options_menu_up:
        gf.clock_timer(gs)
        options_menu()

    while gs.won_game:
        credits()




    pygame.time.wait(1000)
    pygame.mixer.Sound.stop(credits_music)
    total_time()

#gs.won_game = True # Needed to run only credits // todo delete me or comment out
#credits()

#gs.game_started = True # Need to run only game // todo delete me or comment out
#run_game()


#settings_menu()

#game_menu()

# Make sure this is not commented for the full game prior to batching
title_menu()

"""








"""



"""
Batch this:

pyinstaller --onefile -w captive.py control_panel.py credits.py gf.py inventory.py multiline_text.py objects.py puzzles.py room.py scale_points_list.py settings.py stable_items.py tv_channels.py whitespace.py


----ability to ask for a desktop icon:

Function finishpageaction
CreateShortcut "$desktop\foo.lnk" "$instdir\foo.exe"
FunctionEnd

!define MUI_FINISHPAGE_SHOWREADME ""
!define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED
!define MUI_FINISHPAGE_SHOWREADME_TEXT "Create Desktop Shortcut"
!define MUI_FINISHPAGE_SHOWREADME_FUNCTION finishpageaction

https://stackoverflow.com/questions/1517471/how-to-add-a-desktop-shortcut-option-on-finish-page-in-nsis-installer

-ability to choose a place on the C: Drive as a default installation path
-ability to uninstall / show in add/remove programs
-run game after install
-.exe needs to be custom ico
-uninstall old before installing new








"""

