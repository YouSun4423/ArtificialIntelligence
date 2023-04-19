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
    
    ans, visited = HC(g)
    print(ans, visited)


def HC(g):
    current_v = 'S'
    visited = []
    h = INF
    while True:
        next_v_list = []
        visited.append(current_v)
        for v in g.vertices[current_v].edges:
            next_v_list.append((g.vertices[v[0]].id, g.vertices[v[0]].state))
        for v in next_v_list:
            if v[1] < h:
                h = v[1]
                next_v = v[0]
        if next_v == current_v:
            break

        current_v = next_v

    return current_v, visited


if __name__ == '__main__':
    main()