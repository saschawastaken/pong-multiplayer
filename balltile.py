import pygame
from tile import Tile

class BallTile(Tile):

    def __init__(self, rect, color, outline_color) -> None:
        super().__init__(rect, color, outline_color)
        self.standard_vel_x = 5
        self.standard_vel_y = 5
        self.velocity_x = self.standard_vel_x
        self.velocity_y = self.standard_vel_y
    
    def move(self, screen_size, collided_tile=None):

        if collided_tile:
            is_vertical_collision = self.rect.left <= collided_tile.rect.right or self.rect.right >= collided_tile.rect.left

            modification = self.get_vertical_velocity_modification(collided_tile) if is_vertical_collision else self.get_horizontal_velocity_modification(collided_tile)
            
            self.velocity_y = self.standard_vel_y * modification if is_vertical_collision else self.velocity_y * -1
            self.velocity_x = self.standard_vel_x * modification if not is_vertical_collision else self.velocity_x * -1

        adjusted_x = self.rect.x + self.velocity_x
        adjusted_y = self.rect.y + self.velocity_y

        if self.is_out_of_horizontal_border(adjusted_y, screen_size[1]):
            self.velocity_y *= -1
            adjusted_y = self.rect.y + self.velocity_y

        if self.is_out_of_vertical_border(adjusted_x, screen_size[0]):
            self.velocity_x *= -1
            adjusted_x = self.rect.x + self.velocity_x

        self.rect.x = adjusted_x
        self.rect.y = adjusted_y

    def is_out_of_horizontal_border(self, y, screen_height):
        return y + self.rect.height >= screen_height or y <= 0
    
    def is_out_of_vertical_border(self, x, screen_width):
        return x + self.rect.width >= screen_width or x <= 0
    
    def get_vertical_velocity_modification(self, collided_tile):
        collision_point_y = self.rect.bottom if self.rect.y < collided_tile.rect.y else self.rect.y if self.rect.bottom > collided_tile.rect.bottom else self.rect.centery
        
        modification = (collision_point_y - collided_tile.rect.y - collided_tile.rect.height / 2) / collided_tile.rect.height
        
        return modification
    
    def get_horizontal_velocity_modification(self, collided_tile):
        collision_point_x = self.rect.right if self.rect.x < collided_tile.rect.x else self.rect.x if self.rect.right > collided_tile.rect.right else self.rect.centerx
        
        modification = (collision_point_x - collided_tile.rect.x - collided_tile.rect.width / 2) / collided_tile.rect.width

        return modification