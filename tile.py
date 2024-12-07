import pygame

class Tile():

    def __init__(self, rect, color, outline_color) -> None:
        self.rect = rect
        self.color = color
        self.outline_color = outline_color
        self.movement_speed = 5

    def show(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, screen_size, is_direction_up=None):
        
        # There needs to be a check wheter this tile will collide with another tile. if so, then the move should cancel

        adjustment = -self.movement_speed if is_direction_up else self.movement_speed

        adjusted_y = self.rect.y + adjustment if is_direction_up is not None else self.rect.y

        if self.is_out_of_border(screen_size, adjusted_y): return

        self.rect.y = adjusted_y

    def is_out_of_border(self, screen_size, adjusted_y):
        
        return adjusted_y < 0 or adjusted_y + self.rect.height > screen_size[1]
