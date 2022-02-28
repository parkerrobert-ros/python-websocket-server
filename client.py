#!/usr/bin/env python3
import websockets
import asyncio

PORT = 9090
print(f"Server is listening on: {PORT}")

async def echo(websocket, path):
  print("A client has just connected")
  async for message in websocket:
    print("Received a message from client: " + message)
    await websocket.send("received from" + message)
    
start_server = websockets.serve(echo, "0.0.0.0", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
