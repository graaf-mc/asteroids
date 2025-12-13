import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from logger import log_event, log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.colides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        log_state()

        # FrameRate = 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
