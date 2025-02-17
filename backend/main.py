from fastapi import FastAPI
from core.dijkstra import dijkstra

app = FastAPI()
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 2},
    'C': {'D': 2},
    'D': {}
}
@app.get("/shortest-path")
async def get_shortest_path(start:str, end:str):
     return dijkstra(graph, start, end)