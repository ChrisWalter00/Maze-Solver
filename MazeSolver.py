from turtle import *
from PIL import Image

BLACK = (0, 0, 0, 255)

def solveMaze(maze):
    img = Image.open(maze)
    image_width, image_height = img.size

    setup(image_width * 2, image_height * 2)
    bgcolor('white')
    title("Maze Solver")
    bgpic(maze)
    pencolor("red")
    turtlesize(1) # size of turtle (easier for some kids to see)
    pensize(2)
    
    penup()
    goto(0, image_height / 2)
    setheading(0)
    

    inPlace = False
    
    while inPlace == False:
        forward(1)
        x, y = position()
        color = getPixelColor(x, y, img, image_width, image_height)
        if color == BLACK:
            undo()
            right(90)
            inPlace = True
    
    pendown()
    
    unSolved = True
    
    
    while unSolved:
        x, y = position()
        color = getPixelColor(x, y, img, image_width, image_height)
        #print(color)
        leftWall = checkLeft(x, y, heading(), img, image_width, image_height)
        if leftWall == BLACK:
            forward(1)
        else:
            left(90)
            forward(1)
           
        if color == BLACK:
            undo()
            right(90)
            forward(1)

                
        if(y <= -1 * (image_height / 2)):
            unSolved = False
        
    done()
    
def checkLeft(x, y, heading, img, width, height):
    # Calculate the coordinates of the point to the left of the turtle
    if heading == 0:  # Facing right
        left_x = x
        left_y = y + 1
    elif heading == 90:  # Facing up
        left_x = x - 1
        left_y = y
    elif heading == 180:  # Facing left
        left_x = x
        left_y = y - 1
    elif heading == 270:  # Facing down
        left_x = x + 1
        left_y = y

    color = getPixelColor(left_x, left_y, img, width, height)
    return color

def getPixelColor(x, y, img, width, height):
    # Get current turtle coordinates
    
    # Convert Turtle X (-Width/2 to Width/2) to Pixel X (0 to Width)
    pixel_x = int(x + (width / 2))
    
    # Convert Turtle Y (-Height/2 to Height/2) to Pixel Y (0 to Height, inverted)
    pixel_y = int((height / 2) - y)
    
    # Ensure coordinates stay within image boundaries
    if 0 <= pixel_x < width and 0 <= pixel_y < height:
        # Returns an (R, G, B) tuple or an integer palette index depending on the image type
        return img.getpixel((pixel_x, pixel_y))
    else:
        return None

if __name__ == "__main__":
    #filename = input("Enter the filename of the maze: ")
    filename = "maze2.png"
    solveMaze(filename)