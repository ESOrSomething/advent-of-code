import copy
f = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

lines = f.splitlines()
initGrid = []
for i in range(len(lines)):
    initGrid.append([])
    for j in range(len(lines[0])):
        initGrid[i].append(lines[i][j])

initH = 0
initV = 0

print(initGrid)
for line in range(0, len(initGrid)):
        for column in range(0, len(initGrid[line])):
            if initGrid[line][column] == "^":
                initH = column
                initV = line
                initGrid[line][column] = "X"

def test(gridToTest, horizontal, vertical):
    global initH
    global initV
    h = initH
    v = initV
    direction = "up"
    patrol = True
    seen = set()
    grid = copy.deepcopy(gridToTest)
    print(horizontal)
    print(vertical)
    print(grid)
    grid[horizontal][vertical] = "#"
    while patrol == True:
        if (direction, h, v) in seen:
            return True
       
        seen.add((direction, h, v))
        if direction == "up":
            v -= 1
        if direction == "down":
            v += 1
        if direction == "left":
            h -= 1
        if direction == "right":
            h += 1
        if direction == "up":
            if v == 0:
                return False
            else:
                if grid[v-1][h] == "#":
                    direction = "right"
        elif direction == "down":
            if v == len(grid) - 1:
                return False
            else:
                if grid[v+1][h] == "#":
                    direction = "left"
        elif direction == "right":
            if h == len(grid[0]) - 1:
                return False
            else:
                if grid[v][h+1] == "#":
                    direction = "down"
        elif direction == "left":
            if h == 0:
                return False
            else:
                if grid[v][h-1] == "#":
                    direction = "up"

count = 0

for i in range(0, len(initGrid)):
    for j in range(0, len(initGrid[0])):
        if test(initGrid, j, i):
            count += 1
            print(count)
print(count)
