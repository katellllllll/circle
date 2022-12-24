import math
import os



width, height = 40, 40
k = 2  # good value is 1-2


def draw(a,b,r):
    map = [['.' for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            if abs((x-a)**2 + (y-b)**2 - r**2) <= k**2:
                map[y][x] = '#'

    for line in map:
        print(" ".join(line))

os.system("mode con cols=110 lines=40")
print("the field is", width,"x", height,"range")
print("good values for x and y are in [15,30] and for d(must be odd) in [20,35]")

a = int(input("input ur values\nx = "))
b = int(input("y = "))
d = int(input("(must be odd) d = "))

if (d % 2 != 0):
    r = math.floor(d / 2)
    if (r > a or r > b or (r + a) > width or (r + b) > height):
        print("bad input dude")
    else:
        os.system('cls')
        draw(a,b,r)