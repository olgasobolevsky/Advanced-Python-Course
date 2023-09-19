from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas settings from user
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter canvas color, E.g. black or white: ")
# Create canvas
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    # Get shape type from user
    shape_type = input("What shape to draw, E.g. rectangle or square. (Type 'quit' to quit): ")
    # In case of rectangle
    if shape_type.lower() == 'rectangle':
        # Get rectangle settings from user
        shape_row = int(input("Enter row: "))
        shape_column = int(input("Enter column: "))
        shape_width = int(input("Enter width: "))
        shape_height = int(input("Enter height: "))
        color_red = int(input("Enter red color : "))
        color_green = int(input("Enter green color : "))
        color_blue = int(input("Enter blue color : "))
        # Create and draw rectangle
        shape = Rectangle(row=shape_row, column=shape_column, width=shape_width, height=shape_height,
                          color=(color_red, color_green, color_blue))
        shape.draw(canvas=canvas)
        # In case of square
    if shape_type.lower() == 'square':
        # Get square settings from user
        shape_row = int(input("Enter row: "))
        shape_column = int(input("Enter column: "))
        shape_side = int(input("Enter side: "))
        color_red = int(input("Enter red color : "))
        color_green = int(input("Enter green color : "))
        color_blue = int(input("Enter blue color : "))
        # Create and draw square
        shape = Square(row=shape_row, column=shape_column, side=shape_side,
                       color=(color_red, color_green, color_blue))
        shape.draw(canvas=canvas)
    # In case of quit - quit
    if shape_type.lower() == 'quit':
        break

# Create canvas file
canvas.make(imagepath='canvas.png')
