class Bfs:
    g = Grafica()
    def __ini__(self):
        self.bfs = {}

    def bfs(self, r):
        g = Grafica()
        if r in g.vertices:
            cola = [r]

            g.vertices[r].visitado = True
            g.vertices[r].nivel = 0

            print("("+ str(r) + ", "+ str(g.vertices[r].nivel)+")")

            while (len(cola) > 0):
                act = cola[0]
                cola = cola[1:]

                for v in g.vertices[act].vecinos:
                    if g.vertices[v].visitado == False:
                        cola.append(v)
                        g.vertices[v].visitado = True
                        g.vertices[v].nivel = g.vertices[act].nivel + 1
                        print("(" + str (v) + ", " + str(g.vertices[v].nivel) + ")")

