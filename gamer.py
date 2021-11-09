from coordinate import coordinates, locations


class Gamer:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.positions = []

    def move(self, location):
        pos = coordinates[location]
        self.positions.append(pos)
        locations.remove(location)
        return pos

    def scores(self):
        scores = [[(x, y) for x, y in self.positions if x == y]]
        zloc = [(x, y) for x, y in self.positions if x + y == 2]
        scores.append(zloc)
        for pos in range(3):
            xloc = [(x, y) for x, y in self.positions if x == pos]
            scores.append(xloc)
            yloc = [(x, y) for x, y in self.positions if y == pos]
            scores.append(yloc)
        return scores

    def is_win(self):
        win = False
        score = max(len(loc) for loc in self.scores())
        if score == 3:
            print(f"Game Over\n{self.name} won!")
            win = True
        return win

    def check(self):
        options = []
        for positions in self.scores():
            if len(positions) == 2:
                if positions[0][0] == positions[1][0]:
                    x = positions[0][0]
                    y = 3 - positions[0][1] - positions[1][1]
                elif positions[0][1] == positions[1][1]:
                    x = 3 - positions[0][0] - positions[1][0]
                    y = positions[0][1]
                elif positions[0][0] == positions[0][1]:
                    x = y = 3 - positions[0][0] - positions[1][0]
                elif positions[0][0] + positions[0][1] == 2:
                    x = 3 - positions[0][0] - positions[1][0]
                    y = 3 - positions[0][1] - positions[1][1]
                pos = str(x) + str(y)
                if pos in locations:
                    options.append(pos)
        return options