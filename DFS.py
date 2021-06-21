class Dfs:
    g = Grafica()
    def __ini__(self):
        self.dfs = {}

    def dfs(self, r):
        g = Grafica()
        if r in g.vertices:
            g.vertices[r].visitado = True
            for nodo in g.vertices[r].vecinos:
                if g.vertices[nodo].visitado == False:
                    g.vertices[nodo].padre = r
                    print("(" + str(nodo) + ", " + str(r) + ")")
                    g.dfs(nodo)
