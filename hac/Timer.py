import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

counter, text = 10, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
       for e in pygame.event.get():
           if e.type == pygame.USEREVENT:
               counter -= 1
               text = str(counter).rjust(3) if counter > 0 else "Stop"
           if e.type == pygame.QUIT: break
       else:
           screen.fill((255, 255, 255))
           screen.blit(font.render(text, True, (0, 0, 0)), (350, 0))
           pygame.display.flip()
           clock.tick(60)
           continue
       break
