from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import requests
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["PUT"],
    allow_headers=["*"],
)

@app.put("/")
async def root(request: Request):
    data = await request.json()
    ip = data["ip"]
    output = await locate(ip)
    try:
        with open("victims.txt", "a", encoding="utf-8") as f:
            f.write(output)
    except FileExistsError:
        print("file.txt already exists, exclusive creation aborted.")

async def locate(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    return json.dumps(data)