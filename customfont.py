import pygame

class CustomFont():

    def __init__(self, px_size, text_color, font_file, background_Color=None) -> None:
        self.text_color = text_color
        self.background_Color = background_Color
        self.font = pygame.font.Font(font_file, px_size)

    def from_json(self):
        pass

    def get_custom_text(self, text, center_x, center_y):
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (center_x, center_y)

        return CustomText(self.text, self.text_rect)

class CustomText(CustomFont):

    def __init__(self, text, text_rect) -> None:
        
        self.text = text
        self.text_rect = text_rect

    def show(self, surface):
        surface.blit(self.text, self.text_rect)
