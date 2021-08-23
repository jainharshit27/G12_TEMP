import pygame

class Dino:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
        
class Cactus:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino = pygame.image.load("sprites/trex1.png")
cacti = pygame.image.load("sprites/obstacle1.png")
ground = pygame.image.load("sprites/ground.png")

dino_rect = Dino(100, 250, 64, 64)
cactus_rect = Cactus(1100, 275, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    dino_rect.paste_image(dino)
    cactus_rect.paste_image(cacti)
    
    image_width = ground.get_width()
    screen.blit(ground, ground_rect)
    screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
    if ground_rect.x <= -image_width:
        screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
        ground_rect.x = 0
    ground_rect.x -= 1

    pygame.display.update()
    pygame.time.delay(1)
