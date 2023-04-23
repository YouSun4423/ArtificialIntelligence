import heapq

INF = 9999999


class Vertex:
    def __init__(self, id, state):
        self.id = id
        self.state = state
        self.edges = []


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, id, state):
        self.vertices[id] = Vertex(id, state)

    def add_edge(self, source, dest, weight):
        self.vertices[source].edges.append((dest, weight))
        self.vertices[dest].edges.append((source, weight))

    def check_graph(self):
        for vertex_id, vertex in self.vertices.items():
            print(f"V {vertex_id}: S={vertex.state}, E={vertex.edges}")

    def check_cost(self, source, dest):
        for v in self.vertices[source].edges:
            print(v)
            if v[0] == dest:
                return v[1]


def main():
    vertices = ["S", "A", "B", "C", "D", "E", "G"]
    states = [8, 6, 2, 4, 7, 1, 0]
    edges = [
        ("S", "A", 4),
        ("S", "C", 5),
        ("S", "D", 2),
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 3),
        ("B", "E", 3),
        ("B", "G", 2),
        ("C", "D", 2),
        ("C", "E", 1),
        ("D", "E", 1),
        ("E", "G", 5),
    ]
    g = Graph()
    for vertex, state in zip(vertices, states):
        g.add_vertex(vertex, state)
    for edge in edges:
        g.add_edge(*edge)
    
    path, closed_list = A_star(g, "S", "G")
    
    print(path, closed_list)


def h_score(graph, current, goal):
    distances = {v: float('inf') for v in graph.vertices}
    distances[current] = 0

    heap = [(0, current)]
    while heap:
        (d, v) = heapq.heappop(heap)
        if v == goal:
            return distances[goal]
        for neighbor, weight in graph.vertices[v].edges:
            distance = distances[v] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return float('inf')


def A_star(graph, start, goal):
    open_list = [(h_score(graph, start, goal), 0, start)]  # (f, step, node)
    closed_list = set()
    g_scores = {v: float('inf') for v in graph.vertices}
    g_scores[start] = 0
    parents = {start: start}

    while open_list:
        f, step, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current != parents[current]:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path, closed_list

        closed_list.add(current)

        for neighbor, weight in graph.vertices[current].edges:
            tentative_g_score = g_scores[current] + weight
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = (
                    g_scores[neighbor] + h_score(graph, neighbor, goal),
                    step + 1,
                    neighbor,
                )
                parents[neighbor] = current
                if neighbor in closed_list:
                    closed_list.remove(neighbor)
                heapq.heappush(open_list, f_score)

        open_list.sort()
        open_list.sort(key=lambda x: x[1])
        current_step = open_list[0][1]
        same_f = []
        while open_list and open_list[0][1] == current_step:
            same_f.append(heapq.heappop(open_list))
        same_f.sort(key=lambda x: x[2])
        open_list = same_f + open_list

    return None, closed_list


if __name__ == '__main__':
    main()