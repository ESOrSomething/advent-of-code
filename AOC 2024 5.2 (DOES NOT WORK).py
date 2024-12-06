f = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n\n")

rules = f[0].splitlines()
pages = f[1].splitlines()

ruleListA = []
ruleListB = []

for i in rules:
    ruleListA.append(i.split("|")[0])
    ruleListB.append(i.split("|")[1])

print(ruleListA)
print(ruleListB)
print(pages)

count = 0

incorrectLines = []

def test(line):
    pageList = []
    active = True
    for number in pages[line].split(","):
        pageList.append(number)
    valid = True
    for ruleNum in range(0, len(ruleListA)):
        if ruleListA[ruleNum] in pageList and ruleListB[ruleNum] in pageList:
            if pageList.index(ruleListA[ruleNum]) > pageList.index(ruleListB[ruleNum]):
                valid = False
                incorrectLines.append(pages[line])
                return -1
    if valid == True:
        return pageList[len(pageList) // 2]

for i in range(0, len(pages)):
    if test(i) != -1:
        count += int(test(i))
print(count)
print(incorrectLines)

correctOrder = []

listLock = False

print("incorrect")
print(incorrectLines)

graph = {}

print(ruleListB)

for i in range(0, len(ruleListA)):
    graph[ruleListB[i]] = []
    graph[ruleListA[i]] = []
for i in range(0, len(ruleListB)):
    graph[ruleListB[i]].append(ruleListA[i])

print(graph)
orderList = []
while graph:
  for i in graph:
      if graph[i] == []:
          num = i
          orderList.append(i)
  for i in graph:
      for j in graph[i]:
          if graph[i][graph[i].index(j)] == num:
              graph[i].remove(num)
  del graph[num]

global count2
count2 = 0

def check(order, line):
   orderToPrint = [x for x in order if x in line]
   return orderToPrint[len(orderToPrint) // 2]

for i in incorrectLines:
    count2 += int(check(orderList, i))
    
print(count2)
