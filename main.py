import pygame
from sys import exit
pygame.init()
wdith = 800
hight = 400
sWdith = 10
sHight = 10
secreen = pygame.display.set_mode((wdith,hight))
fontA = pygame.font.Font('font/Pixeltype.ttf',50)
pygame.display.set_caption("Corredor")
clock = pygame.time.Clock()
skyImg = pygame.image.load('graphics/Sky.png').convert_alpha()
groundImg = pygame.image.load('graphics/ground.png').convert_alpha()
scoreText = fontA.render('Mi Juego', False , (64,64,64))
scoreTextrec = scoreText.get_rect(center = (400,50))
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
caracolSurfaceIzquierda1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
caracolSurfaceIzquierda1Rect = caracolSurfaceIzquierda1.get_rect(midbottom = (600,300))
caracolSurfaceIzquierda2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
flag = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('funciona')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print('mouse down')
    #dibuamos los elementos
    #updateamos todo
    secreen.blit(skyImg,(0,0))
    secreen.blit(groundImg, (0, 300))
    pygame.draw.rect(secreen,'#c0e8ec',scoreTextrec)
    pygame.draw.rect(secreen, '#c0e8ec', scoreTextrec, 10)

    secreen.blit(scoreText, scoreTextrec)
    secreen.blit(caracolSurfaceIzquierda1, caracolSurfaceIzquierda1Rect)
    caracolSurfaceIzquierda1Rect.right -= 4
    if caracolSurfaceIzquierda1Rect.right < -100: caracolSurfaceIzquierda1Rect.right = 800
    secreen.blit(player_surf,player_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')
    #mouse_pos = pygame.mouse.get_pos()
    #se fija si el mouse esta sobre el rectangulo
    #if player_rect.collidepoint(mouse_pos):
        #muestra los botones q se tocan del mouse
        #print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)