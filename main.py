
import pygame
import time
import math


class BothCars:
    def __init__(self, car_speed, rotation_speed, rotation_angle):
        self.car_speed = car_speed
        self.rotation_speed = rotation_speed  
        self.rotation_angle = rotation_angle 


    def move_forward(self, x, y):
        y -= car_speed * math.cos(math.radians(rotation_angle))
        x -= car_speed * math.sin(math.radians(rotation_angle))
        return x, y

    def move_backward(self, x, y):
        y += car_speed * math.cos(math.radians(rotation_angle))
        x += car_speed * math.sin(math.radians(rotation_angle))
        return x, y


class Player(BothCars):
    def __init__(self, x, y, rotation_angle, car_speed, rotation_speed):
        super().__init__(car_speed, rotation_speed, rotation_angle)  # Calls the __init__ method of the parent class
        self.x = x
        self.y = y
        


    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        global x, y, rotation_angle

        if keys[pygame.K_RIGHT]:
            rotation_angle -= rotation_speed
        elif keys[pygame.K_LEFT]:
            rotation_angle += rotation_speed

        if keys[pygame.K_UP]:
            x, y = self.move_forward(x, y)
        elif keys[pygame.K_DOWN]:
            x, y = self.move_backward(x, y)

def size(image, factor):
    resize = pygame.transform.scale(image, (round(image.get_width() * factor), round(image.get_height() * factor)))
    return resize 

clock = pygame.time.Clock()
FPS = 60

GRASS = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//grass.png"), 2.5)

TRACK = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//track.png"), 0.8)
TRACK_BORDER = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//track_border.png"), 0.8)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

RED_CAR = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//red-car.png"), 0.6)
WHITE_CAR = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//white-car.png"), 0.6)

FINISH = pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//finish.png")
FINISH_POS= (40, 250)



WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Begin the Race!")

pygame.font.init()


x = 170
y = 170
car_speed = 5
rotation_speed = 5  
rotation_angle = 0 

player = Player(x, y, rotation_angle, 5, 5)

images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POS), (TRACK_BORDER, (0, 0))]

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    WIN.blit(text_surface, text_rect)

   


play = True 
while play:
    pygame.display.update()

    clock.tick(FPS)

    rotation_angle %= 360

    for img, pos in images:
        WIN.blit(img, pos)

    player_img = pygame.transform.rotate(RED_CAR, rotation_angle)
    player_rect = player_img.get_rect(center=(x, y))
    WIN.blit(player_img, player_rect.topleft)

    player.keyboard_control()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            break 

    
pygame.quit()