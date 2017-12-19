import time
filename = 'input_day6.txt'
f = open(filename,'rt')
blocks = []
for line in f:
    line = list(map(int, line.split("\t")))
    blocks.append(line)
blocks = blocks[0]

#blocks = [0,2,7,0]


placeholder = []
length = len(blocks)
counter = 0
counter2 = 0
condition = False
checker = 0
blocks = [0,2,7,0]
while checker == 0:
    max_value = max(blocks)
    max_index = blocks.index(max_value)
    blocks[max_index] = 0
    start = max_index+1
    for i in range(max_value):

        if start<len(blocks):
            blocks[start] = blocks[start]+1
            start += 1
        else:
            start = 0
            blocks[start] = blocks[start]+1
            start += 1
    if condition != True:
        for i in placeholder:
            if str(i) == str(blocks):
                counter +=1
                print(counter)
                condition = True
                placeholder = []
                break
    if(condition):
        for i in placeholder:
            if str(i) == str(blocks):
                print("Solution for part 2 below")
                print(counter2)
                checker = 1
                break

    placeholder.append(list(blocks))
    counter += 1
    if condition:
        counter2 += 1
