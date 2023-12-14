import pygame
import time
import math

pygame.font.init()

#function that resizes images utilizing the given factor of the specific image  
def size(image, factor):
    resize = pygame.transform.scale(image, (round(image.get_width() * factor), round(image.get_height() * factor)))
    return resize 

# displaying all the images that are used 
GRASS = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//grass.png"), 2.5)
# included track image, and a border to help with any future collision development 
TRACK = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//track.png"), 0.8)
TRACK_BORDER = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//track_border.png"), 0.8)

RED_CAR = size(pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//red-car.png"), 0.6)

# assigning the position of the finish line to be one the track 
FINISH = pygame.image.load("//Users//rachelbarume//Desktop//Inclasspractice//2140 Final Project//images//finish.png")
FINISH_POS = (40, 250)

#setting the window dimensions to be the exact dimension of the border so it take up the whole screen 
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Begin the Race!")

# display text font and font size 
big_font = pygame.font.SysFont("comicsans", 44)

#display text colors used 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#renders and displays image text 
def blit_text(win, font, text, color, x, y):
    render = font.render(text, 1, color)
    win.blit(render, (x, y))

#class that can be utilized for any levels if game is continued
class GameLevel:
    LEVELS = 1 

    def __init__(self, level=1):
        self.level = level 
        self.started = False
        self.start_time = 0

    def start_new_level(self):
        # Set the game as started and record the start time
        self.started = True 
        self.start_time = time.time()

    def restart(self):
        # Reset the game to level 1 and set it as not started
        self.level = 1
        self.started = False 
        self.start_time = 0
    
    def exit_game(self):
        # Check if the player has left 
        return self.level > self.LEVELS
    
# a class that can be used by multiple cars and a computer automated car if the game was continued
class GeneralCar:
    def __init__(self, car_speed, rotation_speed, rotation_angle):
        self.car_speed = car_speed
        self.rotation_speed = rotation_speed  
        self.rotation_angle = rotation_angle 

    def move_forward(self, x, y):
        # Calculate new position after moving forward
        new_y = y - car_speed * math.cos(math.radians(rotation_angle))
        new_x = x - car_speed * math.sin(math.radians(rotation_angle))
        return self.adjust_position(new_x, new_y)

    def move_backward(self, x, y):
        # Calculate new position after moving backward
        new_y = y + car_speed * math.cos(math.radians(rotation_angle))
        new_x = x + car_speed * math.sin(math.radians(rotation_angle))
        return self.adjust_position(new_x, new_y)

    def adjust_position(self, x, y):
        # Ensure the new position is within the screen boundaries
        x = max(0, min(x, WIDTH))
        y = max(0, min(y, HEIGHT))
        return x, y

# class that inherates from the general car game 
class Player(GeneralCar):
    def __init__(self, x, y, rotation_angle, car_speed, rotation_speed):
        super().__init__(car_speed, rotation_speed, rotation_angle)
        self.x = x
        self.y = y

    #controls the car by keyboard keys 
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        global x, y, rotation_angle

        if keys[pygame.K_RIGHT]:
            rotation_angle -= self.rotation_speed
        elif keys[pygame.K_LEFT]:
            rotation_angle += self.rotation_speed

        if keys[pygame.K_UP]:
            x, y = self.move_forward(x, y)
        elif keys[pygame.K_DOWN]:
            x, y = self.move_backward(x, y)



# Initialize clock and frames per second
clock = pygame.time.Clock()
FPS = 60

# Set initial player position and parameters
x = 170
y = 170
car_speed = 5
rotation_speed = 5  
rotation_angle = 0 

# Create Player instance
player = Player(x, y, rotation_angle, 5, 5)

# Define images to be displayed
images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POS)]

# Function to draw text on the window
def draw_text(text, color, x, y):
    text_surface = big_font.render(text, True, color)
    WIN.blit(text_surface, (x, y))

# Create GameLevel instance
game_level = GameLevel()

# Set initial text position 
text_x = WIDTH / 2 - big_font.size(f"Please press any key to begin level: {game_level.level}.")[0] / 2
text_y = HEIGHT / 2 - big_font.size(f"Please press any key to begin level: {game_level.level}.")[1] / 2


#game loop 
play = True 
while play:
    pygame.display.update()

    clock.tick(FPS)

    rotation_angle %= 360
    if not game_level.started:
        blit_text(WIN, big_font, f"Press any key to begin level: {game_level.level}", (200, 200, 200), text_x, text_y)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game_level.started = True

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
