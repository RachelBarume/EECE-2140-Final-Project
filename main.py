import pygame
import time
import math
#make sure to comment all the code 
# make test code for like the classes and methods 
#make many different methods to call the gui 
#cuz you dont want to be wondering where the bug is coming form so you test different sections 
class both_cars:
    def __init__(self, car_speed, rotation_speed):
        self.car_speed = car_speed
        self.roation_speed = rotation_speed
          

    def move_forward(self, x, y, rotation_angle):
        y -= car_speed * math.cos(math.radians(rotation_angle))
        x -= car_speed * math.sin(math.radians(rotation_angle))

    def move_backward(self, x, y, rotation_angle):
        y += car_speed * math.cos(math.radians(rotation_angle))
        x += car_speed * math.sin(math.radians(rotation_angle))
    
    #should include how to stay within the boarder so both player and computer can inherant 

class Player(both_cars):
    def __init__(self, car_speed, rotation_speed):
        super().__init__(car_speed, rotation_speed)  # Calls the __init__ method of the parent class
        self.rotation_angle = 0  
    
    def keyboard_control(self):
        global x, y, rotational_angle
   
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            rotation_angle -= rotation_speed
        if keys[pygame.K_LEFT]:
            rotation_angle += rotation_speed
        if keys[pygame.K_UP]:
            self.move_forward()
        if keys[pygame.K_DOWN]:
            self.move_backward()

class Computer(both_cars):
    #figure out how to get it to move on its own 
    def __init__(self, car_speed, rotation_speed, path=[]):
        super().__init__(car_speed, rotation_speed)
        self.path = PATH 
        self.speed = car_speed 
        self.position = 0


def size(image, factor):
    resize = pygame.transform.scale(image, (round(image.get_width() * factor), round(image.get_height() * factor)))
    return resize 

clock = pygame.time.Clock()
FPS = 60
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]


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

x = 170
y = 170
car_speed = 5
rotation_speed = 5  

play = True 
rotation_angle = 0 

#both_cars = both_cars()
player = Player(5,5)
computer = Computer(5,5)

images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POS), (TRACK_BORDER, (0, 0))]

while play:
    pygame.display.update()

    clock.tick(FPS)
    
    # Update the rotation angle to be within 0 to 360 degrees
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

    pygame.display.flip()

pygame.quit()
