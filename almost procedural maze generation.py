import turtle
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Maze")
wn.setup(400, 400)

maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.penup()
maze_turtle.goto(-190, -190)
maze_turtle.pendown()

rows = 10
cols = 10
cell_size = 20

maze = [[0] * cols for _ in range(rows)]

def draw_filled_square():
    maze_turtle.begin_fill()
    for _ in range(4):
        maze_turtle.forward(20)
        maze_turtle.left(90)
    maze_turtle.end_fill()

def is_in_bounds(x, y):
    return 0 <= x < cols and 0 <= y < rows

def generate_maze(x, y, counter, max_count):
    if counter >= max_count:
        return

    maze[y][x] = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if is_in_bounds(new_x, new_y) and maze[new_y][new_x] == 0:
            maze_turtle.penup()
            maze_turtle.goto((new_x - cols / 2) * cell_size, (rows / 2 - new_y) * cell_size)
            maze_turtle.pendown()
            draw_filled_square()
            generate_maze(new_x, new_y, counter + 1, max_count)

max_cells = rows * cols // 2

generate_maze(0, 0, 0, max_cells)

maze_turtle.hideturtle()
wn.update()
wn.exitonclick()
