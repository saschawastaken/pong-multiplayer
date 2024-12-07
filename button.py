import pygame

class Button():

    def __init__(self, rect, text, on_click_func, color, hover_color, click_color, outline_Color) -> None:
        self.rect = rect
        self.color = color
        self.hover_color = hover_color
        self.click_color = click_color
        self.text = text
        self.hovered = False
        self.clicked = False
        self.on_click_func = on_click_func

    def show(self, surface):
        conditional_color = {self.hovered: self.hover_color, self.clicked: self.click_color}.get(True, self.color)
        
        pygame.draw.rect(surface, conditional_color, self.rect)
        self.text.show(surface)

    def on_click(self):
        try:
            self.on_click_func()
        except Exception as error:
            raise Exception(f'The function of the button encountered an error: {error}')