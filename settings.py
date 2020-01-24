#kennex

import pygame

class Settings():
    """A class to store settings for Escape the Room.
    
    gs stands for "Game Settings" and will be used throughout
    
    """
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (107, 126, 156)  # Walls
        
        # Game window Settings
        self.gw_width = self.screen_width * .88  # Default is .88
        self.gw_height = self.screen_height * .90  # Default is .90
        self.gw_border = 5

        # Fonts
        self.verdana12 = pygame.font.SysFont("Verdana", 12, True)
        self.verdana16 = pygame.font.SysFont("Verdana", 16, True)
        self.verdana18 = pygame.font.SysFont("Verdana", 18, True)
        self.verdana22 = pygame.font.SysFont("Verdana", 22, True)
        self.arial16 = pygame.font.SysFont("Arial", 16, True)
        self.arial22 = pygame.font.SysFont("Arial", 22, True)
        self.garamond16 = pygame.font.SysFont("Garamond", 16, True)
        self.garamond22 = pygame.font.SysFont("Garamond", 22, True)
        self.garamond30 = pygame.font.SysFont("Garamond", 30, True)


        # Sleep Ticker
        self.sleeperticks = True
        
        # Sidebar Settings
        self.sidebar_w = self.screen_width - self.gw_width
        self.sidebar_x = self.gw_width #- self.gw_border
        
        # Movement Settings in Game Window
        self.gw_move_w = self.gw_width * .03
        self.gw_right_x = self.sidebar_x - self.gw_move_w - self.gw_border
        
        # Clock / Save Area Settings
        #self.clock_box_h = ((self.screen_height - self.gw_height) * 2)
        #self.clock_box_y = self.screen_height - self.clock_box_h
        
        # Inventory Area Settings
        self.inventory_h = self.screen_height #- self.clock_box_h
        self.inv_item_w = self.sidebar_w / 2 * .8
        self.inv_item_h = self.sidebar_w / 2 * .8
        self.item_offset_w = self.gw_border * 2
        self.item_offset_h = self.gw_border * 2.5   

        # Textbox Area Settings
        self.text_box_w = self.gw_width
        self.text_box_h = self.screen_height - self.gw_height - (self.gw_border * 3)
        self.text_box_x = 0
        self.text_box_y = self.gw_height + self.gw_border*3
        
        # Colors
        self.white = (255, 255, 255)
        self.silver = (192, 192, 192)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.orange = (255, 165, 0)
        self.purple = (106, 13, 173)
        self.black = (0, 0, 0)
        self.yellow = (207, 181, 52)
        self.yellowish = (207, 181, 62)
        self.bright_yellow = (255, 255, 0)
        self.brown = (102, 51, 0)
        self.gray = (173, 168, 168)
        self.dark_gray = (53, 53, 53)
        self.dark_blue = (80, 92, 111) # Interior Walls
        
        self.carpet = (128, 128, 130)  # Carpet
        self.door = (81, 85, 88)  # Door / Fairly dark gray
        self.off_white = (226, 226, 224)
        self.file_cabinet = (193, 186, 168)
        self.interior_drawer = (149, 141, 116)
        self.wood = (100, 90, 89)
        self.dark_wood = (95, 90, 89)
        self.darker_wood = (69, 64, 63)
        self.tv_screen = (82, 82, 82)
        
        self.red_book_color = (120, 33, 33)  # Red One
        self.blue_book_color = (66, 72, 158)  # Blue one
        
        self.transcolor = (254, 254, 254, 0)
        self.clickboxcolor = (253, 253, 253)
        
        # Inventory Item Selection
        self.si = None  # si stands for selected item
        self.offset = None
        self.item_selection_choice = False
        self.si_start_x = 0
        self.si_start_y = 0
        
        # Inventory Items Found
        self.door_key_found = False
        self.fc_key1_found = False
        self.fc_key2_found = False
        self.dd_key_found = False
        self.remote_found = False
        self.batteries_found = False
        self.power_cord_found = False
        self.papers_found = False
        self.camera_manual_found = False
        self.chair_manual_found = False
        self.desk_drawer_removed = False

        # Stable Items in Inventory Settings
        self.stable_item_opened = False  # Default = False

        # Remote Settings
        self.remote_opened = False  # Default = False
        self.close_remote = False  # Default = False
        self.batteries_input = False  # Default = False
        
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
        
        # Door Settings
        self.door_opened = False  # Default = False
        
        # TV Settings
        self.tv_on = False  # Default = False
        self.current_channel = None
        self.input_channel = None
        
        # Lights Settings
        self.lights_on = True  # Default = False
        
        # Manual Settings for Camera and Chair Manuals
        self.red_book_opened = False  # Default = False
        self.blue_book_opened = False  # Default = False
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
        self.control_panel_on = True

        # Channel Code
        self.channel_code = 0


        # Color Code List --- MOSTLY STATIC --- name: number[0], letter[1], color[2]
            # The numbers will change every time a new game is started
        self.color_codes = {'purple': [1, 'p', self.purple],
                            'blue': [2, 'b', self.blue],
                            'green': [3, 'g', self.green],
                            'yellow': [4, 'y', self.bright_yellow],
                            'orange':[5, 'o', self.orange],
                            'red': [6, 'r', self.red]}


        
        
        
        
    
    