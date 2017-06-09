import tweepy
import time
import zmq

#Create zeroMQ context
ctx = zmq.Context()
sock = ctx.socket(zmq.PUSH)
sock.connect("tcp://127.0.0.1:5559")

#keys to access Twitter
CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
ACCESS_KEY = '...'
ACCESS_SECRET = '...'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    #gets list of DM
    dms = api.direct_messages()

    #Keeps sending the messages to one of the workers available
    for message in dms:
        data = {'data' : [message.sender_id, message.id, message.text]}
        print('Sending ', data)
        sock.send_json(data)
        time.sleep(1)

    #Nap time to let the program rest
    time.sleep(5)
