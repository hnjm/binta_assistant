import asyncio
import websockets
import sys

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            speech = await websocket.recv()
            #tout les commandes vocales sexecutent ici
            if "binta" in speech:
                print(speech)
            else:
                print('desolé binta nest pas dispo!')


asyncio.run(listen('ws://localhost:2700'))