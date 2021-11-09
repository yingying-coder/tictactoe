ROWS = [
    ["00", "10", "20"],
    ["01", "11", "21"],
    ["02", "12", "22"],
]


class Board:
    def __init__(self):
        self.rows = ROWS

    def update(self, location, sign):
        self.rows[location[1]][location[0]] = sign

    def print_board(self):
        print(" | ".join(self.rows[2]))
        print("------------")
        print(" | ".join(self.rows[1]))
        print("------------")
        print(" | ".join(self.rows[0]))