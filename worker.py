import zmq
import time
import sys
from check import check
from check import processed_or_not
from data import getMedals
from data import getDamage
from data import getWeaponAccuracy
from data import getHeal
from data import getBlockedDamage
from data import getScopedAccuracy
from data import getGeneralStats
from draw import grafica

#list to sort the attributes to scrap from the Overwatch API
hero_list = ['reinhardt','tracer','zenyatta','junkrat','mccree','winston',
             'orisa','hanzo','pharah','roadhog','zarya','torbjorn','mercy',
             'soldier76','ana','widowmaker','genji','reaper','mei','bastion',
             'symmetra','dva','sombra','lucio']
specials = ['reinhardt', 'junkrat', 'winston', 'symmetra']
healers = ['zenyatta', 'mercy', 'soldier76', 'ana', 'sombra', 'lucio']
snipers = ['widowmaker', 'ana']
tanks = ['reinhardt', 'orisa', 'winston', 'zarya', 'mei', 'symmetra', 'dva']

#Connect to the STREAMER
ctx = zmq.Context()
sock = ctx.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5560")

#Keep going forever
while True:
    work = sock.recv_json()
    data = work['data']
    senderId, messageId, message = data

    unread = processed_or_not(messageId)

    if unread == True:
        #Checks if the message has the correct structure (user hero mode)
        dm = message.split()
        if len(dm) == 3:
            user = dm[0]
            hero = dm[1]
            mode = dm[2]

            #Checks if the hero and the mode are well written to continue
            if hero in hero_list:
                if mode in ['competitive', 'quickplay']:
                    allow = check(user, hero, mode)
                    if allow[0] != True:
                        print (allow)
                    else:
                        #common values to extract no matter the situation
                        general = getGeneralStats(allow[1], hero, mode)
                        medallas = getMedals(allow[1], hero, mode)
                        dmg = getDamage(allow[1], hero, mode)

                        #if hero heals, we get the heal value
                        if hero in healers:
                            heal = getHeal(allow[1], hero, mode)
                        else:
                            heal = 0

                        #if hero snipes, we get sniper accuracy
                        if hero in snipers:
                            snipe = getScopedAccuracy(allow[1], hero, mode)
                        else:
                            snipe = 0

                        #if hero doesnt use accuracy weapons, we don't get the value
                        if hero in specials:
                            accuracy = 0
                        else:
                            accuracy = getWeaponAccuracy(allow[1], hero, mode)

                        #if hero blocks damage, we get the blocked dmg value
                        if hero in tanks:
                            block = getBlockedDamage(allow[1], hero, mode)
                        else:
                            block = 0

                        #We create a list to draw the graphic
                        precision = [snipe, accuracy]
                        grafica(general, medallas, precision, messageId, senderId, hero)
#                        message = 'General data:\n'
#                        message += 'Tier: '+str(general[1])+'\n'
#                        message += 'Level: '+str(general[0])+'\n'
#                        message += 'Points: '+str(general[2])+'\n'

#                        datos = hero.upper()+' data on '+mode.upper()+'\n'
#                        datos += 'Damage dealt: '+str(dmg)+'\n'
#                        if hero in healers:
#                            datos += 'Healing done: '+str(heal)+'\n'
#                        if hero in tanks:
#                            datos += 'Blocked damage: '+str(block)+'\n'
#                        final = message+datos
