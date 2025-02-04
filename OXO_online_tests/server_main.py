# oxo server

import socket
import threading
from time import *
from random import randint 

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = ''
print(SERVER)
HEADER = 256
FORMAT = 'utf-8'

mainserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mainserver.settimeout(1)

mainserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mainserver.bind(('0.0.0.0', PORT))

# get the usernames in the text file and save to a list
# if a client is new, server will recieve a message and then check if the username recieved is valid
# if not, returns a False message
# if true, adds name to list

usernames = []
banned = ['usernamecheck','activate','hosting''stopped hosting','joining','player joining','looking for public','public game ended','yournum','turnoff','creating game','move made','match over','game disconnect','public game disconnect','disconnect','hitler']

#.encode(FORMAT)

currentuser = ''
count = 0
loopcount = 0
with open('files//usernames.txt', 'r') as f:
    users = f.read()
    while loopcount < len(users) - 1:
        if users[loopcount] != '\n':
            count = 0
            currentuser = ''
            while users[loopcount + count] != '\n' and loopcount + count < len(users) - 1:
                currentuser += users[loopcount + count]
                count += 1
            loopcount += count
            usernames.append(currentuser)
            print(currentuser)
            loopcount += 1

onlineusers = ['']*(len(usernames)) #holds usernames of all active members
onlineips = [None]*(len(usernames)) #holds ip addresses of all active members. each address has the same index as online users counterpart
publicstatus = [0]*(len(usernames)) #holds the public status of each active member, for checking if they are looking for a game or in a game. same index as online users.

lobbies = [] # lobby theory yo

turnoff = False
def client_talk(conn, addr):
    global turnoff
    global onlineips
    global onlineusers
    global usernames
    global lobbies
    # add a feature where a specific client (the button) can turn off the server
    # when this happens, the username database text file thing is updated
    connected = True
    hosting = False
    joining = False
    public = False
    username = ''
    hostname = ''
    joinname = ''

    opname = ''
    opip = None
    movemade = -1
    while connected:
##        for i in range(0, len(onlineips)):
##            print(onlineips[i])
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: # checks to see if msg is empty
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == 'usernamecheck':
                # when a username is being sent
                conn.send('usernamecheck recieved'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                while not msg_length:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg in usernames or msg in banned: #if in the list or banned, ask for resend
                    conn.send('accept'.encode(FORMAT))
                    print('already in list')
                else: #if not, put them in the list
                    usernames.append(msg)
                    open('files//usernames.txt', 'w').close()
                    with open('files//usernames.txt', 'w') as f:
                        for i in range(0, len(usernames)):
                            f.write(usernames[i])
                            f.write('\n')
                    onlineusers.append('')
                    onlineips.append(None)
                    publicstatus.append(0)
                    conn.send('decline'.encode(FORMAT))
                    print('now in list')
            
            elif msg == 'activate':
                conn.send('activated'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                while not msg_length:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                username = msg
                onlineips[usernames.index(username)] = conn
                onlineusers[usernames.index(username)] = username
                publicstatus[usernames.index(username)] = 1
                print('account activated')

                
            elif msg == 'hosting':
                hosting = True
                print(username)
                conn.settimeout(10)
                while hosting:
                    for i in range(0, len(usernames)):
                        if publicstatus[i] == 1 and onlineips[i] != conn:
                            onlineips[i].send((username + ' is hosting').encode(FORMAT))
##                            print(onlineips[i])

                    try:
                        msg_length = conn.recv(HEADER).decode(FORMAT)
                    except:
                        pass
##                    initime = time()
##                    newtime = time()
##                    while newtime - initime < 10 and not msg_length:
##                        newtime = time()
##                        msg_length = conn.recv(HEADER).decode(FORMAT)
                    
                    try:
                        
                        if msg_length:
                            msg_length = int(msg_length)
                            msg = conn.recv(msg_length).decode(FORMAT)
                            print(msg)
                            if msg == 'stopped hosting':
                                hosting = False
                    except:
                        pass
                conn.settimeout(None)

            elif msg[0:14] == 'player joining' and joining == True:
                joining = False
                print('hell yes')
                onlineips[usernames.index(hostname)].send(('player found:' + msg[14:len(msg)]).encode(FORMAT))

            elif msg == 'joining':
                joining = True
                conn.send('joining recieved'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                while not msg_length:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                msg_length = int(msg_length)
                hostname = conn.recv(msg_length).decode(FORMAT)
                print(hostname)

            elif msg == 'looking for public':
                conn.settimeout(5)
                if len(lobbies) == 0:
                    lobbies.append([])

                if len(lobbies[len(lobbies) - 1]) <= 1:
                    lobbies[len(lobbies) - 1].append(username)
                else:
                    lobbies.append([])

                currentslot = len(lobbies) - 1

                newtime = time()
                currentime = newtime
                timelimit = 120

                quitlook = False

                while newtime - currentime < timelimit and len(lobbies[currentslot]) <= 1 and not quitlook:
                    try:
                        msg_length = conn.recv(HEADER).decode(FORMAT)
                    except:
                        pass
                    try:
                        if msg_length:
                            msg_length = int(msg_length)
                            msg = conn.recv(msg_length).decode(FORMAT)
                            if msg == 'quit looking':
                                quitlook = True
                    except:
                        pass
                            
                    newtime = time()
                conn.settimeout(None)
                if not quitlook:
                    if newtime - currentime == 0:
                        newtime = time()
                        currentime = time()
                        while newtime - currentime < 10:
                            newtime = time() # to fix off timing issue
                    newtime = time()
                    currentime = time()
                    while newtime - currentime < 5:
                        newtime = time() # to fix off timing issue
                        
                    if len(lobbies[currentslot]) == 2:
                        opindex = lobbies[currentslot].index(username)
                        if opindex == 0:
                            opindex = 1
                        else:
                            opindex = 0

                        opname = lobbies[currentslot][opindex]
                        print(opname)
                        print('\n')
                        print(usernames.index(opname))

                        conn.send((str(opindex)+'player found'+opname).encode(FORMAT))
                    else:
                        conn.send('timeout'.encode(FORMAT))
                        del lobbies[currentslot]
                        currentslot = -1

            elif msg == 'public game ended':
                if opindex == 1:
                    count = 0
                    userfound = False
                    while count < len(lobbies):
                        if lobbies[count][0] == username:
                            userfound = True
                            del lobbies[count]

                        count += 1
                            
                
                            




















                
##                public = True
##                absolnew = time()
##                absolcur = time()
##                while absolnew - absolcur < 120 and public:
##                    absolnew = time()
##                    print(str(absolnew - absolcur))
##                    hoj = randint(1, 2) #flip a coin to see if you are either a joiner or a hoster
##                    if hoj == 1: #hoster
##                        print(username + ' is a hoster')
##                        publicstatus[usernames.index(username)] = 2
##                        newtime = time()
##                        currentime = time()
##                        conn.settimeout(5)
##                        pubhosting = True
##                        while newtime - currentime < 60 and pubhosting:
##                            stoplooking = False
##                            newtime = time()
##                            #print(str(newtime - currentime))
##                            position = usernames.index(username) + 1
##                            if position >= len(usernames):
##                                position = 0
##
##                            while position != usernames.index(username) and stoplooking == False:
##                                if position >= len(usernames):
##                                    position = 0
##
##                                if publicstatus[position] == 3:
##                                    #stoplooking = True
##                                    onlineips[position].send(('sending public invite'+username).encode(FORMAT))
##                                    
##                                position += 1
##
##
##                            try:
##                                msg_length = conn.recv(HEADER).decode(FORMAT)
##                            except:
##                                pass
##                            
##                            try:
##                                
##                                if msg_length:
##                                    msg_length = int(msg_length)
##                                    msg = conn.recv(msg_length).decode(FORMAT)
##                                    print(msg)
##                                    if msg == 'timeout':
##                                        pubhosting = False
##                                        public = False
##                            except:
##                                pass
##                        conn.settimeout(None)
##                    else: #joiner
##                        print(username + ' is a joiner')
##                        publicstatus[usernames.index(username)] = 3
##                        newtime = time()
##                        currentime = time()
##                        conn.settimeout(5)
##                        pubjoining = True
##                        while newtime - currentime < 60 and pubjoining:
##                            newtime = time()
##                            #print(str(newtime - currentime))
##                            try:
##                                msg_length = conn.recv(HEADER).decode(FORMAT)
##                            except:
##                                pass
##                            
##                            try:
##                                
##                                if msg_length:
##                                    msg_length = int(msg_length)
##                                    msg = conn.recv(msg_length).decode(FORMAT)
##                                    print(msg)
##                                    if msg[0:22] == 'public invite recieved':
##                                        pubjoining = False
##                                        public = False
##                                        opname = msg[22:len(msg)]
##                                        onlineips[usernames.index(opname)].send(('public invite recieved too'+username).encode(FORMAT))
##                                    elif msg == 'timeout':
##                                        public = False
##
##                            except:
##                                pass
##
##
##                        conn.settimeout(None)
                    
##                    stoplooking = False
##                    ttl = randint(10, 200) #ttl = time to live
##                    #print(username + ' will wait for ' + str(ttl))
##                    conn.settimeout(ttl)
##                    
##                    try:
##                        msg_length = conn.recv(HEADER).decode(FORMAT)
##                    except:
##                        pass
##                    
##                    try:
##                        
##                        if msg_length:
##                            msg_length = int(msg_length)
##                            msg = conn.recv(msg_length).decode(FORMAT)
##                            print(msg)
##                            if msg[0:22] == 'public invite recieved':
##                                public = False
##                                opname = msg[22:len(msg)]
##                                onlineips[usernames.index(opname)].send(('public invite recieved too'+username).encode(FORMAT))
##                            elif msg == 'timeout':
##                                public = False
####                            elif msg == 'finished waiting':
####                                pass
##                    except:
##                        pass
##
##                    if public:
##                        position = usernames.index(username) + 1
##                        if position >= len(usernames):
##                            position = 0
##
##                        while position != usernames.index(username) and stoplooking == False:
##                            if position >= len(usernames):
##                                position = 0
##
##                            if publicstatus[position] == 2:
##                                stoplooking = True
##                                onlineips[position].send(('sending public invite'+username).encode(FORMAT))
##                                
##                            position += 1
##                conn.settimeout(None)
##                if public:
##                    conn.send('timeout'.encode(FORMAT))
##                opname = ''
##                print('finished')
##                publicstatus[usernames.index(username)] = 1

            elif msg[0:7] == 'yournum':
                opip.send(('opnum' + msg[7:len(msg)]).encode(FORMAT))

                
            
            elif msg == 'turnoff':
                turnoff = True
                connected = False
                # maybe involve a double check for the correct user

            elif msg == 'creating game':
                conn.send('game created'.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                msg_length = int(msg_length)
                opname = conn.recv(msg_length).decode(FORMAT)
                opip = onlineips[usernames.index(opname)]
                conn.send('opponent recieved'.encode(FORMAT))

            elif msg[0:9] == 'move made' and opname != '':
                print(msg)
                movemade = int(msg[9:len(msg)])
                opip.send(('move made' + str(movemade)).encode(FORMAT))

            elif msg == 'match over':
                hostname = ''
                opname = ''
                opip = None

            elif msg == 'game disconnect':
                opip.send('opponent has disconnected'.encode(FORMAT))
                hostname = ''
                opname = ''
                opip = None

            elif msg == 'public game disconnect':
                opip.send('opponent has disconnected'.encode(FORMAT))
                hostname = ''
                opname = ''
                opip = None
                count = 0
                userfound = False
                while count < len(lobbies):
                    if lobbies[count][0] == username:
                        userfound = True
                        del lobbies[count]

                    count += 1

            elif msg == 'disconnect':
                hostname = ''
                opname = ''
                opip = None
                onlineips[usernames.index(username)] = None
                publicstatus[usernames.index(username)] = 0
                onlineusers[usernames.index(username)] = ''
                connected = False
                
                
    conn.close()


def start():
    mainserver.listen()
    print('Server start')
    while turnoff == False:
        conn, addr = mainserver.accept()
        
        thread = threading.Thread(target=client_talk, args=(conn, addr))
        thread.start()
##    with open('files//usernames.txt', 'w') as f:
##        for name in usernames:
##            f.write(name)
##            f.write('\n')
        

start()
open('files//usernames.txt', 'w').close()
with open('files//usernames.txt', 'w') as f:
    for i in range(0, len(usernames) - 1):
        f.write(usernames[i])
        f.write('\n')
    f.write(usernames[len(usernames) - 1])


        
    
