import pygame
from customfont import CustomFont
from button import Button
from buttoncontainer import ButtonContainer
from tile import Tile
from balltile import BallTile
from scene import Scene
# import json
# from types import SimpleNamespace

class GameScene(Scene):

    def __init__(self, screen_size) -> None:
        self.tiles = []
        self.tile_movement_step = 10
        self.screen_size = screen_size
        self.tile_scores = []
        super().__init__()

    def add_tile(self, rect, color, outline_color):
        tile = Tile(rect, color, outline_color)
        self.tiles.append(tile)

        return self.tiles.index(tile)

    def add_ball_tile(self, rect, color, outline_color):
        tile = BallTile(rect, color, outline_color)
        self.tiles.append(tile)

        return self.tiles.index(tile)

    def add_tile_score(self, tile_index):
        self.tile_scores[tile_index] = 0
    
    def increment_tile_score(self, tile_index):
        self.tile_scores[tile_index] += 1

    def is_out_of_border(self, x, y, width, height):
        return x < 0 or x + width > self.screen_size[0] or y < 0 or y + height > self.screen_size[1]

    def show(self, surface):
        for button in self.buttons:
            button.show(surface)

        for button_container in self.button_containers:
            button_container.show_buttons(surface)

        for text in self.texts:
            text.show(surface)
        
        for tile in self.tiles:
            tile.show(surface)
    
    def get_tile_collision(self, collision_tile):
        
        tiles = [tile for tile in self.tiles if tile != collision_tile]

        for tile in tiles:
            if tile.rect.colliderect(collision_tile):
                return tile

    def handle_tile_movement(self, tile_index, screen_size, keyboard_events):
        tile = self.tiles[tile_index]
        collided_tile = self.get_tile_collision(tile)

        if isinstance(tile, BallTile):    
            tile.move(screen_size, collided_tile)
            return

        if collided_tile != None: return

        movements = tuple(keyboard_events.values())
        # print(movements)
        # print((tuple(keyboard_events) == (True,True) or tuple(keyboard_events) == (False,False)))
        if (movements == (True,True) or movements == (False,False)): return
        
        tile.move(self.screen_size, keyboard_events[pygame.K_UP])