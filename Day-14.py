
string = "hxtvlmkl-"
#string = "flqrgnkx-"

def hash(puzzle):
    m = k(list(puzzle.encode()) + [17, 31, 73, 47, 23], 64)
    o = ''
    for i in range(0, 256, 16):
        x = 0
        for j in range(16):
            x ^= m[i+j]
        o += '%02x' % x
    return o


def k(d, r=1):
    m, p, s = list(range(256)), 0, 0
    #m =  [0,1,2,3,4]
    #d = [3,4,1,5]
    for _ in range(r):
        for i in d:
            for o in range(i//2):
                a, b = (p+o) % len(m), (p+i-o-1) % len(m)
                m[a], m[b] = m[b], m[a]
            p += i + s
            s += 1
    return m

def free_space(knot):
    used = 0
    free = 0
    knot = bin(int(knot,16))
    knot = knot[2:]
    knot = knot.zfill(128)
    knot = list(knot)
    for x in knot:
        if x == "1":
            used += 1
    free = 128 - used
    return used,free, knot

used = 0
free = 0
regions = []
grids = []
for x in range(0,128):
    string2 = string + str(x)
    string2 = hash(string2)
    a, b, grid = free_space(string2)
    grids.append(grid)
    used += a
    free += b

print("Free: ",free)
print("Used: ",used)

def del_region(grid,i,j):
    num_rows = len(grid)
    num_cols = len(grid[0])

    if i<0 or i>= num_rows or j < 0 or j >= num_cols:
        #outside
        return
    elif grid[i][j] == "0":
        return
    else:
        grid[i][j] = "0"
        del_region(grid, i+1, j)
        del_region(grid, i-1, j)
        del_region(grid, i, j+1)
        del_region(grid, i, j-1)
part2 = 0
for i, row in enumerate(grids):
    for j, c in enumerate(row):
        if c == "1":
            part2 += 1
            del_region(grids, i, j)
print("Part 2: ",part2)
