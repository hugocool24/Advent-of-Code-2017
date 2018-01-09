filename = 'input_day7.txt'
f = open(filename,'rt')
tower = []
for line in f:
    line = list(map(str, line.split()))
    placeholder = ""
    for weight in line[1]:
        if weight.isdigit():
            placeholder = placeholder + weight
    line[1]=int(placeholder)
    tower.append(line)

#Find the tower with the lowest weight.
tower_updated = []

for line in tower:
    placeholder = []
    for x in line:
        try:
            x = x.replace(",","")
        except:
            pass
        placeholder.append(x)
    tower_updated.append(placeholder)

def first_tree(tower_updated):
    for program in tower_updated:
        checker = False
        for child in tower_updated:
            for x in range(3,len(child)):
                if program[0] == child[x]:
                    checker = True
        if checker == False:
            print(program)
            legs = program[3:]
            return(legs)

legs = first_tree(tower_updated)
# Part 2

def find_weight(prog, towerList, initWeight):
    weight = initWeight
    for child in towerList:
        if child[0] == prog:
            if len(child)==2:
                weight += child[1]
            else:
                weight += child[1]
                for x in child[3:]:
                    weight = find_weight(x,towerList,weight)
    return weight

leg_weight = []
for x in legs:
    weights = find_weight(x,tower_updated,0)
    leg_weight.append(weights)
for x in leg_weight:
    if leg_weight.count(x)==1:
        bad_leg_index = leg_weight.index(x)
    else:
        correctWeight=x

def weightChecker(weightsTester,nameList):
    for check in weightsTester:
        if weightsTester.count(check)==1:
            return nameList[weightsTester.index(check)]
    return False

def balance(BadProg,towerList,weight_mem):
    weight_memory = []
    child_memory = 0
    parent_memory = 0
    for child in towerList:
        if child[0] == BadProg:
            weight = child[1]
            child_memory = list(child[3:])
            parent_memory = list(child)
            for x in child[3:]:
                weight_memory.append(find_weight(x, towerList, 0))
    if weightChecker(weight_memory,child_memory) != False:
        balance(weightChecker(weight_memory,child_memory),towerList,weight_memory)
    else:
        odd = 0
        for check in weight_mem:
            if weight_mem.count(check)==1:
                odd = check
            else:
                correct = check
        if odd > correct:
            print(parent_memory[1]-abs(correct-odd))
        else:
            print(parent_memory[1]+abs(correct-odd))
balance(legs[bad_leg_index],tower_updated,0)
