
# define a node
# Adjacency list implementation
"""
An adjacency list representation for a graph associates each vertex in the graph with the collection of its neighboring vertices or edges. There are many variations of this basic idea, differing in the details of how they implement the association between vertices and collections, in how they implement the collections, in whether they include both vertices and edges or only vertices as first class objects, and in what kinds of objects are used to represent the vertices and edges.

An implementation suggested by Guido van Rossum uses a hash table to associate each vertex in a graph with an array of adjacent vertices. In this representation, a vertex may be represented by any hashable object. There is no explicit representation of edges as objects.[1]
Cormen et al. suggest an implementation in which the vertices are represented by index numbers.[2] Their representation uses an array indexed by vertex number, in which the array cell for each vertex points to a singly linked list of the neighboring vertices of that vertex. In this representation, the nodes of the singly linked list may be interpreted as edge objects; however, they do not store the full information about each edge (they only store one of the two endpoints of the edge) and in undirected graphs there will be two different linked list nodes for each edge (one within the lists for each of the two endpoints of the edge).

The object oriented incidence list structure suggested by Goodrich and Tamassia has special classes of vertex objects and edge objects.

Each vertex object has an instance variable pointing to a collection object that lists the neighboring edge objects. In turn, each edge object points to the two vertex objects at its endpoints.[3]

This version of the adjacency list uses more memory than the version in which adjacent vertices are listed directly, but the existence of explicit edge objects allows it extra flexibility in storing additional information about edges.


"""


class Graph():
    def __init__(self):
        self.nodes = {}
        self.node_count = 0
        print("Graph Created")

    def add_node(self, vert_id=None, vert_connection_ids=None):

        if vert_id == None:
            if vert_connection_ids == None:
                vertex = Vertex(self.node_count)
            else:
                vertex = Vertex(self.node_count, vert_connection_ids)

            self.nodes[self.node_count] = vertex

        self.node_count += 1

    def print_node_attributes(self, v_id):
        if v_id in self.nodes:
            print("ID:{0}".format(self.nodes[v_id].vert_id))

            if len(self.nodes[v_id]["edge_connections"] > 0):
                if "edge_connections" in self.nodes[v_id]:
                    for edge in self.nodes[v_id].edge_connections:
                        print("Edge connected to:{0}".format(edge))
        else:
            print("This Node does not exist")

    def print_all_nodes(self):
        for node in self.nodes:
            print("ID:{0} Connections:{1}".format(
                self.nodes[node].vert_id, self.nodes[node].edge_connections))

    def get_node_count(self):
        return self.node_count


class Vertex():
    def __init__(self, vert_id, connection_ids=None, weight=None):
        self.edge_connections = []
        self.vert_id = vert_id
        self.weight = weight

        if connection_ids != None:
            for vert in connection_ids:
                self.edge_connections.append(
                    Edge([vert, vert_id], weight=weight))

        print("Created Vertex {0}".format(vert_id))


class Edge():
    def __init__(self, endpoints, weight=None):
        self.vertex_endpoints = endpoints
        self.weight = weight
        print("Edge Added between {0} : {1}".format(
            endpoints[0], endpoints[1]))


# n1 = Node()
graph = Graph()
graph.add_node()
graph.add_node(vert_connection_ids=[0])

# graph.print_node_attributes(0)
# graph.print_node_attributes(1)
