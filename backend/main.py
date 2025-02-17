from fastapi import FastAPI
from core.dijkstra import dijkstra

app = FastAPI()

@app.get("/shortest-path")
async def get_shortest_path(start:str, end:str):
    return dijkstra(start, end)