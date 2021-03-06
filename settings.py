#kennex

import pygame

pygame.font.init()

class Settings():
    """A class to store settings for Escape the Room.
    
    gs stands for "Game Settings" and will be used throughout
    
    """
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Game Version
        self.game_version = 'v 0.8.8.7'
        self.start_game_from_load = False
        """
        People that want the game:
        Reddit Users:
        ReallyRussell
        Shuffledrive
        
        
        Use this area to discuss version: 
        -5/24/2020 - Version 0.8.8.7 ---
            -Puzzle B (grid in blue book for box ii) was allowing non-three digit codes to pass due to leading zeros.  This was fixed and tested for all numbers.
            -Added numbers to the color grid in the blue book for clarity.
            -Changed the papers to read: "colors of diamonds" instead of "check out"
            -Added a better clue for the grid puzzle for the code.  Tested and working in both resolutions.
            -Added additional clues to the yellow book to hopefully make the game a little easier.
            
        -5/19/2020 - Version 0.8.8.6 ---
            -Fixed the bug that didn't save the colors on the blue book color line.
            -Added ability to see all codes in the game.
            -Fixed the clock saving bug maybe???
            
        -5/11/2020 - Version 0.8.8.5 ---
            -Fixed a bug on saving the game // Was missing 2 lines in the save method
            -Fixed the channel code not saving
            -Fixed the line sizes error on new game load
            
        -5/9/2020 -- Version 0.8.8.4 ---
            -Steam approved for release!
            -All stats are working (Times escaped, best time, worst time, least amount of clicks to escape)
            -All achievement images are in Steam, for the 17 achievements
            -Added the secret achievement channel
            -Added the WASD achievement
            -Added the Mo clicks Mo problems achievement
            -Added the interesting puzzle for the egg
            -Tested all achievements /// All Work
            
        -5/4/2020 -- Version 0.8.8.3 ---
            -Got all achievements working that are in Steam.  Need a few more achievements.
            -Got stats working and it works for the few achievements that require it.
            -Need to add more stats information   
            -Setting up the build for review with Steam         
            
        -4/28/2020 -- Version 0.8.8.2 ---
            -Added the ability to check the fonts in the system and if the font doesn't exist to use the default font.
            -Fixed some of the bugs.
            -Fixed a lot of areas for optimization that needed to be done.
            
        -4/27/2020 -- Version 0.8.8.2 ---
            -Fixed resolution issues
            
        -4/26/2020 -- Version 0.8.8.1 ---
            -Got Steam Achievements Working.  Need to make a full list and get them more working in the game.
            -Need to figure out Stats also
            
        -4/25/2020 -- Verizon 0.8.8 ---
            -Got OpenGL corrected and no longer lagging.  Uses much less resources and things seem to work fairly well.
                        
        -4/24/2020 -- Version 0.8.7 ---
            -Got Steam overlay working with OpenGL
            -Need to make OpenGL faster
            -Optimized some of the game objects and cleared out a lot of the game objects file
            -Remove pygame.init() from every file except for captive.py
            
        -4/22/2020 -- Version 0.8.6 ---
            -Added a lot of different functionality
            -Added a handful of Steam Achievements
            
        -4/18/2020 -- Version 0.8.2 ---
            -Added ability to connect game to Steam and have Steam Achievements
            -Added the Easter Egg that can be added to the inventory in a secret location
            -Added various new changes and fixes
            -Changed the TV stand in room view 1 if it's opened to view properly
            
        -3/24/2020 -- Version 0.7.8 ---
            -Added time value to end of game to inform user of time escaped
        
        -3/22/2020 -- Version 0.7.7 ---
            -Fixed the blue book text by changing the fonts, hoping this will work better on more PC's.
            -Fixed the blue book hint, changing the colors to not make them confusing.
            -Fixed the ability to trigger the wall outlet from the closet.
            -Fixed the fact that the message on the TV would play over and over if you kept pressing play.
            -Fixed the fact that a new game wouldn't start after the game was beat and you pressed play again.
            -Added verison number to the main manu and options menu.
            -Altered the clues on the paper to better address the diamonds, number grid, and colors.
            -Changed up where items are scaled and transformed, keeping them directly off the blits.
            -Removed the "unlock all" and "show all items" settings.

        -3/21/2020 -- Version 0.7.6 ---
            -Started a verisoning log.
            -Added quit menu with ability to quit with or without saving.
            -Will automatically install game into C: drive.
            -Added credits and got them to roll up, like a movie.
            -Save and Load were updated for error handling, so this was fixed.
            -Updated the ability to leave and run the credits.            

        
        """

        # Static Game Settings

        # Save and Load Filename Settings
        self.save_filename = None
        self.options_menu_up = False
        self.settings_menu_up = False
        self.quit_menu_up = False
        self.setting1_checked = False # 1440x960
        self.setting2_checked = False # 1200x800
        self.setting3_checked = False # Fullscreen
        self.achievement_list = []
        #self.achievement_list = [b'ACH_BUTTONS', b'ACH_COLLECT', b'ACH_CREDITS', b'ACH_DR', b'ACH_EGG', b'ACH_EXIT_FIVE', b'ACH_EXIT_ONE', b'ACH_EXIT_ONEHOUR', b'ACH_EXIT_TEN', b'ACH_EXIT_TWOHOUR', b'ACH_F', b'ACH_GOLD', b'ACH_PT', b'ACH_STAY', b'ACH_WINDOW']


        # Screen Settings
        self.screen_width = 1440 # 1440 // 1200
        self.screen_height = 960 # 960  // 800
        self.screen_rect_all = None





        # Alphabet List
        self.alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.wasd_list = []

        # WhiteSpace
        self.whitespace_count = 0

        # Show Cheats
        self.show_cheats = False
        self.show_cheats_channel = '999F999F999F'

        # Game window Settings
        self.gw_width = self.screen_width * .88  # Default is .88
        self.gw_height = self.screen_height * .90  # Default is .90
        self.gw_border = 5

        # Check Fonts
        #print(pygame.font.get_fonts())
        if 'verdana' not in pygame.font.get_fonts():
            self.verdana_name = pygame.font.get_default_font()
            print('Verdana not found')
        else:
            self.verdana_name = 'Verdana'

        if 'timesnewroman' not in pygame.font.get_fonts():
            self.times_new_roman_name = pygame.font.get_default_font()
            print('Times New Roman not found')
        else:
            self.times_new_roman_name = 'Times New Roman'

        if 'arial' not in pygame.font.get_fonts():
            self.arial_name = pygame.font.get_default_font()
            print('Arial not found')
        else:
            self.arial_name = 'Arial'

        if 'cambria' not in pygame.font.get_fonts():
            self.cambria_name = pygame.font.get_default_font()
            print('Cambria not found')
        else:
            self.cambria_name = 'Cambria'

        """self.verdana_name = 'Verdana'
        self.times_new_roman_name = 'Times New Roman'
        self.arial_name = 'Arial'
        self.cambria_name = 'Cambria'"""

        # Fonts
        self.verdana8 = pygame.font.SysFont(self.verdana_name, 8, True)
        self.verdana12 = pygame.font.SysFont(self.verdana_name, 12, True)
        self.verdana16 = pygame.font.SysFont(self.verdana_name, 16, True)
        self.verdana18 = pygame.font.SysFont(self.verdana_name, 18, True)
        self.verdana20 = pygame.font.SysFont(self.verdana_name, 20, True)
        self.verdana22 = pygame.font.SysFont(self.verdana_name, 22, True)
        self.verdana24 = pygame.font.SysFont(self.verdana_name, 24, True)
        self.verdana28 = pygame.font.SysFont(self.verdana_name, 28, True)
        self.verdana32 = pygame.font.SysFont(self.verdana_name, 32, True)
        self.verdana40 = pygame.font.SysFont(self.verdana_name, 40, True)
        self.verdana55 = pygame.font.SysFont(self.verdana_name, 55, True)

        self.times12 = pygame.font.SysFont(self.times_new_roman_name, 12, True)
        self.times14 = pygame.font.SysFont(self.times_new_roman_name, 14, True)
        self.times20 = pygame.font.SysFont(self.times_new_roman_name, 20, True)

        self.arial12 = pygame.font.SysFont(self.arial_name, 12, True)
        self.arial14 = pygame.font.SysFont(self.arial_name, 14, True)
        self.arial16 = pygame.font.SysFont(self.arial_name, 16, True)
        self.arial22 = pygame.font.SysFont(self.arial_name, 22, True)
        self.arial32 = pygame.font.SysFont(self.arial_name, 32, True)
        self.arial48 = pygame.font.SysFont(self.arial_name, 48, True)
        self.arial60 = pygame.font.SysFont(self.arial_name, 60, True)
        self.arial88 = pygame.font.SysFont(self.arial_name, 88, True)

        self.cambria12 = pygame.font.SysFont(self.cambria_name, 12, True)
        self.cambria16 = pygame.font.SysFont(self.cambria_name, 16, True)
        self.cambria18 = pygame.font.SysFont(self.cambria_name, 18, True)
        self.cambria20 = pygame.font.SysFont(self.cambria_name, 20, True)
        self.cambria22 = pygame.font.SysFont(self.cambria_name, 22, True)
        self.cambria24 = pygame.font.SysFont(self.cambria_name, 24, True)
        self.cambria30 = pygame.font.SysFont(self.cambria_name, 30, True)
        self.cambria48 = pygame.font.SysFont(self.cambria_name, 48, True)
        self.cambria90 = pygame.font.SysFont(self.cambria_name, 90, True)
        self.cambria150 = pygame.font.SysFont(self.cambria_name, 150, True)


        # Sleep Ticker
        #self.sleeperticks = True

        # Sidebar Settings
        self.sidebar_w = self.screen_width - self.gw_width
        self.sidebar_x = self.gw_width #- self.gw_border

        # Movement Settings in Game Window
        self.gw_move_w = self.gw_width * .03
        self.gw_right_x = self.sidebar_x - self.gw_move_w - self.gw_border

        # Clock / Save Area Settings
        #self.clock_box_h = ((self.screen_height - self.gw_height) * 2)
        #self.clock_box_y = self.screen_height - self.clock_box_h

        # Line Calculations
        # Room View 3 (TV Stand)
        self.r3_line_x2 = 1070 # Standard size for 1200 W // Will change if run at 1440 W
        self.r3_line_y2 = 750 # Standard size for 1200 W // Will change if run at 1440 W

        self.r3_1_line_x2 = 1093 # Standard size for 1200 W // Will change if run at 1440 W
        self.r3_1_line_y2 = 740 # Standard size for 1200 W // Will change if run at 1440 W

        self.r4_1_line_x2 = 1074 # Standard size for 1200 W // Will change if run at 1440 W
        self.r4_1_line_y2 = 741 # Standard size for 1200 W // Will change if run at 1440 W






        # Inventory Area Settings
        self.inventory_h = self.screen_height #- self.clock_box_h
        self.inv_item_w = self.sidebar_w / 2 * .8
        self.inv_item_h = self.sidebar_w / 2 * .8
        self.item_offset_w = self.gw_border * 2
        self.item_offset_h = self.gw_border * 2.5

        self.full_game_window_height = self.gw_height + (self.gw_border * 3)

        self.number_total_items = 15

        # Textbox Area Settings
        self.text_box_w = self.gw_width
        self.text_box_h = self.screen_height - self.gw_height - (self.gw_border * 3)
        self.text_box_x = 0
        self.text_box_y = self.gw_height + self.gw_border*3

        # Colors
        self.bg_color = (107, 126, 156)  # Walls
        self.white = (255, 255, 255)
        self.white_alpha = (255, 255, 255, 128)
        self.silver = (192, 192, 192)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.orange = (255, 165, 0)
        self.purple = (106, 13, 173)
        self.black = (0, 0, 0)
        self.yellow = (207, 181, 52)
        self.gray_transparent = (173, 168, 168, 75)
        self.yellowish = (207, 181, 62)
        self.bright_yellow = (255, 255, 0)
        self.brown = (102, 51, 0)
        self.gray = (173, 168, 168)
        self.dark_gray = (53, 53, 53)
        self.the_other_gray = (88, 88, 88)
        self.dark_blue = (80, 92, 111) # Interior Walls
        self.dark_brown = (56, 25, 11)
        self.good_green = (198, 239, 206)
        self.bad_red = (255, 199, 206)
        self.outer_floor = (118, 112, 100)
        self.carpet = (128, 128, 130)  # Carpet
        self.door = (81, 85, 88)  # Door / Fairly dark gray
        self.off_white = (226, 226, 224)
        self.file_cabinet = (193, 186, 168)
        self.interior_drawer = (149, 141, 116)
        self.wood = (100, 90, 89)
        self.dark_wood = (95, 90, 89)
        self.darker_wood = (69, 64, 63)
        self.tv_screen = (82, 82, 82)
        self.safe = (47, 54, 82)
        self.red_book_color = (120, 33, 33)  # Red One
        self.blue_book_color = (66, 72, 158)  # Blue one
        self.yellow_book_color = (245, 236, 61)  # Yellow one
        self.transcolor = (254, 254, 254, 0)
        self.clickboxcolor = (253, 253, 253)




        self.game_started = False
        self.game_ended = False
        self.clicked_credits = False

        # ----------------------------------------------------------------------------------------------------------
        # All Variable Settings that need to be saved and reset

        # Game
        self.new_game = True

        # Count Clicks
        self.game_clicks = 0

        # Text
        self.text = None
        self.current_text = None

        # Clock
        self.frame_rate = 60


        self.client_start_time = 0
        self.current_game_time = 0
        self.save_time = 0
        self.pause_time = 0
        self.resume_time = 0
        self.stoppage_time = 0
        self.end_time = 0
        self.load_time = 0



        # Win Game
        self.won_game = False # Default = False todo make false
        self.leave = False # Default = False

        # Inventory Items Found
        self.door_key_found = False # Default = False
        self.red_key_found = False # Default = False
        self.purple_key_found = False # Default = False
        self.green_key_found = False # Default = False
        self.remote_found = False # Default = False todo make false
        self.batteries_found = False # Default = False
        self.power_cord_found = False # Default = False
        self.papers_found = False # Default = False
        self.red_book_found = False # Default = False
        self.blue_book_found = False # Default = False
        self.yellow_book_found = False # Default = False
        self.desk_drawer_removed = False # Default = False
        self.shirt_found = False # Default = False
        self.screwdriver_found = False # Default = False
        self.egg_found = False # Default = False

        self.power_cord_desk_1 = False # Default = False
        self.power_cord_desk_2 = False # Default = False
        self.power_cord_window_1 = False # Default = False

        self.moveable_items_index_list = []
        self.number_all_items_found = 0

        self.door_key_used = False # Default = False
        self.red_key_used = False # Default = False
        self.purple_key_used = False # Default = False
        self.green_key_used = False # Default = False
        self.batteries_used = False # Default = False
        self.power_cord_used = False # Default = False
        self.screwdriver_used = False # Default = False
        self.egg_used = False # Default = False


        # Stable Items in Inventory Settings
        self.stable_item_opened = False  # Default = False

        # Shirt Settings
        self.shirt_opened = False

        # Remote Settings
        self.remote_opened = False  # Default = False
        self.close_remote = False  # Default = False
        self.batteries_input = False  # Default = False # todo change to false
        self.button_input_list = []
        self.entered_buttons = None
        self.muted = False
        self.volume = None

        # TV Settings
        self.tv_on = False  # Default = False todo make false
        self.current_channel = '3' # Default = '3' todo make '3'
        self.random_channel = None
        self.tv_sound_play_var = 0
        self.safe_on_sound_var = 0
        self.tv_stand_open_var = 0
        self.current_tv_screen_color = (82, 82, 82)
        self.message_channel_play = False
        self.tv_stand_open = False
        self.tv_stand_egg_found_text_var = True  # Default = True
        self.easter_egg_channel = '366F'

        # Safe Settings
        self.safe_uncovered = False # Default = false todo make false
        self.safe_on = False  # Default = False // Nothing on the safe can be done or used until the safe is turned on todo make false
        self.safe_initialized = False # Safe can only be opened if a certain channel is on the TV todo make false
        self.safe_use_color = self.black
        self.color_number_1 = self.black  # This number is needed to open the safe
        self.color_number_2 = self.black  # This number is needed to open the safe
        self.safe_combo_n1 = 0  # This number is needed to open the safe
        self.safe_combo_n2 = 0  # This number is needed to open the safe
        self.safe_combo_n3 = 0  # This number is needed to open the safe
        self.safe_combo_n4 = 0  # This number is needed to open the safe

        self.safe_number_n1 = self.safe_combo_n1
        self.safe_number_n2 = self.safe_combo_n2
        self.safe_number_n3 = self.safe_combo_n3
        self.safe_number_n4 = self.safe_combo_n4
        self.safe_color_c1 = self.color_number_1
        self.safe_color_c2 = self.color_number_2

        self.safe_opened = False # Default = False todo change to false
        self.safe_combo_random = []
        self.safe_combo = []
        self.safe_alpha_pra_answer = None
        self.tv_color_numbers = []
        self.turn_safe_on_channel = None
        self.safe_alpha_index = 0
        self.safe_combo_a1 = 0 # This number is needed to open the safe

        # Default room view
        self.fourth_wall = False  # Default = False
        self.current_room_view = 0
        
        # Default Drill Down Room Views
        self.drill_possible = False  # Default = False
        self.room_view_drill_down = 0  # Default = 0

        # Drawer Opened Settings
        self.fcd1_opened = False  # Default = False
        self.fcd2_opened = False  # Default = False
        self.dd1_opened = False  # Default = False
        self.dd2_opened = False  # Default = False
        self.dd3_opened = False  # Default = False

        self.dd3_open_attempts = 0  # Default = 0
        self.fc2_open_attempts = 0  # Default = 0
        self.desk_drawer_up = False

        # Locked Settings
        self.fcd1_locked = False  # Default = False
        self.fcd2_locked = True  # Default = True // Unlocked with Purple Key
        self.dd1_locked = True  # Default = True // Unlocked with Green Key
        self.dd2_locked = False  # Default = False
        self.dd3_locked = True  # Default = True // Unlocked with Red Key
        self.door_locked = True  # Default = True // Unlocked with Door Key (Gold)

        # Door Settings
        self.door_opened = False  # Default = False todo change to false
        self.door_number = None
        self.konar_number = None # Street sign in Camera 2
        self.cam_two_number = None

        # Lights Settings
        self.lights_on = True  # Default = False todo change to false
        self.lights_beginning = True
        
        # Settings for Red and Blue Book
        self.red_book_opened = False  # Default = False
        self.blue_book_opened = False  # Default = False
        self.yellow_book_opened = False  # Default = False
        self.current_page = 1  # Default = 1
        self.current_book = None
        self.diary_choice = 0

        # Papers Inventory Item Settings
        self.papers_opened = False  # Default = False
        self.current_paper_in_view = 1  # Default = 1

        # Problem A Settings

        # Problem B Settings
        self.prb_n1 = 0
        self.prb_n2 = 0
        self.prb_code = 0

        # Puzzle A Settings
        self.pua_code = 0
        self.pua_double_digits = []

        # Puzzle B Settings
        self.pub_n1 = 0
        self.pub_n3 = 0
        self.pub_n2 = 0
        self.pub_n4 = 0
        self.pub_n5 = 0
        self.pub_n6 = 0
        self.pub_n7 = 0
        self.pub_n8 = 0
        self.pub_n9 = 0
        self.pub_code = 0

        # Control Panel
        self.control_panel_on = False

        # Channel Codes
        self.channel_code = 0
        self.list_to_display_on_egg = []


        # Color Code List --- MOSTLY STATIC --- name: number[0], letter[1], color[2]
            # The numbers will change every time a new game is started
        self.color_codes = {'purple': [1, 'p', self.purple],
                            'blue': [2, 'b', self.blue],
                            'green': [3, 'g', self.green],
                            'yellow': [4, 'y', self.bright_yellow],
                            'orange':[5, 'o', self.orange],
                            'red': [6, 'r', self.red]}




        self.settings_dictionary = {}

        # Inventory Item Selection
        self.selected_item_index = None
        self.selected_item = None
        self.offset = None
        self.item_selection_choice = False
        self.selected_item_start_x = 0
        self.selected_item_start_y = 0
    

