import sys
import requests
import json
import time
import random

def check(player, hero, mode):
    url = 'https://owapi.net/api/v3/u/'+player+'/blob'
    time.sleep(random.randint(1,7))

    #Prepare the connections for the HTTPS Request
    debug = {'verbose': sys.stderr}
    user_agent = {'User-agent': 'Mozilla/5.0'}
    imprime  = requests.get(url, headers = user_agent)
    toParse = imprime.json()
    print(url)

    #Check if user exist
    try:
        print('Error: ',toParse['error'])

        if(toParse['error'] == 429):
            return check(player, hero, mode)
        else:
            return 'Usuario no existe'
    except:
        pass

    #Check if hero is played long enough to get data
    if toParse['eu']['heroes']['playtime'][mode][hero] < 1:
        return 'Tiempo de juego insuficiente'

    #If all requirements met, give permission to scrap data
    return [True, toParse]


#return True if the message has already been processed or False in it hasn't
def processed_or_not(dm_id):

    id_list = []
    evaluar = str(dm_id)+'\n'

    #opens the list of processed messages and converts it to a list
    rFich = open('processed.txt', 'r')
    for a in rFich:
        id_list.append(a)

    #check if the message is in the list aka was already processed
    if evaluar in id_list:
        print('Mensaje ya procesado')
        return False

    #writes the id of the message and gives permission to the main to continue
    else:
        wFich = open('processed.txt', 'a')
        wFich.write(evaluar)
        wFich.close()

        return True
