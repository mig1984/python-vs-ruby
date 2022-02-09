from fastapi import FastAPI
import datetime
import json

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/api/current-time")
def read_root():
    return {'timestamp': int(datetime.datetime.now().timestamp())}

@app.get("/api/bigdata")
def read_item():
    d = {}
    for k in range(0, 2000):
        a = []
        for i in range(99, -1, -1):
            a.append(i)
        d[k] = a
    return d

#TODO: don't know how to match certain regexp in the path
#@app.get("/api/{i}/{rxp}")
#def read_item(i: Integer, rxp):
