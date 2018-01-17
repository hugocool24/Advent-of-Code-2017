from math import sqrt
with open('input_day11.txt','r') as myfile:
    path=myfile.read().replace('\n','')
path = list(map(str, path.split(',')))

x,y,z = 0,0,0
dist = []
for i in path:
    if i == 'n':
        y += 1
        z -= 1
    elif i == 'ne':
        x += 1
        z -= 1
    elif i == 'se':
        x += 1
        y -= 1
    elif i == 's':
        y -= 1
        z += 1
    elif i == 'sw':
        x -= 1
        z += 1
    elif i == 'nw':
        x -= 1
        y += 1
    dist.append((abs(x)+abs(y)+abs(z))/2)
print ((abs(x) + abs(y) + abs(z)) / 2)
print(max(dist))
