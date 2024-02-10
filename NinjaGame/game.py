import pygame
import sys

class Game:
    def __init__(self) -> None:
        pygame.init()
        #change window name
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # sets background color of cloud to black

        self.img_pos = [160, 260]
        self.movement = [False, False] # [up, down]

        #making rectangle collision area
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) # adds blue background
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 10 # booleans 1 and 0, y movement is calculated based on key press

            self.screen.blit(self.img, self.img_pos) # top left is (0, 0), screen.blit to show on our screen

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) # creates rectangle (0, 0, w, h)

            #collision test
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area) # draws out collision area rect on screen in color
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area) # not colliding, diff color
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP: # up key . demonstrate to move cloud
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP: # up key . demonstrate to move cloud
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            
            pygame.display.update()
            self.clock.tick(60) # loop runs at 60 fps

Game().run()