import asyncio
import websockets
import sys
from binta_core import binta 




def clear_blank_space(string):
    string =  string.split(' ')
    new_string = [el for el in string if el !='']
    return " ".join(new_string)

def clear_speech(original_speech, badwords):
    new_speech = original_speech
    for word in badwords:
        new_speech= new_speech.replace(word, "")
    return clear_blank_space(new_speech)


async def listen(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            speech = await websocket.recv()
            #tout les commandes vocales sexecutent ici
            keyword_activators = ["ok binta", "okay binta", 
            "ok ben ca", "okay ben ca", "binta", "ben ca"]

            if any(keyword in speech for keyword in keyword_activators):
                parole = clear_speech(speech, keyword_activators)
                print("orignal",speech)
                print("pure",parole)
                binta.speak(speech.replace('binta',''))
            else:
                print('desolé binta nest pas dispo!')


asyncio.run(listen('ws://localhost:2700'))