#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import random

async def hello(websocket, path):
    name = await websocket.recv()

    greeting = name

    #await websocket.send(greeting)
    print(type(greeting))
    #for x in len(name):
        #print(name[x])

    i = 0
    lista = []
    for x in range(len(name)):
        f = x
        if name[x] == ',':
            lista.append(name[i:f])
            i = x+1
    lista.append(name[i:])

    print(lista)
    random.shuffle(lista)
    print(lista)

    #matriz = [ [lista[x]] for x in range(len(lista))]
    matriz = []

    for x in range(len(lista)-1):
        matriz.append([lista[x],'Villager'])


    print(matriz)
    f = open("matriz.txt", "w")
    f.write(str(matriz))
    f.close()

    return matriz

start_server = websockets.serve(hello, '192.168.0.101', 9998)

asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
