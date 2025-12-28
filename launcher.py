from pygame import *

init()

screen_width, screen_height = 600, 500
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Ping-Pong launcher")

font = font.Font(None, 36)

mouse_click = "n"

class Button:
    def __init__(self, pos, size, colour, hover_colour, text, text_colour):
        self.pos = pos
        self.size = size
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.text_colour = text_colour
    
        self.rect = Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        if mouse.get_pos():
            pygame.draw.rect(screen, self.hover_colour, self.rect)
            text = font.render(self.text, True, self.text_colour)
            screen.blit(text, self.rect)

            if mouse_click == "l":
                return True

        pygame.draw.rect(screen, self.colour, self.rect)
        text = font.render(self.text, True, self.text_colour)

        return False

play_button = Button((100, 75), (400, 125), (150, 150, 150), (125, 125, 125), "Play", (50, 50, 50))

run = True

while run:
    screen.fill((255, 255, 255))

    if play_button.update:
        print("play")

    mouse_click = "n"
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 0:
                mouse_click = "l"
    
    display.update()