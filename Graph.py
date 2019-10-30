class Vertex:
    def __init__(self, vertexes):
        self.flag = -1
        self.vertexes = vertexes

    def add_vertex(self, vertex):
        self.vertexes.append(vertex)

    def change_flag(self, flag):
        self.flag = flag

    def __str__(self):
        return "flag: " + str(self.flag) + " vertexes: " + str(self.vertexes)
