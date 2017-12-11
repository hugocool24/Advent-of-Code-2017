filename = 'input_day5.txt'
f = open(filename,'rt')
#Part 1
instructions = []
for i in f:
    i, _ =  i.split('\n')
    i = int(i)
    instructions.append(i)

#Part 1
finish = len(instructions)
agent = 0
steps = 0
placeholder = 0
while agent < finish and agent >= 0:
    if instructions[agent] == 0:
        instructions[agent] += 1
        steps += 1
    else:
        test = instructions[agent]
        placeholder = agent
        agent = agent + test
        instructions[placeholder] += 1
        steps += 1
print(steps)
#Part 2
filename = 'input_day5.txt'
f = open(filename,'rt')
instructions = []
for i in f:
    i, _ =  i.split('\n')
    i = int(i)
    instructions.append(i)
finish = len(instructions)
print(finish)
agent = 0
steps = 0
placeholder = 0
while agent < finish and agent >= 0:
    if instructions[agent] == 0:
        instructions[agent] += 1
        steps += 1
    elif(instructions[agent] >= 3):
        test = instructions[agent]
        placeholder = agent
        agent = agent + test
        instructions[placeholder] -= 1
        steps += 1
    else:
        test = instructions[agent]
        placeholder = agent
        agent = agent + test
        instructions[placeholder] += 1
        steps += 1
print(steps)
