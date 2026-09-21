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

tableau = Tableau()
while True:

    x = input("Enter x value (or 'exit' to quit): ")
    if x.lower() == 'exit':
        break
    if x in tableau.xs:
        print(f"x value {x} already exists. Please enter a unique x value.")
        continue
    if x == '':
        print("x value cannot be empty. Please enter a valid x value.")
        continue
    if type(x) is not str:
        print("x value must be a string. Please enter a valid x value.")
        continue
    y = input("Enter y value: ")
    if y == '':
        print("y value cannot be empty. Please enter a valid y value.")
        continue
    if type(y) is not str:
        print("y value must be a string. Please enter a valid y value.")
        continue
    tableau.add(x, y)
    