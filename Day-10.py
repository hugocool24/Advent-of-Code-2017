filename = 'input_day10.txt'
f = open(filename,'rt')
for line in f:
    input_length = list(map(int, line.split(',')))

circ = [x for x in range(0,256)]

#input_length = [3,4,1,5]
#circ = [0,1,2,3,4]
skip = 0
pos = 0
for ip in input_length:
    if pos+ip>=len(circ):
        placeholder = circ[0:(pos+ip)%len(circ)]
        placeholder.reverse()
        placeholder2 = circ[(pos)%len(circ):]
        placeholder3 = circ[(pos+ip)%len(circ):(pos)%len(circ)]
        placeholder2.reverse()
        circ = placeholder2 + placeholder3 + placeholder
        if ip==len(circ):
            placeholder2.reverse()
            placeholder.reverse()
            placeholder3 = placeholder2 + placeholder
            placeholder3.reverse()
            #print(placeholder3[len(circ)-(pos%len(circ)):])
            circ = placeholder3[len(circ)-pos%len(circ):] + placeholder3[0:len(circ)-pos%len(circ)]
    else:
        placeholder = circ[pos%len(circ):(pos+ip)%len(circ)]
        placeholder2 =circ[:pos%len(circ)]
        placeholder3 = circ[(pos+ip)%len(circ):]
        placeholder.reverse()
        circ = placeholder2 + placeholder + placeholder3
    pos = (pos + ip + skip)%len(circ)
    skip += 1
    #print(len(circ))
print(circ[0]*circ[1])

for line in f:
    input_length = list(map(int, line.split(',')))

circ = [x for x in range(0,256)]

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

m = k([int(x) for x in input_length])
print(m[0] * m[1])

data = input().strip()

m = k(list(data.encode()) + [17, 31, 73, 47, 23], 64)
print(m)
o = ''
for i in range(0, 256, 16):
    x = 0
    for j in range(16):
        x ^= m[i+j]
    o += '%02x' % x
print(o)
