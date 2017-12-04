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
