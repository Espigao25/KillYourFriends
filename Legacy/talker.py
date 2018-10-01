import websockets
#import random
import asyncio
import queue
import time
#import socketserver
import kyf

global session

async def sndData(websocket, path):

    z = time.time()
    while ((time.time() - z) < 60 ):   # The connection closes if 60 seconds go by without receiving anything
        time.sleep(0.1)
        if session.outgoingQueue.empty() == False:
            await websocket.send(session.outgoingQueue.get())
            z = time.time()



def startTCP(mafiaGame):
    global session
    session = mafiaGame
    asyncio.set_event_loop(asyncio.new_event_loop())

    start_server2 = websockets.serve(sndData, '192.168.0.101', 9997)

    asyncio.get_event_loop().run_until_complete(start_server2)
    asyncio.get_event_loop().run_forever()


# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     The request handler class for our server.
#
#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """
#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         name = self.request.recv(1024).strip()
#
#         i = 0
#         lista = []
#         for x in range(len(name)):
#             f = x
#             if name[x] == ',':
#                 lista.append(name[i:f])
#                 i = x+1
#         lista.append(name[i:])
#         print(lista)
#         sendtoQueue(lista)
#
# def sendtoQueue(data):
#     dataQueue.put(data)
#     print(dataQueue.get())
#
# def startTCP():
#
#     HOST, PORT = "192.168.0.101", 9998
#
#     # Create the server, binding to localhost on port 9999
#     server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
#
#     # Activate the server; this will keep running until you
#     # interrupt the program with Ctrl-C
#     server.serve_forever()
