import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    bg = pygame.image.load('img/bg.jpg')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def Background(image):
        size = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(size, (0, 0))
    clock = pygame.time.Clock()
    score = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    aster=pygame.sprite.Group()
    bullet=pygame.sprite.Group()

    Asteroid.containers = (aster, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (bullet, updatable, drawable)

    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)
        for a in aster:
            if (player.collision(a)):
                if player.is_dead():
                    print(f'Game Over!\n|__Your score is {score}')
                    return
                else:
                    player.respawn()
            for b in bullet:
                if b.collision(a):
                    score += 1
                    a.split()
        screen.fill('black')
        Background(bg)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        t = clock.tick(60)
        dt = t/1000

if __name__ == '__main__':
    main()