# network import
from socket import *
import thread
# log import
import logging
from logging.handlers import RotatingFileHandler

# proto generated import
import imp
imp.load_source('user_pb2', 'src/gen/user_pb2.py')
imp.load_source('tweet_pb2', 'src/gen/tweet_pb2.py')
imp.load_source('ack_pb2', 'src/gen/ack_pb2.py')
from tweet_pb2 import *
from ack_pb2 import *
# manage tweet date import
import datetime

# default settings of the server
PORT = 10000
HOST = '127.0.0.1'
BUFF = sys.getsizeof(Tweet())+140
MAX_CONNECTION = 5

# log config
logging.basicConfig(filename='server.log', level=logging.INFO)  # log in file
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())  # log in the console too

# To fire when a message from a client is received
def handler(clientsock, addr):
    data = clientsock.recv(BUFF)
    response = Ack()
    try:
        if data:
            # get the tweet
            tweet = Tweet();
            tweet.ParseFromString(data)
            # log tweet from user to another
            logger.info(datetime.datetime.fromtimestamp(tweet.timestamp / 1e3).strftime("%Y-%m-%d %H:%M:%S")
                        + ' - Message from ' + tweet.sender.username + ' ' + repr(addr)
                        + ' to ' + ('@'+tweet.receiver.username if tweet.receiver.username else 'everyone') 
                        + ' : ' + tweet.message)
            # set status to OK
            response.status = Ack.OK
            logger.debug(repr(addr) + ' recv:' + tweet.__str__())
            logger.debug(repr(addr) + ' sent:' + response.__str__())
        else:
            # no message
            response.status = Ack.NOK
            response.message = 'Message empty'
    except Exception, e:
        # something went wrong
        logger.exception(e)
        # let's tell it to the client
        response.status = Ack.NOK
        response.message = repr(e.message)
    finally:
        # safe socket close
        clientsock.send(response.SerializeToString())
        clientsock.close()
    
    logger.debug(repr(addr) + "- closed connection")  # log on console

if __name__ == '__main__':
    # server socket initialization
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind((HOST,PORT))
    # listen tweet from client
    serversock.listen(MAX_CONNECTION)
    logger.info('waiting for connection... listening on port : ' + repr(PORT))
    while 1:
        clientsock, addr = serversock.accept()
        # get a tweet !
        logger.debug('...connected from:' + repr(addr))
        thread.start_new_thread(handler, (clientsock, addr))
