from turtle import *

def solveMaze(maze, height, width):
    setup(height * 50, width * 50)
    bgcolor('white')
    title("Maze Solver")
    bgpic(maze)
    color("red") # Colour line
    turtlesize(1) # size of turtle (easier for some kids to see)
    pensize(2)
    
    penup()
    goto(0,height * 10)
    pendown()

    canvas = getcanvas()
    unSolved = True

    while unSolved:
        pass
    done()
    

if __name__ == "__main__":
    filename = input("Enter the filename of the maze: ")
    solveMaze(filename, 5, 5)