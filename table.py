class Tableau:
    def __init__(self):
        self.xs = []
        self.ys = []
    def add(self, x, y):
        self.xs.append(x)
        self.ys.append(y)
    def get(self):
        return self.xs, self.ys
    def get_y(self, x):
        if x in self.xs:
            index = self.xs.index(x)
            return self.ys[index]
        else:
            return None