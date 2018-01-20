
import time
f = open('input_day12.txt','rt')
#f = open('test_day12.txt','rt')
pipes = []
for line in f:
    line = list(map(str, line.split()))
    line = list(map(lambda each:each.strip(","), line))
    pipes.append(line)


def check_group(number,pipes):
    try:
        connections = {pipes[number][0]}
    except:

        return False
    counter = 0
    while True:
        for lines in pipes:
            for x in lines:
                if x in connections:
                    connections.add(lines[0])
                    for x in lines[2:]:
                        connections.add(x)
        if counter == len(connections):
            return connections
        else:
            counter = len(connections)

connections = check_group(0,pipes)
print("Part 1: ",len(connections))

def update_pipes(connections,pipes):
    for x in connections:
        for y in pipes:
            if x == y[0]:
                pipes.remove(y)
    return pipes

group_counter = 0
while len(pipes) != 0:
    for programs in range(0,2000):
        connections = check_group(programs,pipes)
        if not connections:
            pass
        else:
            group_counter += 1
            update_pipes(connections,pipes)

print("Part 2: ",group_counter)
