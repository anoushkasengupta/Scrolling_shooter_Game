import pygame

pygame.init()

screen_width = 800
screen_height = int(screen_width*0.8)

screen_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game')

class soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('1player.png')
        self.image = pygame.transform.scale(img, (int(img.get_width()* scale), int(img.get_height()* scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
       
player = soldier(200, 200, 2)
player2 = soldier(400, 200, 2)

run = True
while run:
    
    screen_window.blit(player.image, player.rect)
    screen_window.blit(player2.image, player2.rect)
    
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False          
            
    pygame.display.update()           
            
pygame.quit()
            