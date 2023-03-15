import pygame
import os
# Initializing the game
pygame.init()

# Settomg the window settings
winWidth = 800
winHeight = int(winWidth * 0.8)
screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hack n Slash")

# Creating Game Clock
clock = pygame.time.Clock()
FPS = 60

# Color Variables
BLACK = (0, 0, 0)

# Physics 
GRAVITY = 0.75

# Action Variables
moving_left = False
moving_right = False
attack_q = False
attack_e = False
attack_r = False

# Importing Background Image
background_image_filename = 'Assets/Background/Battleground3.png'
background = pygame.image.load(background_image_filename).convert()
bg_rect = background.get_rect()

# Function to put the background on the screen
def draw_bg():
    screen.blit(background, bg_rect)
    pygame.draw.line(screen, BLACK, (0,300), (winWidth, 300))

# Class to Create a Sprite
class Sprite(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Loop to Store Animations
        animation_types = ['Idle', 'Run', 'Jump']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'Assets/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                image = pygame.image.load(f'Assets/{self.char_type}/{animation}/{i}.png')
                image = pygame.transform.scale(image, (int(image.get_width() * scale),(int(image.get_height() * scale))))
                temp_list.append(image)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Function to Move Sprite
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        self.vel_y += GRAVITY

        if self.vel_y > 10:
            self.vel_y

        dy += self.vel_y

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy


    # Fucntion to Change the Animation
    def update_animation(self):
        Animation_Timer = 100
        self.image = self.animation_list[self.action][self.index]
        if pygame.time.get_ticks() - self.update_time > Animation_Timer:
            self.update_time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.animation_list[self.action]):
            self.index = 0

    # Function to Change Sprite Action
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            self.update_time = pygame.time.get_ticks()
    # Function to Draw Sprite to Screen
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

# Player and Mob Sprites
player = Sprite('Player', 200, 200, 1, 5)
mob = Sprite('SkeletonW', 300, 235, 1, 3)

# Start of Game Loop
run = True
while run:
    clock.tick(FPS)
    
    # Update Loop
    draw_bg()
    player.update_animation()
    mob.draw()
    player.draw()

    if player.alive:
        if player.in_air:
            player.update_action(2)
        elif moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(moving_left, moving_right)
    # Read in Imput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Key Presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
            if event.key == pygame.K_q:
                attack_q = True
            if event.key == pygame.K_ESCAPE:
                run = False

        # Key Releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    # Update Screen
    pygame.display.update()

pygame.quit()


