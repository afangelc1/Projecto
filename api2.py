from fastapi import FastAPI
import csv

app=FastAPI()

@app.get("/")
async def index():
    return "mensaje"

diccionario={}

@app.get("/metrica")
async def get_all():
    if len(diccionario)==0: #Preguntar de nuevo
        read_all()
    return diccionario


@app.post("/metrica")
async def crear(id:int,timestamp:str, metrica:int):
    if len(diccionario)==0: #Preguntar de nuevo
        read_all()
    diccionario[timestamp]={"id":id,"metrica":metrica}
    write_doc(id,timestamp, metrica)
    return diccionario

@app.put("/metrica")
async def actualizar(id:int,timestamp:str, metrica:int):
    diccionario[timestamp]={"id":id,"metrica":metrica}
    reescribir()
    return diccionario

@app.delete("/metrica")
async def eliminar(timestamp:str):
    diccionario.pop(timestamp)
    reescribir()
    return diccionario


def read_all():
    with open("metricas.csv","r") as file:
        lector=csv.reader(file)

        for fila in lector:
            diccionario[fila[1]]={"id":fila[0],"metrica":fila[2]}

#
def write_doc(id:int,timestamp:str, metrica:int):
    diccionario[timestamp]={"id":id,"metrica":metrica} # Para que el cambio se vea reflejado en el diccionario
    with open("metricas.csv","a+",newline="") as file:
        escritor=csv.writer(file,delimiter=",")
        escritor.writerow([id,timestamp,metrica])#Aquí también se escribe en el archivo

def reescribir():
    with open("metricas.csv","w",newline="") as file:
        escritor=csv.writer(file,delimiter=",")
        for i in diccionario:
            escritor.writerow([diccionario[i]["id"],i,diccionario[i]["metrica"]])














