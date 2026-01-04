from pygame import *

init()

screen_width, screen_height = 600, 500
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Ping-Pong launcher")

u_font = font.Font(None, 80)

def fit_text(text, max_width, max_height, text_colour):
    size = max_height
    while size > 1:
        f = font.Font(None, size)
        text_surf = f.render(text, True, (0, 0, 0))
        if text_surf.get_width() <= max_width and text_surf.get_height() <= max_height:
            return f, text_surf
        size -= 1

mouse_click = "n"

class Button:
    def __init__(self, pos, size, colour, hover_colour, text, text_colour):
        self.pos = pos
        self.size = size
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.text_colour = text_colour

        self.font, self.text_surf = fit_text(self.text, self.size[0], self.size[1], self.text_colour)
        self.text_pos = (int(self.pos[0]+(self.size[0]-self.text_surf.get_width())/2), int(self.pos[1]+(self.size[1]-self.text_surf.get_height())/2))

        self.rect = Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):

        if self.rect.collidepoint(mouse.get_pos()):
            draw.rect(screen, self.hover_colour, self.rect)
            screen.blit(self.text_surf, self.text_pos)

            if mouse_click == "l":
                return True
        
        else:
            draw.rect(screen, self.colour, self.rect)
            screen.blit(self.text_surf, self.text_pos)

        return False
    
    def update_font(self, new_text):
        self.text = new_text
        self.font, self.text_surf = fit_text(self.text, self.size[0], self.size[1], self.text_colour)
        self.text_pos = (int(self.pos[0]+(self.size[0]-self.text_surf.get_width())/2), int(self.pos[1]+(self.size[1]-self.text_surf.get_height())/2))


play_button = Button((100, 25), (400, 125), (150, 150, 150), (125, 125, 125), "Play", (50, 50, 50))
ip_button = Button((100, 175), (400, 125), (150, 150, 150), (125, 125, 125), " Enter IP Adress ", (50, 50, 50))
port_button = Button((100, 325), (400, 125), (150, 150, 150), (125, 125, 125), " Enter Port ", (50, 50, 50))

selected_button = "0"

pressed_key = ""

ip_text = ""
port_text = ""

run = True

while run:
    screen.fill((255, 255, 255))

    if play_button.update():
        print("play")

    if ip_button.update():
        selected_button = "ip"
        ip_button.update_font("...")
        if port_text == "":
            port_button.update_font(" Enter Port ")

    elif port_button.update():
        selected_button = "port"
        if ip_text == "":
            ip_button.update_font(" Enter IP Adress ")
        port_button.update_font("...")
    
    elif mouse_click == "l":
        selected_button = "0"
        if ip_text == "":
            ip_button.update_font(" Enter IP Adress ")
        if port_text == "":
            port_button.update_font(" Enter Port ")
    
    if selected_button == "ip":
        if pressed_key == "SKBACKSPACE":
            ip_text = ip_text[:-1]
        else:
            ip_text += pressed_key
        ip_button.update_font(ip_text)

    elif selected_button == "port":
        if pressed_key == "SKBACKSPACE":
            port_text = port_text[:-1]
        else:
            port_text += pressed_key
        port_button.update_font(port_text)

    pressed_key = ""
    mouse_click = "n"

    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                mouse_click = "l"
        
        if e.type == KEYUP:
            if e.key == K_BACKSPACE:
                pressed_key = "SKBACKSPACE"
            else:
                pressed_key = e.unicode
    
    display.update()
