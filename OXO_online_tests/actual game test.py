# actual game testing
import pygame
import pygame.font
from menuclass import menu
from random import randint #temporary for CPU fight
from time import *
pygame.init()

screen = pygame.display.set_mode((500, 500), 0)
white = (255, 255, 255)
grey = (100, 100, 100)

game = menu(screen)
game.createobj('images//battlefield.png', (400, 400), 50, 100)
# text displaying opponent name above the game board
game.createobj('images//ytb.png', (300, 300), 0, -75)
game.createobj('images//win1.png', (450, 450), 50, 50)
game.createobj('images//win2.png', (450, 450), 50, 50)

font = pygame.font.SysFont('Comic Sans MS', 35)
vs = font.render(('VS'), False, grey)
opname = font.render('victor', False, grey)
opx, opy = 300, 25

errorfont = font = pygame.font.SysFont('Comic Sans MS', 25)
errormsg = font.render('There has been a problem with the server', False, grey)

going = True
while going:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            going = False
            pygame.quit()
    if going:
        screen.fill(white)
        game.displayobj(0)
        game.displayobj(1)
##        screen.blit(vs, (opx, opy))
##        screen.blit(opname, (opx, opy + 40))

        screen.blit(errormsg, (5, 450))

        pygame.display.flip()
        pygame.display.update()




### creation of circle outliner
##highlight = pygame.image.load('images//highlight.png')
##highlight = pygame.transform.scale(highlight, (100, 100))
##oppacity = 60
##highlight.fill((255, 255, 255, oppacity), None, pygame.BLEND_RGBA_MULT) #used to change oppacity
##
##coordlist = [[]]*9
##imagelist = [None]*9
##piecelist = ['']*9
##
##
##def wincondition(symbol):
##    if (piecelist[0] == symbol and piecelist[1] == symbol and piecelist[2] == symbol) or \
##       (piecelist[3] == symbol and piecelist[4] == symbol and piecelist[5] == symbol) or \
##       (piecelist[6] == symbol and piecelist[7] == symbol and piecelist[8] == symbol) or \
##       (piecelist[0] == symbol and piecelist[3] == symbol and piecelist[6] == symbol) or \
##       (piecelist[1] == symbol and piecelist[4] == symbol and piecelist[7] == symbol) or \
##       (piecelist[2] == symbol and piecelist[5] == symbol and piecelist[8] == symbol) or \
##       (piecelist[0] == symbol and piecelist[4] == symbol and piecelist[8] == symbol) or \
##       (piecelist[2] == symbol and piecelist[4] == symbol and piecelist[6] == symbol):
##
##        return True
##    else:
##        return False
##    
##
##    
### the host will be x, other player will be o
##
##symbol = 'X'
##image = pygame.image.load('images//' + symbol + '.png')
##image = pygame.transform.scale(image, (100, 100))
##
##count = 0
##yourturn = True
##mouse = pygame.mouse.get_pos()
##endscreen = False
##going = True
##while going:
##    events = pygame.event.get()
##    for event in events:
##        if event.type == pygame.QUIT:
##            going = False
##            pygame.quit()
##        elif event.type == pygame.MOUSEBUTTONDOWN:
##            if 70 <= mouse[0] <= 170:
##                if 130 <= mouse[1] <= 230:
##                    if piecelist[0] == '':
##                        yourturn = False
##                        piecelist[0] = symbol
##                        imagelist[0] = image
##                        coordlist[0] = [70, 130]
##                elif 255 <= mouse[1] <= 355:
##                    if piecelist[1] == '':
##                        yourturn = False
##                        piecelist[1] = symbol
##                        imagelist[1] = image
##                        coordlist[1] = [70, 255]
##                elif 375 <= mouse[1] <= 475:
##                    if piecelist[2] == '':
##                        yourturn = False
##                        piecelist[2] = symbol
##                        imagelist[2] = image
##                        coordlist[2] = [70, 375]
##            elif 195 <= mouse[0] <= 295:
##                if 130 <= mouse[1] <= 230:
##                    if piecelist[3] == '':
##                        yourturn = False
##                        piecelist[3] = symbol
##                        imagelist[3] = image
##                        coordlist[3] = [195, 130]
##                elif 255 <= mouse[1] <= 355:
##                    if piecelist[4] == '':
##                        yourturn = False
##                        piecelist[4] = symbol
##                        imagelist[4] = image
##                        coordlist[4] = [195, 255]
##                elif 375 <= mouse[1] <= 475:
##                    if piecelist[5] == '':
##                        yourturn = False
##                        piecelist[5] = symbol
##                        imagelist[5] = image
##                        coordlist[5] = [195, 375]
##            elif 320 <= mouse[0] <= 420:
##                if 130 <= mouse[1] <= 230:
##                    if piecelist[6] == '':
##                        yourturn = False
##                        piecelist[6] = symbol
##                        imagelist[6] = image
##                        coordlist[6] = [320, 130]
##                elif 255 <= mouse[1] <= 355:
##                    if piecelist[7] == '':
##                        yourturn = False
##                        piecelist[7] = symbol
##                        imagelist[7] = image
##                        coordlist[7] = [320, 255]
##                elif 375 <= mouse[1] <= 475:
##                    if piecelist[8] == '':
##                        yourturn = False
##                        piecelist[8] = symbol
##                        imagelist[8] = image
##                        coordlist[8] = [320, 375]
##    for piece in piecelist:
##        if piece != '':
##            count += 1
##    if count == 9:
##        if wincondition('X') == True:
##            print('you won')
##            going = False
##            endscreen = True
##        elif wincondition('O') == True:
##            print('you lost')
##            going = False
##            endscreen = True
##
##        elif wincondition('X') == False and wincondition('O') == False:
##            print('tie')
##            going = False
##            endscreen = True
##    count = 0
##    if yourturn == False and endscreen == False:
##        symbol = 'O'
##        image = pygame.image.load('images//' + symbol + '.png')
##        image = pygame.transform.scale(image, (100, 100))
##
##        cpu = randint(0, 8)
##        while piecelist[cpu] != '':
##            cpu = randint(0, 8)
##            
##        match cpu:
##            case 0:
##                templist = [70, 130]
##            case 1:
##                templist = [70, 255]
##            case 2:
##                templist = [70, 375]
##            case 3:
##                templist = [195, 130]
##            case 4:
##                templist = [195, 255]
##            case 5:
##                templist = [195, 375]
##            case 6:
##                templist = [320, 130]
##            case 7:
##                templist = [320, 255]
##            case 8:
##                templist = [320, 375]
##
##        
##        piecelist[cpu] = symbol
##        imagelist[cpu] = image
##        coordlist[cpu] = templist
##        yourturn = True
##        symbol = 'X'
##        image = pygame.image.load('images//' + symbol + '.png')
##        image = pygame.transform.scale(image, (100, 100))
##    if going:
##        if wincondition('X') == True:
##            print('you won')
##            going = False
##            endscreen = True
##        elif wincondition('O') == True:
##            print('you lost')
##            going = False
##            endscreen = True
##        mouse = pygame.mouse.get_pos()
##        #print(str(mouse[0]) + ', ' + str(mouse[1]))
##        screen.fill(white)
##        game.displayobj(0)
##        #screen.blit(cross, (70, 130))
##        if 70 <= mouse[0] <= 170:
##            if 130 <= mouse[1] <= 230:
##                screen.blit(highlight, (70, 130))
##            elif 255 <= mouse[1] <= 355:
##                screen.blit(highlight, (70, 255))
##            elif 375 <= mouse[1] <= 475:
##                screen.blit(highlight, (70, 375))
##        elif 195 <= mouse[0] <= 295:
##            if 130 <= mouse[1] <= 230:
##                screen.blit(highlight, (195, 130))
##            elif 255 <= mouse[1] <= 355:
##                screen.blit(highlight, (195, 255))
##            elif 375 <= mouse[1] <= 475:
##                screen.blit(highlight, (195, 375))
##        elif 320 <= mouse[0] <= 420:
##            if 130 <= mouse[1] <= 230:
##                screen.blit(highlight, (320, 130))
##            elif 255 <= mouse[1] <= 355:
##                screen.blit(highlight, (320, 255))
##            elif 375 <= mouse[1] <= 475:
##                screen.blit(highlight, (320, 375))
##
##        
##
##        for i in range(0, 9):
##            if piecelist[i] != '':
##                screen.blit(imagelist[i], (coordlist[i][0], coordlist[i][1]))
##        
##        #screen.blit(highlight, (mouse[0], mouse[1]))
##        pygame.display.flip()
##        pygame.display.update()
##
##
##print('done')
##mouse = pygame.mouse.get_pos()
##while endscreen:
##    events = pygame.event.get()
##    for event in events:
##        if event.type == pygame.QUIT:
##            going = False
##            pygame.display.quit()
##            pygame.quit()
##    if endscreen:
##        screen.fill(white)
##        game.displayobj(0)
##        for i in range(0, 9):
##            if piecelist[i] != '':
##                screen.blit(imagelist[i], (coordlist[i][0], coordlist[i][1]))
##        pygame.display.flip()
##        pygame.display.update()
