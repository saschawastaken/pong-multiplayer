import pygame
from customfont import CustomFont
from button import Button

class Menu():

    def __init__(self, font_file, button_font) -> None:
        win_size = pygame.display.get_window_size()

        self.title_font = CustomFont(30, (200,200,200), font_file)
        self.title = self.title_font.get_custom_text('Pong Multiplayer', win_size[0] / 2, win_size[1] / 2)
        self.button_font = button_font
        # self.standardButtonFont
        self.buttons = []

    def add_button(self, rect, color, hover_color, click_color, outline_color, text):
        self.buttons.append(Button(rect, color, hover_color, click_color, outline_color, self.button_font.get_custom_text(text, rect.centerx, rect.centery)))

    def show(self, surface):
        self.title.show(surface)

        for button in self.buttons:
            button.show(surface)

    def get_button_by_position(self, pos):
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                return button

    def reset_button_color_flags(self):
        for button in self.buttons:
            button.hovered = False 
            button.clicked = False

    def handle_mouse_motion(self):
        self.reset_button_color_flags()

        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)
        
        if (button == None): return

        button.hovered = True

    def handle_mouse_button_down(self):
        self.reset_button_color_flags()
        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)

        if (button == None): return

        button.clicked = True

        print(f"Mouse Position: [{mouse_pos[0]}, {mouse_pos[1]}]")
    
    def handle_mouse_button_up(self):
        self.reset_button_color_flags()
        mouse_pos = pygame.mouse.get_pos()

        button = self.get_button_by_position(mouse_pos)
        
        if (button == None or not button.clicked): return

        print('Button clicked!')