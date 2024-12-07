from button import Button
import pygame

class ButtonContainer():

    def __init__(self, center_x, center_y, button_width, button_height, horizontal_space, vertical_space, button_alignment, custom_font) -> None:
        self.buttons = []

        self.center_x = center_x
        self.center_y = center_y
        self.button_width = button_width
        self.button_height = button_height
        self.horizontal_space = horizontal_space
        self.vertical_space = vertical_space
        self.button_alignment = button_alignment # could be 'vertical' or 'horizontal'
        self.custom_font = custom_font
    
    def add_button(self, text, ôn_click_func, color, hover_color, click_color, outline_color):

        buttons_len = len(self.buttons) + 1

        rect = pygame.Rect(0, 
                           0,
                           self.button_width,
                           self.button_height)

        rect.centerx = self.center_x
        rect.centery = self.center_y

        if self.button_alignment == 'horizontal':
            rect.x += self.button_width * buttons_len

            if buttons_len > 1:
                
                rect.x += self.horizontal_space * (buttons_len - 1)
        
        elif self.button_alignment == 'vertical':
            rect.y += self.button_height * buttons_len
            
            if buttons_len > 1:
                
                rect.y +=  self.vertical_space * (buttons_len - 1)

        button = Button(rect, self.custom_font.get_custom_text(text, rect.centerx, rect.centery), ôn_click_func, color, hover_color, click_color, outline_color)

        self.buttons.append(button)
    
    def show_buttons(self, surface):
        for button in self.buttons:
            button.show(surface)