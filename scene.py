import pygame
from customfont import CustomFont
from button import Button
from buttoncontainer import ButtonContainer
from tile import Tile
# import json
# from types import SimpleNamespace

class Scene():

    def __init__(self) -> None:
        win_size = pygame.display.get_window_size()

        self.standard_button_font_index = -1

        self.fonts = []
        self.buttons = []
        self.button_containers = []
        self.texts = []

    def add_button(self, rect, text, color, hover_color, click_color, outline_color):
        self.buttons.append(Button(rect, self.standard_button_font.get_custom_text(text, rect.centerx, rect.centery), color, hover_color, click_color, outline_color))

    def add_button_container(self, x, y, width, height, horizontal_space, vertical_space, button_alignment, font_index):
        try:
            container = ButtonContainer(x, y, width, height, horizontal_space, vertical_space, button_alignment, self.fonts[font_index])
        except IndexError:
            raise Exception('The given font index is not present in fonts of this scene.')
        
        self.button_containers.append(container)

        return self.button_containers.index(container)

    def add_container_button(self, container_index, text, ôn_click_func, color, hover_color, click_color, outline_color):
        self.button_containers[container_index].add_button(text, ôn_click_func, color, hover_color, click_color, outline_color)

    def add_font(self, font_file, font_size, font_color):
        font = CustomFont(font_size, font_color, font_file)
        
        self.fonts.append(font)

        return self.fonts.index(font)

    def set_button_font(self, font_index):
        self.standard_button_font = self.fonts[font_index]

    def add_text(self, text, center_x, center_y, font_index):
        if self.fonts[font_index] == None: pass

        self.texts.append(self.fonts[font_index].get_custom_text(text, center_x, center_y))

    def show(self, surface):
        for button in self.buttons:
            button.show(surface)

        for button_container in self.button_containers:
            button_container.show_buttons(surface)

        for text in self.texts:
            text.show(surface)

    def get_button_by_position(self, pos):
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                return button
        
        for container in self.button_containers:
            for button in container.buttons:
                if button.rect.collidepoint(pos):
                    return button

    def reset_button_color_flags(self):
        for button in self.buttons:
            button.hovered = False 
            button.clicked = False
        
        for container in self.button_containers:
            for button in container.buttons:
                button.hovered = False 
                button.clicked = False


    def handle_mouse_motion(self):
        self.reset_button_color_flags()

        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)
        
        if (button == None): return

        button.hovered = True

    def handle_mouse_button_down(self):
        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)

        if (button == None): return

        button.clicked = True

        print(f"Mouse Position: [{mouse_pos[0]}, {mouse_pos[1]}]")
    
    def handle_mouse_button_up(self):
        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)
        
        if (button == None or not button.clicked): return

        button.on_click()

        self.reset_button_color_flags()
