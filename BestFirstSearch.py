from collections import deque

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
    vertices = ["S", "A", "B", "C", "D", "E", "F", "G"]
    states = [4, 4, 2, 3, 1, 1, 0, 0]
    edges = [
        ("S", "A", 2),
        ("S", "B", 6),
        ("A", "B", 2),
        ("A", "C", 1),
        ("B", "E", 5),
        ("B", "F", 4),
        ("B", "E", 5),
        ("C", "E", 2),
        ("C", "D", 5),
        ("D", "E", 1),
        ("D", "G", 1),
        ("E", "G", 5),
    ]
    g = Graph()
    for vertex, state in zip(vertices, states):
        g.add_vertex(vertex, state)
    for edge in edges:
        g.add_edge(*edge)
    
    closed_list = BFS(g)
    
    print(closed_list)


def BFS(g):
    open_list = deque()
    open_list.append(('S', 4))
    closed_list = deque()
    while True:
        s = open_list.pop()[0]
        closed_list.append(s)
        if s == 'G':
            break
        for v in g.vertices[s].edges:
            if not (g.vertices[v[0]].id, g.vertices[v[0]].state) in open_list:
                open_list.append((g.vertices[v[0]].id, g.vertices[v[0]].state))
        
        for i in range(len(open_list) - 1):
            if open_list[i + 1][1] > open_list[i][1]:
                tmp = open_list[i + 1]
                open_list[i + 1] = open_list[i]
                open_list[i] = tmp

        if not open_list:
            break

    return closed_list


if __name__ == '__main__':
    main()