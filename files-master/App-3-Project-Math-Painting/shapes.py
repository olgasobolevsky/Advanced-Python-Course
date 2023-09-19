class Square:
    def __init__(self, row, column, side, color):
        self.row = row
        self.column = column
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.row:self.row + self.side, self.column:self.column + self.side] = self.color


class Rectangle:
    def __init__(self, row, column, width, height, color):
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.row:self.row + self.height, self.column:self.column + self.width] = self.color