import sys
from socket import *
from json import dumps
from json import loads
sHostName   = u"codearena.eu"  # host that we want to connect to
nPortNumber = 7654 # port

nUserId = '9501' # your user id
sHash = u'9a25f5a967bf35c2aa1ddab778b4dc58' # your hash

nBufferSize = 8192 # answer buffer size

try:
   client = socket(AF_INET, SOCK_STREAM)  # we create the socket
   client.connect((sHostName, nPortNumber)) # we connect to the server
except Exception, e:
   print u"Could not open socket: %s" % e 
   # error message. Unfortunately we couldn't create the socket and connect to the server

login_dict={}
login_dict['userid']=nUserId
login_dict['hashid']=sHash
login_dict['gamemode']=1
 # we build xml for logging in to the server
client.send(dumps(login_dict)) # xml sending
xmlResponse = client.recv(nBufferSize) # getting the response from the server
print xmlResponse 
xmlResponses=xmlResponse.split( '\n')
response=loads(xmlResponses[0])
if not response['status'] == 'GAME_READY': 
# xml does not have the GAME_READY message. We connected but something has gone wrong and we cannot login
   print "Game not ready"
   sys.exit() # leaving the programm 
else:
   print "LogedIn!" # we are logged in and can send commends for our bot
   print xmlResponse # showing the xml answer 

# further part of the programm, where we will control our bot and send other xml commends


client.close() # closing the socket. end of the programm
