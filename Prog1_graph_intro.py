# intro graph
# working on dictionary is easier, compact and saves time
# so we convert the list of tuples into dictionary first
class Graph:
    def __init__(self, routes_list):
        self.routes_list = routes_list
        self.graph_dic = {}
        for start, end in self.routes_list:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]


routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto')
]
route_graph = Graph(routes)

print(route_graph.graph_dic)
