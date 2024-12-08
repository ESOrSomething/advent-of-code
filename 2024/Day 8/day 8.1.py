data = open("data.txt", "r").read().splitlines()
import itertools

grid = []
dictionary = {}
for line in range(0, len(data)):
    grid.append([])
    columnNum = 0
    for column in data[line]:
        grid[line].append(data[line][columnNum])
        columnNum += 1

print(grid)

for line in range(0, len(grid)):
    columnNum = 0
    for column in grid[line]:
        if grid[line][columnNum] != ".":
            if grid[line][columnNum] in dictionary:
                dictionary[grid[line][columnNum]].append((columnNum, -line))
            else:
                dictionary[grid[line][columnNum]] = [(columnNum, -line)]
        columnNum += 1

count = 0
locations = []

for item in dictionary:
    for a, b in itertools.combinations(dictionary[item], 2):
        a1 = a[0] # horizontal a
        a2 = a[1] # vertical a
        b1 = b[0] # horizontal b
        b2 = b[1] # vertical b
        if a1 >= b1:
            temp1, temp2 = a1, a2
            a1, a2 = b1, b2
            b1, b2 = temp1, temp2
        slopeV = (b2 - a2)
        slopeH = (b1 - a1)
        print((a, b))
        print(slopeV)
        print(slopeH)
        print((b1, b2))
        print((a1, a2))
        if b2 + slopeV in range(0, -len(grid), -1) and b1 + slopeH in range(0, len(grid)):
            if (b1 + slopeH, b2 + slopeV) not in locations:
                locations.append((b1 + slopeH, b2 + slopeV))
        if a2 - slopeV in range(0, -len(grid), -1) and a1 - slopeH in range(0, len(grid)):
            if (a1 - slopeH, a2 - slopeV) not in locations:
                locations.append((a1 - slopeH, a2 - slopeV))

print(dictionary)
print(grid)
print("Answer: " + str(len(locations)))