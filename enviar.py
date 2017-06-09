import tweepy
import time

#keys to access Twitter
CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
ACCESS_KEY = '...'
ACCESS_SECRET = '...'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    subir = open('graficas.txt', 'r')
    lista = []
    for i in subir:
        lista.append(i)

    for i in lista:
        send = i.split()
        print(send[1])
        toSend = 'Datos de '+send[2]+': '+send[0]
        api.send_direct_message(send[1], text=toSend)
    borrar = open('graficas.txt', 'w')
    borrar.close()
    time.sleep(300)
