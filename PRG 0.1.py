import pygame
import sys


pygame.init()
pygame.mixer.init()


BLACK = 0, 0, 0


winWidth = 800
winHeight = 600
FPS = 30
screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hack n Slash")
background_image_filename = 'Assets/Background Assets/PNG/Battleground3/Bright/Battleground3.png'
background = pygame.image.load(background_image_filename).convert()
bg_rect = background.get_rect()
clock = pygame.time.Clock()


player_image_filename = 'Assets/Idle Animation/Idle1.png'
player_image = pygame.image.load(player_image_filename).convert()
player_image.set_colorkey(BLACK)


def gameExit():
    pygame.quit()
    sys.exit()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (winWidth / 2, winHeight / 2)
        self.rect.bottom = winHeight


game_sprites = pygame.sprite.Group()
player = Player()
game_sprites.add(player)

while True:
    clock.tick(FPS)
    screen.blit(background, bg_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()

        game_sprites.update()
        game_sprites.draw(screen)
        pygame.display.flip()

