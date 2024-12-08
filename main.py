import socket
import pygame
from scene import Scene
from GameScene import GameScene
from customsocket import CustomSocket

BACKGROUND_COLOR = (20, 20, 20)
SCREEN_SIZE = (720, 360)
FONTFILE = 'ARCADE_I.TTF'
PROGRAM_STATE = 'MENU'
TPS = 60
NET_RULE = 'CLIENT' # CLIENT OR HOST

pygame.init()
pygame.display.init()
pygame.display.set_caption('Ping Pong')

clock = pygame.time.Clock()
surface = pygame.display.set_mode(SCREEN_SIZE)

socket = CustomSocket()
if NET_RULE == 'HOST':
    socket.start_listening(8000)

if NET_RULE == 'CLIENT':
    socket.connect('192.168.0.192', 8000)

def update_surface(surface):
    global BACKGROUND_COLOR, SHOW_CALLS, PROGRAM_STATE 
    surface.fill(BACKGROUND_COLOR)

    SHOW_CALLS[PROGRAM_STATE](surface)

    pygame.display.update()

def handle_events():
    global MOUSE_EVENTS, KEYBOARD_EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        
        if event.type in MOUSE_EVENTS:
            MOUSE_EVENTS[event.type]()
        
        if event.type == pygame.KEYDOWN:
            if event.key in KEYBOARD_EVENTS.keys():
                KEYBOARD_EVENTS[event.key] = True
                """
                keyboard_event = KEYBOARD_EVENTS[event.key]
                keyboard_event['method'](keyboard_event['scene'], keyboard_event['tile_index'], keyboard_event['y_adjustment'])
                """

        if event.type == pygame.KEYUP:
            if event.key in KEYBOARD_EVENTS.keys():
                KEYBOARD_EVENTS[event.key] = False

def quit_program():
    pygame.quit()
    quit(0)

def start_game():
    global PROGRAM_STATE
    PROGRAM_STATE = 'GAME'

def switch_hosting():
    global PROGRAM_STATE
    PROGRAM_STATE = 'HOSTING'

def to_do():
    print('This button needs functionality.')

# Menu Init
MenuScene = Scene()
menu_title_font_index = MenuScene.add_font(FONTFILE, 30, (200,200,200))
menu_button_font_index = MenuScene.add_font(FONTFILE, 15, (175,175,175))
MenuScene.set_button_font(menu_button_font_index)

MenuScene.add_text('Pong Multiplayer', SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 * 0.35, menu_title_font_index)

button_container_index = MenuScene.add_button_container(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2, 80, 30, 30, 30, 'vertical', menu_button_font_index)

MenuScene.add_container_button(button_container_index, 'Join', start_game, (0,153,0), (0,122,0), (0,92,0), (200,200,200))
MenuScene.add_container_button(button_container_index, 'Host', switch_hosting, (255,140,0), (204,112,0), (153,84,0), (200,200,200))
MenuScene.add_container_button(button_container_index, 'Quit', quit_program, (153,0,0), (122,0,0), (92,0,0), (200,200,200))

# Hosting Init

HostingScene = Scene()
hosting_title_font_index = HostingScene.add_font(FONTFILE, 30, (200,200,200))
HostingScene.add_text('Hosting', SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 * 0.35, hosting_title_font_index)

# Game Init

MainScene = GameScene(SCREEN_SIZE)

game_tile_a_index = MainScene.add_tile(pygame.Rect(SCREEN_SIZE[0] * 0.1, SCREEN_SIZE[1] / 2, 20, 100), (222, 222, 222), (0,0,0))
game_tile_b_index = MainScene.add_tile(pygame.Rect(SCREEN_SIZE[0] * 0.9, SCREEN_SIZE[1] / 2, 20, 100), (222, 222, 222), (0,0,0))
ball_tile_index = MainScene.add_ball_tile(pygame.Rect(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2, 20, 20), (222, 222, 222), (0,0,0))

MOUSE_EVENTS = {
    pygame.MOUSEBUTTONDOWN: MenuScene.handle_mouse_button_down,
    pygame.MOUSEBUTTONUP: MenuScene.handle_mouse_button_up,
    pygame.MOUSEMOTION: MenuScene.handle_mouse_motion
}

KEYBOARD_EVENTS = {
    pygame.K_UP: False,
    pygame.K_DOWN: False
}

SHOW_CALLS = {
    'MENU': MenuScene.show,
    'GAME': MainScene.show,
    'HOSTING': HostingScene.show
}

while True:
    
    clock.tick(TPS)
    handle_events()

    if NET_RULE == 'HOST':
        socket.listen()

    if NET_RULE == 'CLIENT':
        socket.send_data(b'ich in eif dae geilschti siech.')

    if PROGRAM_STATE == 'GAME':
        MainScene.handle_tile_movement(game_tile_a_index, SCREEN_SIZE, KEYBOARD_EVENTS)
        MainScene.handle_tile_movement(ball_tile_index, SCREEN_SIZE, KEYBOARD_EVENTS)

    update_surface(surface)
