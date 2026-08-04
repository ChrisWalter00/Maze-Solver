from turtle import Screen, Turtle

PATH_WIDTH = 15

def get_pixel_color(x, y):
    canvas = screen.getcanvas()
    items = canvas.find_overlapping(x, y, x, y)

    if items:
        return canvas.itemcget(items[0], "fill")  # get 0 object (canvas)

    return None

screen = Screen()
width, height = screen.window_width() / 2, screen.window_height() / 2
screen.setworldcoordinates(-width, height, width, -height)

maze_drawer = Turtle(visible=False)
maze_drawer.color("purple")
maze_drawer.speed("fastest")

# draw simplified maze
wall_len = 0

for _ in range(20):
    maze_drawer.left(90)
    wall_len += PATH_WIDTH
    maze_drawer.forward(wall_len)

# navigate maze from center
maze_runner = Turtle()
maze_runner.color("dark green", "green")
maze_runner.penup()
maze_runner.goto(-PATH_WIDTH, -PATH_WIDTH)

def run_maze():
    maze_runner.forward(1)

    x, y = maze_runner.position()
    color_at_turtle = get_pixel_color(x, y)

    if color_at_turtle == "purple":
        maze_runner.backward(PATH_WIDTH - 1)
        maze_runner.left(90)
        x, y = maze_runner.position()

    if -width < x < width and -height < y < height:
        screen.ontimer(run_maze, 10)

run_maze()

screen.exitonclick()