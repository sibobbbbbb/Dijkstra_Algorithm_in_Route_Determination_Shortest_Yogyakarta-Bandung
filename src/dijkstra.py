import heapq

def dijkstra(graph, start, end):
    node_weights = {}
    shortest_path = {}
    for node in graph:
        if node == start:
            node_weights[node] = 0
        else:
            node_weights[node] = float('infinity')
        shortest_path[node] = []

    prioQ = [(0, start)]

    while prioQ:
        current_distance, current_node = heapq.heappop(prioQ)
        if current_distance > node_weights[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < node_weights[neighbor]:
                node_weights[neighbor] = new_distance
                shortest_path[neighbor] = shortest_path[current_node] + [current_node]
                heapq.heappush(prioQ, (new_distance, neighbor))
    
    return node_weights[end], shortest_path[end]
