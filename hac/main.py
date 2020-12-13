import pygame
import random
from Player import Player
from Enemy import Enemy
from Coin import Coin

pygame.init()

size    = (800, 600)
BGCOLOR = (255, 255, 255)
screen = pygame.display.set_mode(size)
scoreFont = pygame.font.Font("fonts/UpheavalPro.ttf", 30)
healthFont = pygame.font.Font("fonts/OmnicSans.ttf", 50)
healthRender = healthFont.render('z', True, pygame.Color('red'))
pygame.display.set_caption("Top Down")
costOfBoost1 = 10
costOfBoost2 = 15
score = 0
done = False
hero = pygame.sprite.GroupSingle(Player(screen.get_size()))
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
lastEnemy = 0
clock = pygame.time.Clock()

    
def game_loop():
    done = False
    global costOfBoost1
    global score
    hero = pygame.sprite.GroupSingle(Player(screen.get_size()))
    print(hero.sprite.movementSpeed)
    enemies = pygame.sprite.Group()
    lastEnemy = pygame.time.get_ticks()
    lastEnemy = pygame.time.get_ticks()
    lastCoin = pygame.time.get_ticks()
    counter, text = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    while hero.sprite.alive and not done:
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        currentTime = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else "Stop"
                if text == "Stop":
                    done = True
            if event.type == pygame.QUIT:
                quit()

        screen.fill(BGCOLOR)
        screen.blit(font.render(text, True, (0, 0, 0)), (350, 0))
        clock.tick(60)
        process_keys(keys, hero)
        process_mouse(mouse, hero)

        # Enemy spawning process
        if lastEnemy < currentTime - 200 and len(enemies) < 50:
            spawnSide = random.random()
            if spawnSide < 0.25:
                enemies.add(Enemy((0, random.randint(0, size[1]))))
            elif spawnSide < 0.5:
                enemies.add(Enemy((size[0], random.randint(0, size[1]))))
            elif spawnSide < 0.75:
                enemies.add(Enemy((random.randint(0, size[0]), 0)))
            else:
                enemies.add(Enemy((random.randint(0, size[0]), size[1])))
            lastEnemy = currentTime

        if lastCoin < currentTime - 5000 and len(coins) < 20:
            coins.add(Coin((random.randint(0, 800), (random.randint(0, 600)))))
            lastCoin = currentTime

        move_entities(hero, enemies, clock.get_time() / 17)
        score += coinUp(hero, coins)
        render_entities(hero, enemies)

    #test buttons
        if keys[pygame.K_4]:
            if hero.sprite.movementSpeed < 25: 
                hero.sprite.movementSpeed += 0.1
                score -= costOfBoost1
                costOfBoost1 *= 1.05
                print(costOfBoost1,  hero.sprite.movementSpeed)
        if keys[pygame.K_5]:
            store()
        if keys[pygame.K_6]:
            score = 999999999
        
        # Health and score render
        for hp in range(hero.sprite.health):
            screen.blit(healthRender, (15 + hp * 35, 0))

        scoreRender = scoreFont.render(str(score), True, pygame.Color('gold'))
        scoreRect = scoreRender.get_rect()
        scoreRect.right = 780
        scoreRect.top = 560
        screen.blit(scoreRender, scoreRect)
        pygame.display.flip()
        clock.tick(120)
    if hero.sprite.alive  == 0:
        store()
done = game_loop()
while not done:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    currentTime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if keys[pygame.K_r]:
        done = game_loop()
    pygame.quit()
