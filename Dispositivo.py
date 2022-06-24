import asyncio
import random
from datetime import datetime
import requests


lista=[]

loop=asyncio.get_event_loop()
async def dispositivo(id):
    while True:
        await asyncio.sleep(10)
        print(datetime.now())
        data= {"id":id,"valor":random.randrange(3,100),
               "fecha":datetime.timestamp(datetime.now())}
        print(data)
        lista.append(data)

async def enviar_métrica():
    while True:
        await asyncio.sleep(15)
        if len(lista)>0:
            dato=lista.pop()
            response3=requests.post("http://127.0.0.1:8000/metrica",params={"id":dato["id"],"timestamp":dato["fecha"],"metrica":dato["valor"]})
        print("sigo en pie")

future=loop.create_task(dispositivo(2))
loop.run_until_complete(enviar_métrica())





