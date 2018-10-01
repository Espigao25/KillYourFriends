import websockets
#import random
import asyncio
import queue
import time
#import socketserver
import kyf

global session


def startTCP(mafiaGame):
    global session
    session = mafiaGame
    asyncio.set_event_loop(asyncio.new_event_loop())

    start_server2 = websockets.serve(speakerTCP, '192.168.0.101', 9998)

    asyncio.get_event_loop().run_until_complete(start_server2)
    asyncio.get_event_loop().run_forever()



async def speakerTCP(websocket, path):

    while True:  ## ISTO PRECISA DE TRABALHO, PARA SUPORTAR RECONECÇÕES
        receive_task = asyncio.ensure_future(
            rcvData(websocket, path))
        transmit_task = asyncio.ensure_future(
            sndData(websocket, path))
        done, pending = await asyncio.wait(
            [receive_task, transmit_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

async def sndData(websocket, path):

        if session.outgoingQueue.empty() == False:
            await websocket.send(session.outgoingQueue.get())


async def rcvData(websocket, path):

        name = await websocket.recv()

        i = 0
        lista = []
        for x in range(len(name)):
            f = x
            if name[x] == ',':
                lista.append(name[i:f])
                i = x+1
        lista.append(name[i:])
        #print(lista)
        session.rcvCommand(lista)
        #print(lista)


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
