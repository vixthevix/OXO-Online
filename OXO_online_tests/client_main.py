# oxo main client

import os
import pygame
import pygame.font
import socket
import threading
import select
from menuclass import menu
from time import *
from random import randint


##oripath = str(os.path.abspath('client_main.py'))
##print(oripath) #C:\Users\GP\OneDrive\Documents\Victor\project_personnel\OXO_online\client_main.py
##
##curcar = oripath[len(oripath) - 1]
##pos = 0
##while curcar != '\\':
##    pos += 1
##    curcar = oripath[len(oripath) - 1 - pos]
##
##
##
##oripath = oripath[0:len(oripath) - pos]
##print(oripath)
    



PORT = 5050
SERVER = '' # current ip address, may change
#SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 256
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = True
try:
    client.connect((SERVER, PORT))
    print('connected')
except:
    connected = False
    print('not connected')

def send(msg):
    message = msg.encode(FORMAT) 
    msg_length = len(message) 
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) 
    client.send(send_length)
    client.send(message)

def recieve():
    if not (client.recv(2048).decode(FORMAT)):
        print('\n')
        print(client.recv(2048).decode(FORMAT))



pygame.init()

screen = pygame.display.set_mode((500, 500), 0)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

username = ''
filefound = True

try:
    namefile = open('files\\namefile.txt', 'r')
except:
    namefile = open('files\\namefile.txt', 'w')
    filefound = False



with open('files\\namefile.txt', 'r') as f:
    username = f.read()
    if len(username) == 0:
        filefound = False
        print('nothing found')

def username_menu(errorstate):
    # include a list of all non allowed characters
    banned = ['\\', '@', "'", '"']
    retry = errorstate
    phrase = []
    name = ''
    userstart = menu(screen)
    userstart.createobj('images//usernamequest.png', (250, 250), 125, 50)
    userstart.createobj('images//usernameinsert.png', (10000, 300), -150, 150)
    going = True
    mouse = pygame.mouse.get_pos()
    font = pygame.font.SysFont('Comic Sans MS', 25)
    while going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                going = False
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    #phrase += 'a'
                    phrase.append('a')
                elif event.key == pygame.K_b:
                    #phrase += 'b'
                    phrase.append('b')
                elif event.key == pygame.K_c:
                    #phrase += 'c'
                    phrase.append('c')
                elif event.key == pygame.K_d:
                    #phrase += 'd'
                    phrase.append('d')
                elif event.key == pygame.K_e:
                    #phrase += 'e'
                    phrase.append('e')
                elif event.key == pygame.K_f:
                    #phrase += 'f'
                    phrase.append('f')
                elif event.key == pygame.K_g:
                    #phrase += 'g'
                    phrase.append('g')
                elif event.key == pygame.K_h:
                    #phrase += 'h'
                    phrase.append('h')
                elif event.key == pygame.K_i:
                    #phrase += 'i'
                    phrase.append('i')
                elif event.key == pygame.K_j:
                    #phrase += 'j'
                    phrase.append('j')
                elif event.key == pygame.K_k:
                    #phrase += 'k'
                    phrase.append('k')
                elif event.key == pygame.K_l:
                    #phrase += 'l'
                    phrase.append('l')
                elif event.key == pygame.K_m:
                    #phrase += 'm'
                    phrase.append('m')
                elif event.key == pygame.K_n:
                    #phrase += 'n'
                    phrase.append('n')
                elif event.key == pygame.K_o:
                    #phrase += 'o'
                    phrase.append('o')
                elif event.key == pygame.K_p:
                    #phrase += 'p'
                    phrase.append('p')
                elif event.key == pygame.K_q:
                    #phrase += 'q'
                    phrase.append('q')
                elif event.key == pygame.K_r:
                    #phrase += 'r'
                    phrase.append('r')
                elif event.key == pygame.K_s:
                    #phrase += 's'
                    phrase.append('s')
                elif event.key == pygame.K_t:
                    #phrase += 't'
                    phrase.append('t')
                elif event.key == pygame.K_u:
                    #phrase += 'u'
                    phrase.append('u')
                elif event.key == pygame.K_v:
                    #phrase += 'v'
                    phrase.append('v')
                elif event.key == pygame.K_w:
                    #phrase += 'w'
                    phrase.append('w')
                elif event.key == pygame.K_x:
                    #phrase += 'x'
                    phrase.append('x')
                elif event.key == pygame.K_y:
                    #phrase += 'y'
                    phrase.append('y')
                elif event.key == pygame.K_z:
                    #phrase += 'z'
                    phrase.append('z')
                elif event.key == pygame.K_SPACE:
                    #phrase += ' '
                    phrase.append(' ')
                elif event.key == pygame.K_BACKSPACE:
                    if len(phrase) != 0:
                        phrase.pop(len(phrase) - 1)
                elif event.key == pygame.K_RETURN:
                    retry = False
                    name = ''
                    for i in range(0, len(phrase)):
                        name += phrase[i]
                    return name
                    going = False
                    
        if going:
            for i in range(0, len(phrase)):
                name += phrase[i]
            displayname = font.render(name, False, white)
            screen.fill(white)
            userstart.displayobj(0)
            userstart.displayobj(1)
            if retry:
                errorname = font.render('Error, username is invalid', False, red)
                screen.blit(errorname, (75, 400)) 
            screen.blit(displayname, (0, 250))
            name = ''
            pygame.display.flip()
            pygame.display.update()

def checkforusername(name):
    # this is used for the server to check whether the username
    # of this account is in the database
    # only runs on account creation
    # must create a countermeasure against new account creation through file editing
    send('usernamecheck')
    ready,_,_ = select.select([client], [], [], 0.01)
    while not ready:
        ready,_,_ = select.select([client], [], [], 0.01)
    if ready:
        if client.recv(2048).decode(FORMAT) == 'usernamecheck recieved':
            send(name)
    else:
        pass
    
    ready,_,_ = select.select([client], [], [], 0.01)
    while not ready:
        ready,_,_ = select.select([client], [], [], 0.01)
    if ready:
        if client.recv(2048).decode(FORMAT) == 'accept': # if the username exists in the database, does nothing
            return True
        else: # if the username doesnt exist, erase all existing scores from the current ones and create a new account
            return False
    else:
        pass
    

  
def activate_account(name):
    send('activate')
    ready,_,_ = select.select([client], [], [], 0.01)
    while not ready:
        ready,_,_ = select.select([client], [], [], 0.01)
    if ready:
        if client.recv(2048).decode(FORMAT) == 'activated':
            send(name)
    else:
        pass




try:
    scorefile = open('files\\scorefile.txt', 'r')
except:
    scorefile = open('files\\scorefile.txt', 'w')

# first number is num of wins, second number is num of losses, third number is num of draws
scorecap = 999

with open('files\\scorefile.txt', 'r') as f:
    scores = f.read()
    print(scores)
    if len(scores) == 0:
        emptyscore = True
        print('emptyscore')
    else:
        emptyscore = False

if emptyscore:
    with open('files\\scorefile.txt', 'w') as f:
        f.write('0')
        f.write('\n')
        f.write('0')
        f.write('\n')            
        f.write('0')
        f.write('\n')
        wins = 0
        losses = 0
        draws = 0
else:
    with open('files\\scorefile.txt', 'r') as f:
        scores = f.read()
        count = 0
        curscore = ''
        wins = 0
        losses = 0
        draws = 0
        scoretype = 0
        while count < len(scores):
            while scores[count] != '\n':
                curscore += scores[count]
                count += 1

            count += 1
            match scoretype:
                case 0:
                    wins = int(curscore)
                case 1:
                    losses = int(curscore)
                case 2:
                    draws = int(curscore)

            curscore = ''
            scoretype += 1

if wins > scorecap or draws > scorecap or losses > scorecap:
    wins = 0
    draws = 0
    losses = 0

def updatescores(w, L, d):
    open('files\\scorefile.txt', 'w').close()
    with open('files\\scorefile.txt', 'w') as f:
        f.write(str(w))
        f.write('\n')
        f.write(str(L))
        f.write('\n')            
        f.write(str(d))
        f.write('\n')

def startmenu(w, L, d, errorfound):
    #create objects for score display
    start = menu(screen)
    start.createobj('images//exit1.png', (175, 175), 50, 350)
    start.createobj('images//public1.png', (175, 175), 50, 275)
    start.createobj('images//private1.png', (175, 175), 50, 200)
    start.createobj('images//logo.png', (275, 250), 125, 50)

    start.createobj('images//exit2.png', (175, 175), 50, 350)
    start.createobj('images//public2.png', (175, 175), 50, 275)
    start.createobj('images//private2.png', (175, 175), 50, 200)

    start.createobj('images//scoreboard.png', (275, 250), 275, 245)
    red = (255, 0, 0) 

    font = pygame.font.SysFont('Comic Sans MS', 25)
    wins = font.render(str(w), False, red)
    losses = font.render(str(L), False, red)
    draws = font.render(str(d), False, red)

    errorstate = errorfound

    menubuttons = [False, False, False]
    going = True
    mouse = pygame.mouse.get_pos()
    while going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                going = False
                pygame.display.quit()
                pygame.quit()
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 256 <= mouse[1] <= 300:
                    return 'private'
                    
                elif 60 <= mouse[0] <= 215 and 331 <= mouse[1] <= 375:
                    return 'public'
                    
                elif 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                    send('disconnect')
                    return 'exit'
                

        if going:
            mouse = pygame.mouse.get_pos()
            screen.fill(white)


            if 60 <= mouse[0] <= 215 and 256 <= mouse[1] <= 300:
                start.displayobj(6)
            else:
                start.displayobj(2)
                
            if 60 <= mouse[0] <= 215 and 331 <= mouse[1] <= 375:
                start.displayobj(5)
            else:
                start.displayobj(1)
                
            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                start.displayobj(4)
            else:
                start.displayobj(0)

            start.displayobj(3)
            start.displayobj(7)
            screen.blit(wins, (340, 315))
            screen.blit(losses, (340, 365))
            screen.blit(draws, (340, 420))

            if errorstate:
                errormsg = font.render('There has been a problem with the server', False, red)
                screen.blit(errormsg, (5, 450))
            pygame.display.flip()
            pygame.display.update()

def publicgame():
    try:
        send('looking for public')
    except:
        return 'server error'
    pmenu = menu(screen)
    pmenu.createobj('images//publicwait.png', (400, 400), 50, 50)
    pmenu.createobj('images//back1.png', (175, 175), 50, 350)
    pmenu.createobj('images//back2.png', (175, 175), 50, 350)

    
    
    
    newtime = time()
    currentime = time()
    timelimit = 180 #3 minutes

    ttlnew = 0
    ttlcur = 0

    gameready = False
    opname = ''
    going = True
    mouse = pygame.mouse.get_pos()
    while going: #and newtime - currentime < timelimit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                going = False
                send('disconnect')
                pygame.display.quit()
                pygame.quit()
                return ['exit']
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                    going = False
                    send('quit looking')
                    return ['stop looking']
        if going: #and newtime - currentime < timelimit:
            #newtime = time()
            mouse = pygame.mouse.get_pos()
            screen.fill(white)
            pmenu.displayobj(0)

            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                pmenu.displayobj(2)
            else:
                pmenu.displayobj(1)

            pygame.display.flip()
            pygame.display.update()

##            ttl = randint(10, 100)
##            ttlnew = time()
##            ttlcur = time()
##            while ttlnew - ttlcur < ttl:
##                ttlnew = time()
##                newtime = time()
##            send('finished waiting')

            ready,_,_ = select.select([client], [], [], 0.01)
            if ready:
                msg = client.recv(2048).decode(FORMAT)
                print(msg[1:13])
                if msg[1:13] == 'player found':
                    opname = msg[13:len(msg)]
                    condition = str(msg[0])
                    print(condition)
                    going = False
                    gameready = True
                elif msg == 'timeout':
                    going = False
            else:
                pass
            
            pygame.display.flip()
            pygame.display.update()
##            if ready:
##                msg = client.recv(2048).decode(FORMAT)
##                if msg[0:21] == 'sending public invite':
##                    print('i am player 1')
##                    opname = msg[21:len(msg)]
##                    send('public invite recieved'+opname)
##                    going = False
##                    gameready = True
##                elif msg[0:26] == 'public invite recieved too':
##                    opname = msg[26:len(msg)]
##                    print('i am player 2')
##                    send('timeout')
##                    going = False
##                    gameready = True
##                elif msg == 'timeout':
##                    going = False
##            else:
##                pass

    if gameready:
        print('game is ready')
        print(opname)
        return [opname, condition]
    else:
        print('timeout')
        return ['timeout']



def privategame():
    priv = menu(screen)
    priv.createobj('images//join1.png', (175, 175), 50, 200)
    priv.createobj('images//host1.png', (175, 175), 50, 275)
    priv.createobj('images//back1.png', (175, 175), 50, 350)
    priv.createobj('images//join2.png', (175, 175), 50, 200)
    priv.createobj('images//host2.png', (175, 175), 50, 275)
    priv.createobj('images//back2.png', (175, 175), 50, 350)
    
    priv.createobj('images//logo.png', (275, 250), 125, 50)

    
    going = True
    mouse = pygame.mouse.get_pos()
    while going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                going = False
                pygame.display.quit()
                pygame.quit()
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 256 <= mouse[1] <= 300:
                    going = False
                    return 'join'
                    
                elif 60 <= mouse[0] <= 215 and 331 <= mouse[1] <= 375:
                    going = False
                    return 'host'
                    
                elif 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                    return 'back'
                    going = False
        if going:
            mouse = pygame.mouse.get_pos()
            screen.fill(white)

            if 60 <= mouse[0] <= 215 and 256 <= mouse[1] <= 300:
                priv.displayobj(3)
            else:
                priv.displayobj(0)
                
            if 60 <= mouse[0] <= 215 and 331 <= mouse[1] <= 375:
                priv.displayobj(4)
            else:
                priv.displayobj(1)
                
            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                priv.displayobj(5)
            else:
                priv.displayobj(2)
            
            priv.displayobj(6)
            pygame.display.flip()
            pygame.display.update()


##def sendusername(name):
##    # this is used for the server to check whether the username
##    # of this account is in the database
##    # must create a countermeasure against new account creation through file editing
##    send('usernamecheck')
##    ready,_,_ = select.select([client], [], [], 0.01)
##    while not ready:
##        ready,_,_ = select.select([client], [], [], 0.01)
##    if ready:
##        send(name)
##    else:
##        pass
##    
##    ready,_,_ = select.select([client], [], [], 0.01)
##    while not ready:
##        ready,_,_ = select.select([client], [], [], 0.01)
##    if ready:
##        if client.recv(2048).decode(FORMAT) == 'accept': # if the username exists in the database, does nothing
##            return True
##        else: # if the username doesnt exist, erase all existing scores from the current ones and create a new account
##            return False
##    else:
##        pass
            
def hostgame():
    hmenu = menu(screen)
    hmenu.createobj('images//joinwait.png', (400, 400), 50, 50)
    hmenu.createobj('images//back1.png', (175, 175), 50, 350)
    hmenu.createobj('images//back2.png', (175, 175), 50, 350)

    try:
        send('hosting')
    except:
        return 'server error'
    
    going = True
    mouse = pygame.mouse.get_pos()
    while going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                going = False
                pygame.display.quit()
                pygame.quit()
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                    send('stopped hosting')
                    return 'stopped hosting'
                    going = False
        if going:
            mouse = pygame.mouse.get_pos()
            screen.fill(white)
            hmenu.displayobj(0)
            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                hmenu.displayobj(2)
            else:
                hmenu.displayobj(1)

            initime = time()
            newtime = time()
            ready,_,_ = select.select([client], [], [], 0.01)
##            while not ready and newtime - initime < 0.25:
##                newtime = time()
##                ready,_,_ = select.select([client], [], [], 0.01)
            if ready:
                msg = client.recv(2048).decode(FORMAT)
                if msg[0:12] == 'player found':
                    going = False
                    send('stopped hosting')
                    return msg[13:len(msg)]
            else:
                pass



            pygame.display.flip()
            pygame.display.update()


def joingame():

    # create the menu for getting the host name
    # then edit it to wait for player to join host
    phrase = []
    name = ''
    font = pygame.font.SysFont('Comic Sans MS', 25)
    
    joinmenu = menu(screen)
    joinmenu.createobj('images//hostnamerequest.png', (250, 250), 125, 50)
    joinmenu.createobj('images//usernameinsert.png', (10000, 300), -150, 150)
    joinmenu.createobj('images//back1.png', (175, 175), 50, 350)
    joinmenu.createobj('images//back2.png', (175, 175), 50, 350)
    
    initgoing = True
    secondgoing = True
    mouse = pygame.mouse.get_pos()
    while initgoing:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                initgoing = False
                pygame.display.quit()
                pygame.quit()
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                    initgoing = False
                    secondgoing = False
                    return 'stop looking'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    #phrase += 'a'
                    phrase.append('a')
                elif event.key == pygame.K_b:
                    #phrase += 'b'
                    phrase.append('b')
                elif event.key == pygame.K_c:
                    #phrase += 'c'
                    phrase.append('c')
                elif event.key == pygame.K_d:
                    #phrase += 'd'
                    phrase.append('d')
                elif event.key == pygame.K_e:
                    #phrase += 'e'
                    phrase.append('e')
                elif event.key == pygame.K_f:
                    #phrase += 'f'
                    phrase.append('f')
                elif event.key == pygame.K_g:
                    #phrase += 'g'
                    phrase.append('g')
                elif event.key == pygame.K_h:
                    #phrase += 'h'
                    phrase.append('h')
                elif event.key == pygame.K_i:
                    #phrase += 'i'
                    phrase.append('i')
                elif event.key == pygame.K_j:
                    #phrase += 'j'
                    phrase.append('j')
                elif event.key == pygame.K_k:
                    #phrase += 'k'
                    phrase.append('k')
                elif event.key == pygame.K_l:
                    #phrase += 'l'
                    phrase.append('l')
                elif event.key == pygame.K_m:
                    #phrase += 'm'
                    phrase.append('m')
                elif event.key == pygame.K_n:
                    #phrase += 'n'
                    phrase.append('n')
                elif event.key == pygame.K_o:
                    #phrase += 'o'
                    phrase.append('o')
                elif event.key == pygame.K_p:
                    #phrase += 'p'
                    phrase.append('p')
                elif event.key == pygame.K_q:
                    #phrase += 'q'
                    phrase.append('q')
                elif event.key == pygame.K_r:
                    #phrase += 'r'
                    phrase.append('r')
                elif event.key == pygame.K_s:
                    #phrase += 's'
                    phrase.append('s')
                elif event.key == pygame.K_t:
                    #phrase += 't'
                    phrase.append('t')
                elif event.key == pygame.K_u:
                    #phrase += 'u'
                    phrase.append('u')
                elif event.key == pygame.K_v:
                    #phrase += 'v'
                    phrase.append('v')
                elif event.key == pygame.K_w:
                    #phrase += 'w'
                    phrase.append('w')
                elif event.key == pygame.K_x:
                    #phrase += 'x'
                    phrase.append('x')
                elif event.key == pygame.K_y:
                    #phrase += 'y'
                    phrase.append('y')
                elif event.key == pygame.K_z:
                    #phrase += 'z'
                    phrase.append('z')
                elif event.key == pygame.K_SPACE:
                    #phrase += ' '
                    phrase.append(' ')
                elif event.key == pygame.K_BACKSPACE:
                    if len(phrase) != 0:
                        phrase.pop(len(phrase) - 1)
                elif event.key == pygame.K_RETURN:
                    name = ''
                    for i in range(0, len(phrase)):
                        name += phrase[i]
                    initgoing = False
        if initgoing:
            for i in range(0, len(phrase)):
                name += phrase[i]
            displayname = font.render(name, False, white)
            name = ''
            mouse = pygame.mouse.get_pos()
            screen.fill(white)
            joinmenu.displayobj(0)
            joinmenu.displayobj(1)
            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                joinmenu.displayobj(3)
            else:
                joinmenu.displayobj(2)
            screen.blit(displayname, (0, 250))

            pygame.display.flip()
            pygame.display.update()

##    ready,_,_ = select.select([client], [], [], 0.01)
##    while not ready:
##        ready,_,_ = select.select([client], [], [], 0.01)
##    if ready:
##        if client.recv(2048).decode(FORMAT) == 'joining recieved':
##            pass
##    else:
##        return 'server error'

    if secondgoing:
        try:
            send('joining')
        except:
            return 'server error'
        ready,_,_ = select.select([client], [], [], 0.01)
        while not ready:
            ready,_,_ = select.select([client], [], [], 0.01)
        if ready:
            if client.recv(2048).decode(FORMAT) == 'joining recieved':
                pass
        else:
            return 'server error'
        send(name)
    # set up a timer for 3 minutes before resetting to title screen, out of time for hosting

    waiting = menu(screen)
    waiting.createobj('images//hostwait.png', (400, 400), 50, 50)
    waiting.createobj('images//back1.png', (175, 175), 50, 350)
    waiting.createobj('images//back2.png', (175, 175), 50, 350)

    
    nameinfo = font.render(('Looking for: ' + name), False, black)

    gameready = False
    initime = time()
    newtime = time()
    mouse = pygame.mouse.get_pos()
    while secondgoing and newtime - initime < 180:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                secondgoing = False
                pygame.display.quit()
                pygame.quit()
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                        secondgoing = False
                        return 'stop looking'
        if secondgoing and newtime - initime < 180:
            mouse = pygame.mouse.get_pos()
            newtime = time()
            screen.fill(white)
            waiting.displayobj(0)
            if 60 <= mouse[0] <= 215 and 406 <= mouse[1] <= 450:
                waiting.displayobj(2)
            else:
                waiting.displayobj(1)

            screen.blit(nameinfo, (5, 5))
            pygame.display.flip()
            pygame.display.update()
            ready,_,_ = select.select([client], [], [], 0.01)
            if ready:
                if client.recv(2048).decode(FORMAT) == (name + ' is hosting'):
                    send('player joining' + username)
                    secondgoing = False
                    gameready = True
            else:
                pass

    
    if not gameready:
        return 'server error'
    else:
        return name

def wincondition(symbol, piecelist):
    if (piecelist[0] == symbol and piecelist[1] == symbol and piecelist[2] == symbol) or \
       (piecelist[3] == symbol and piecelist[4] == symbol and piecelist[5] == symbol) or \
       (piecelist[6] == symbol and piecelist[7] == symbol and piecelist[8] == symbol) or \
       (piecelist[0] == symbol and piecelist[3] == symbol and piecelist[6] == symbol) or \
       (piecelist[1] == symbol and piecelist[4] == symbol and piecelist[7] == symbol) or \
       (piecelist[2] == symbol and piecelist[5] == symbol and piecelist[8] == symbol) or \
       (piecelist[0] == symbol and piecelist[4] == symbol and piecelist[8] == symbol) or \
       (piecelist[2] == symbol and piecelist[4] == symbol and piecelist[6] == symbol):

        return True
    else:
        return False
#opponent username, a number denoting either:
#0) you are a private host 1) you are a private joiner 2) you are in a public game
# to make life easier, private hosts go first
# in a public game, idk;

def playgame(opponent, yourtype):
    newtime = time()
    currentime = time()
    while newtime - currentime < 5:
        newtime = time()
    send('creating game')
    ready = select.select([client], [], [], 0.01)
    while not ready:
        ready = select.select([client], [], [], 0.01)
    if client.recv(2048).decode(FORMAT) == 'game created':
        print('game created')
        send(opponent)
    else:
        return 'server error'

    ready = select.select([client], [], [], 0.01)
    while not ready:
        ready = select.select([client], [], [], 0.01)
    if client.recv(2048).decode(FORMAT) == 'opponent recieved':
        print('opponent recieved')
        #pass
    else:
        return 'server error'

    game = menu(screen)
    game.createobj('images//battlefield.png', (400, 400), 50, 100)
    if yourtype == 0:
        #send('going') #going will indicate your making a move
        going = True
        waiting = False
        symbol = 'X'
        opsymbol = 'O'
        opcolour = (255, 0, 0)
        game.createobj('images//tbr.png', (300, 300), 0, -75)
        game.createobj('images//ytb.png', (300, 300), 0, -75)
    elif yourtype == 1:
        #send('waiting')# #waiting will indicate your waiting for your opponent
        going = False
        waiting = True
        symbol = 'O'
        opsymbol = 'X'
        opcolour = (0, 0, 255)
        game.createobj('images//tbb.png', (300, 300), 0, -75)
        game.createobj('images//ytr.png', (300, 300), 0, -75)
##    else:
##        yournum = -1
##        opnum = -1
##        while yournum == opnum:
##            yournum = randint(0, 100)
##            send('yournum'+str(yournum))
##
##            ready = select.select([client], [], [], 0.01)
##            while not ready:
##                ready = select.select([client], [], [], 0.01)
##            if ready:
##                msg = client.recv(2048).decode(FORMAT)
##                if msg[0:6] == 'opnum':
##                    print('opnum')
##                    opnum = int(msg[6:len(msg)])
##                else:
##                    return 'server error'
##
##        if yournum > opnum:
##            going = True
##            waiting = False
##            symbol = 'X'
##            opsymbol = 'O'
##        else:
##            going = False
##            waiting = True
##            symbol = 'O'
##            opsymbol = 'X'

    greatergoing = True
    gameended = False

    image = pygame.image.load('images//' + symbol + '.png')
    image = pygame.transform.scale(image, (100, 100))

    # text displaying opponent name above the game board
    font = pygame.font.SysFont('Comic Sans MS', 35)
    vs = font.render(('VS'), False, opcolour)
    opname = font.render(opponent, False, opcolour)
    opx, opy = 300, 25

    # creation of circle outliner
    highlight = pygame.image.load('images//highlight.png')
    highlight = pygame.transform.scale(highlight, (100, 100))
    oppacity = 60
    highlight.fill((255, 255, 255, oppacity), None, pygame.BLEND_RGBA_MULT) #used to change oppacity

    coordlist = [[]]*9
    imagelist = [None]*9
    piecelist = ['']*9


    count = 0
    message = ''
    condition = ''
    movemade = -1
    
    mouse = pygame.mouse.get_pos()
    while greatergoing:
        for piece in piecelist:
            if piece != '':
                count += 1
        if count == 9:
            if wincondition('X', piecelist) == False and wincondition('O', piecelist) == False:
                condition = 'tie'
                greatergoing = False
                going = False
                gameended = True
        if wincondition(symbol, piecelist) == True:
            condition = 'win'
            greatergoing = False
            going = False
            gameended = True
        elif wincondition(opsymbol, piecelist) == True:
            condition = 'loss'
            greatergoing = False
            going = False
            gameended = True
        count = 0
        image = pygame.image.load('images//' + symbol + '.png')
        image = pygame.transform.scale(image, (100, 100))
        while going:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    send('public game disconnect')
                    send('disconnect')
                    going = False
                    greatergoing = False
                    pygame.quit()
                    return 'exit'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 70 <= mouse[0] <= 170:
                        if 130 <= mouse[1] <= 230:
                            if piecelist[0] == '':
                                going = False
                                waiting = True
                                piecelist[0] = symbol
                                imagelist[0] = image
                                coordlist[0] = [70, 130]
                                message = '0'
                        elif 255 <= mouse[1] <= 355:
                            if piecelist[1] == '':
                                going = False
                                waiting = True
                                piecelist[1] = symbol
                                imagelist[1] = image
                                coordlist[1] = [70, 255]
                                message = '1'
                        elif 375 <= mouse[1] <= 475:
                            if piecelist[2] == '':
                                going = False
                                waiting = True
                                piecelist[2] = symbol
                                imagelist[2] = image
                                coordlist[2] = [70, 375]
                                message = '2'
                    elif 195 <= mouse[0] <= 295:
                        if 130 <= mouse[1] <= 230:
                            if piecelist[3] == '':
                                going = False
                                waiting = True
                                piecelist[3] = symbol
                                imagelist[3] = image
                                coordlist[3] = [195, 130]
                                message = '3'
                        elif 255 <= mouse[1] <= 355:
                            if piecelist[4] == '':
                                going = False
                                waiting = True
                                piecelist[4] = symbol
                                imagelist[4] = image
                                coordlist[4] = [195, 255]
                                message = '4'
                        elif 375 <= mouse[1] <= 475:
                            if piecelist[5] == '':
                                going = False
                                waiting = True
                                piecelist[5] = symbol
                                imagelist[5] = image
                                coordlist[5] = [195, 375]
                                message = '5'
                    elif 320 <= mouse[0] <= 420:
                        if 130 <= mouse[1] <= 230:
                            if piecelist[6] == '':
                                going = False
                                waiting = True
                                piecelist[6] = symbol
                                imagelist[6] = image
                                coordlist[6] = [320, 130]
                                message = '6'
                        elif 255 <= mouse[1] <= 355:
                            if piecelist[7] == '':
                                going = False
                                waiting = True
                                piecelist[7] = symbol
                                imagelist[7] = image
                                coordlist[7] = [320, 255]
                                message = '7'
                        elif 375 <= mouse[1] <= 475:
                            if piecelist[8] == '':
                                going = False
                                waiting = True
                                piecelist[8] = symbol
                                imagelist[8] = image
                                coordlist[8] = [320, 375]
                                message = '8'
            for piece in piecelist:
                if piece != '':
                    count += 1
            if count == 9:
                if wincondition('X', piecelist) == False and wincondition('O', piecelist) == False:
                    condition = 'tie'
                    greatergoing = False
                    going = False
                    gameended = True
            if wincondition(symbol, piecelist) == True:
                condition = 'win'
                greatergoing = False
                going = False
                gameended = True
            elif wincondition(opsymbol, piecelist) == True:
                condition = 'loss'
                greatergoing = False
                going = False
                gameended = True
            count = 0
            if going:
##                if wincondition('X') == True:
##                    print('you won')
##                    going = False
##                    endscreen = True
##                elif wincondition('O') == True:
##                    print('you lost')
##                    going = False
##                    endscreen = True
                mouse = pygame.mouse.get_pos()
                #print(str(mouse[0]) + ', ' + str(mouse[1]))
                screen.fill(white)
                game.displayobj(0)
                game.displayobj(2)
                screen.blit(vs, (opx, opy))
                screen.blit(opname, (opx, opy + 40))
                #screen.blit(cross, (70, 130))
                if 70 <= mouse[0] <= 170:
                    if 130 <= mouse[1] <= 230:
                        screen.blit(highlight, (70, 130))
                    elif 255 <= mouse[1] <= 355:
                        screen.blit(highlight, (70, 255))
                    elif 375 <= mouse[1] <= 475:
                        screen.blit(highlight, (70, 375))
                elif 195 <= mouse[0] <= 295:
                    if 130 <= mouse[1] <= 230:
                        screen.blit(highlight, (195, 130))
                    elif 255 <= mouse[1] <= 355:
                        screen.blit(highlight, (195, 255))
                    elif 375 <= mouse[1] <= 475:
                        screen.blit(highlight, (195, 375))
                elif 320 <= mouse[0] <= 420:
                    if 130 <= mouse[1] <= 230:
                        screen.blit(highlight, (320, 130))
                    elif 255 <= mouse[1] <= 355:
                        screen.blit(highlight, (320, 255))
                    elif 375 <= mouse[1] <= 475:
                        screen.blit(highlight, (320, 375))

                

                for i in range(0, 9):
                    if piecelist[i] != '':
                        screen.blit(imagelist[i], (coordlist[i][0], coordlist[i][1]))

                ready,_,_ = select.select([client], [], [], 0.01)
                if ready:
                    msg = client.recv(2048).decode(FORMAT)
                    if msg == 'opponent has disconnected':
                        print('opponent has disconnected')
                        waiting = False
                        going = False
                        greatergoing = False
                        return 'server error'
                
                #screen.blit(highlight, (mouse[0], mouse[1]))
                pygame.display.flip()
                pygame.display.update()
        
        if message != '':
            send('move made' + message)

        while waiting:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    send('public game disconnect')
                    send('disconnect')
                    greatergoing = False
                    waiting = False
                    pygame.display.quit()
                    pygame.quit()
                    return 'exit'
            for piece in piecelist:
                if piece != '':
                    count += 1
            if count == 9:
                if wincondition('X', piecelist) == False and wincondition('O', piecelist) == False:
                    condition = 'tie'
                    greatergoing = False
                    going = False
                    gameended = True
            if wincondition(symbol, piecelist) == True:
                condition = 'win'
                greatergoing = False
                going = False
                gameended = True
            elif wincondition(opsymbol, piecelist) == True:
                condition = 'loss'
                greatergoing = False
                going = False
                gameended = True
            count = 0
            if waiting:
                screen.fill(white)
                game.displayobj(0)
                game.displayobj(1)
                screen.blit(vs, (opx, opy))
                screen.blit(opname, (opx, opy + 40))
                mouse = pygame.mouse.get_pos()
                for i in range(0, 9):
                    if piecelist[i] != '':
                        screen.blit(imagelist[i], (coordlist[i][0], coordlist[i][1]))

                pygame.display.flip()
                pygame.display.update()

                ready,_,_ = select.select([client], [], [], 0.01)
                if ready:
                    msg = client.recv(2048).decode(FORMAT)
                    if msg == 'opponent has disconnected':
                        print('opponent has disconnected')
                        waiting = False
                        going = False
                        greatergoing = False
                        return 'server error'
                    elif msg[0:9] == 'move made':
                        movemade = int(msg[9:len(msg)])
                        match movemade:
                            case 0:
                                templist = [70, 130]
                            case 1:
                                templist = [70, 255]
                            case 2:
                                templist = [70, 375]
                            case 3:
                                templist = [195, 130]
                            case 4:
                                templist = [195, 255]
                            case 5:
                                templist = [195, 375]
                            case 6:
                                templist = [320, 130]
                            case 7:
                                templist = [320, 255]
                            case 8:
                                templist = [320, 375]

                        image = pygame.image.load('images//' + opsymbol + '.png')
                        image = pygame.transform.scale(image, (100, 100))

                        piecelist[movemade] = opsymbol
                        imagelist[movemade] = image
                        coordlist[movemade] = templist

                        waiting = False
                        going = True
                        
                pygame.display.flip()
                pygame.display.update()
                        
                
    # after match
    match condition:
        case 'win':
            game.createobj('images//win1.png', (450, 450), 50, 50)
            game.createobj('images//win2.png', (450, 450), 50, 50)
        case 'loss':
            game.createobj('images//loss1.png', (450, 450), 50, 50)
            game.createobj('images//loss2.png', (450, 450), 50, 50)
        case 'tie':
            game.createobj('images//draw.png', (450, 450), 50, 50)
    newtime = time()
    currentime = time()
    going = True
    while newtime - currentime < 5 and going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send('disconnect')
                going = False
                pygame.quit()
                return 'exit'
        if newtime - currentime < 5 and going:
            screen.fill(white)
            game.displayobj(0)
            screen.blit(vs, (opx, opy))
            screen.blit(opname, (opx, opy + 40))
            mouse = pygame.mouse.get_pos()
            for i in range(0, 9):
                if piecelist[i] != '':
                    screen.blit(imagelist[i], (coordlist[i][0], coordlist[i][1]))

            if condition != 'tie':
                game.displayobj(3)
                tnewtime = time()
                tcurrentime = time()
                while tnewtime - tcurrentime < 0.5:
                    tnewtime = time()
                    
                pygame.display.flip()
                pygame.display.update()
                
                game.displayobj(4)
                tnewtime = time()
                tcurrentime = time()
                while tnewtime - tcurrentime < 0.5:
                    tnewtime = time()
            else:
                game.displayobj(3)

            newtime = time()
            pygame.display.flip()
            pygame.display.update()

                
                

    send('match over')
    return condition

          
mainloop = True
response = ''
activated = False
errorfound = False
updatescores(wins, losses, draws)

if not connected:
    serverdown = menu(screen)
    serverdown.createobj('images//svd.png', (450, 450), 50, 50)
    going = True
    while going:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                going = False
                pygame.quit()
        if going:
            serverdown.displayobj(0)
            pygame.display.flip()
            pygame.display.update()
                

else:
    while mainloop:
        if filefound == False:
            username = username_menu(False)
            userexist = checkforusername(username)
            while userexist:
                username = username_menu(True)
                userexist = checkforusername(username)
            with open('files\\namefile.txt', 'w') as f:
                f.write(username)
            filefound = True

        if activated == False:
            userexist = checkforusername(username)
            if not userexist:
                open('files\\namefile.txt', 'w').close()
                wins = 0
                losses = 0
                draws = 0
                updatescores(wins, losses, draws)
                username = username_menu(False)
                userexist = checkforusername(username)
                while userexist:
                    username = username_menu(True)
                    userexist = checkforusername(username)
                with open('files\\namefile.txt', 'w') as f:
                    f.write(username)

            activate_account(username)
            activated = True
        response = startmenu(wins, losses, draws, errorfound)
        errorfound = False
        if response == 'exit':
            mainloop = False
            updatescores(wins, losses, draws) 
            pygame.quit()
        elif response == 'public':
            pubresponse = publicgame()
            if pubresponse[0] == 'timeout':
                errorfound = True
            elif pubresponse[0] == 'stop looking':
                pass
            elif pubresponse[0] == 'exit':
                mainloop = False
                updatescores(wins, losses, draws) 
                pygame.quit()
            else:
                print('connected publicly')
                response = playgame(pubresponse[0], int(pubresponse[1]))
                if response == 'server error':
                    print('server error')
                    send('match over')
                    errorfound = True
                else:
                    match response:
                        case 'win':
                            if wins < 999:
                                wins += 1
                        case 'loss':
                            if losses < 999:
                                losses += 1
                        case 'tie':
                            if draws < 999:
                                draws += 1
                    send('public game ended')
        elif response == 'private':
            response = privategame()
            if response == 'back':
                pass
            elif response == 'join':
                response = joingame()
                if response == 'server error':
                    errorfound = True
                elif response == 'stop looking':
                    pass
                elif response == 'exit':
                    mainloop = False
                    updatescores(wins, losses, draws) 
                    pygame.quit()
                else:
                    print('it worked')
                    print(response)
                    response = playgame(response, 1)
                    if response == 'server error':
                        errorfound = True
                    elif response == 'exit':
                        mainloop = False
                        updatescores(wins, losses, draws) 
                        pygame.quit()
                    else:
                        match response:
                            case 'win':
                                if wins < 999:
                                    wins += 1
                            case 'loss':
                                if losses < 999:
                                    losses += 1
                            case 'tie':
                                if draws < 999:
                                    draws += 1
            elif response == 'host':
                response = hostgame()
                if response == 'stopped hosting':
                    pass
                elif response == 'exit':
                    mainloop = False
                    updatescores(wins, losses, draws) 
                    pygame.quit()
                elif response == 'server error':
                    errorfound = True
                else:
                    print('it worked')
                    print(response)
                    response = playgame(response, 0)
                    if response == 'server error':
                        errorfound = True
                    elif response == 'exit':
                        mainloop = False
                        updatescores(wins, losses, draws) 
                        pygame.quit()
                    else:
                        match response:
                            case 'win':
                                if wins < 999:
                                    wins += 1
                            case 'loss':
                                if losses < 999:
                                    losses += 1
                            case 'tie':
                                if draws < 999:
                                    draws += 1

