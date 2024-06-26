from src.dijkstra import dijkstra
from src.graph import get_graph

def main():
    graph = get_graph()
    start_node = 'YOGYAKARTA'
    end_node = 'BANDUNG'

    distance, route = dijkstra(graph, start_node, end_node)

    print(f"The shortest route from {start_node} to {end_node} is:")
    for node in route:
        print(f"{node} -> ", end="")
    print(f"{end_node}")
    print(f"Total distance: {distance}")

if __name__ == "__main__":
    main()
