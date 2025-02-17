import heapq
from typing import Dict, List, Tuple

def dijkstra(graph,start, end):
    # Create a priority queue - Store (cost, node)
    heap = [(0,start)]
    
    # Dictionary to store the shortest known distance to each node
    shortest_path = {node:float('inf') for node in graph}
    shortest_path[start] = 0 # Distance to start node is 0
    predecessors = {}
    
    while heap:
        # Get the node with the smallest distance
        curren_distance, current_node = heapq.heappop(heap)
        
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors.get(current_node)
            return {"distance": curren_distance, "path": path[::-1]}
        
        # Iterate over neighbors
        for neighbor in graph.get(current_node):
            distance = curren_distance + graph[current_node][neighbor]
            
            # If a shorter path is found, update the and push to heap
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
                
    return {"error":"No path found"}