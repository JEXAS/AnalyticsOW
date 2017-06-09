import zmq
import time

context = zmq.Context(1)
# Socket facing clients
frontend = context.socket(zmq.PULL)
frontend.bind("tcp://*:5559")
# Socket facing services
backend = context.socket(zmq.PUSH)
backend.bind("tcp://*:5560")

zmq.device(zmq.STREAMER, frontend, backend)
