#Part-1
num = 289326
i = 1
while i*i < num:
    i+=2
length_side = i
test = [i*i - k*(i-1) for k in range(4)]
for p in test:
    dist = abs(p-num)
    if dist <= (i-1)//2:
        print(i-1-dist)
        break
#Part-2

coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
num2 = 289326
def part2(goal):
    x = y = dx = 0
    dy = -1
    grid = {}
    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if(x+ox, y+oy) in grid:
                total += grid[(x+ox, y+oy)]
        if total > int(goal):
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
print(part2(num2))
