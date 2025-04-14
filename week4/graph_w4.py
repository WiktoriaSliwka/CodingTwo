class Graph: 
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = set(edges)
        self.adjacency_list = 

g = Graph(
    ["a","b","c"],
    [("a","b"),("b","c"),("a","c")]
)
print(g.adjacency_list)

# adjacency_list  = {
#     "a": ["b","c"],
#     "b": ["a","b"],
#     "c": ["a", "b"]
# }


# adjacency_matrix = {
#     "a": {
#        "a": 1
#        "b": 0
#        "c": 1
#     },
#     "b": {
#         "a": 1
#         "b": 0
#         "c": 1
#     },
#     "c": {
#         "a": 1
#         "b": 1
#         "c": 0
#     }
# }

