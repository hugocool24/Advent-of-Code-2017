filename = 'input_day2.txt'
f = open(filename,'rt')
results = []
for line in f:
    line = list(map(int, line.split()))
    results.append(line)
tot_diff = 0
for line in results:
    maximum = max(line)
    minimum = min(line)
    tot_diff += maximum-minimum
print (tot_diff)

y = 0
line = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]

def tester(matrix,number,memory):
    for x in matrix[number]:
        placeholder = list(matrix[number])
        placeholder.remove(x)
        for y in placeholder:
            try:
                if x%y == 0:
                    memory += x/y
            except:
                pass
    if number > 0:
        return tester(matrix,number-1,memory)
    else:
        return memory

print(tester(results,len(results)-1,0))
