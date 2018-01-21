import time
f = open('input_day13.txt','rt')
#f = open('test_day13.txt','rt')
firewall = []
for line in f:
    line = list(map(str, line.split()))
    line = list(map(lambda each:each.strip(":"), line))
    line = list(map(int,line))
    firewall.append(line)

scanner = [0]*(firewall[-1][0]+1)
scanner_movement = ['Down']*(firewall[-1][0]+1)
mover = -1

def move_scanner(firewall,scanner,scanner_movement):
    for x in firewall:
        if scanner_movement[x[0]] == 'Down':
            scanner[x[0]] += 1
        elif scanner_movement[x[0]] == 'Up':
            scanner[x[0]] += -1
        try:
            if x[1] == scanner[x[0]]:
                scanner_movement[x[0]] = 'Up'
            if scanner[x[0]] == 1:
                scanner_movement[x[0]] = 'Down'
        except:
            scanner[x] = 0
    return scanner, scanner_movement


def move_mover(mover,scanner,firewall):
    mover += 1
    if scanner[mover] == 1:
        for x in firewall:
            if x[0] == mover:
                return x[0]*x[1], mover, False
    else:
        return 0, mover, True

summer = []
penalty = 0
scanner, _ = move_scanner(firewall,scanner,scanner_movement)
scanner_movement = ['Down']*(firewall[-1][0]+1)

for x in range(0,firewall[-1][0]+1):
    penalty, mover, _ = move_mover(mover,scanner,firewall)
    summer.append(penalty)
    scanner, scanner_movement = move_scanner(firewall, scanner, scanner_movement)
print("Part 1:",sum(summer))

scanner = [0]*(firewall[-1][0]+1)
scanner_movement = ['Down']*(firewall[-1][0]+1)
scanner, _ = move_scanner(firewall,scanner,scanner_movement)
scanner_movement = ['Down']*(firewall[-1][0]+1)

mover = -1

delay = -1
original_scan = list(scanner)
original_scan_mover = list(scanner_movement)

while True:
    delay += 1
    mover = -1
    penalty = []
    win = True
    scanner,scanner_movement = move_scanner(firewall,original_scan,original_scan_mover)
    original_scan = list(scanner)
    original_scan_mover = list(scanner_movement)
    for x in range(0,firewall[-1][0]+1):
        score, mover, win = move_mover(mover,scanner,firewall)
        penalty.append(score)
        if win == False:
            break
        scanner, scanner_movement = move_scanner(firewall, scanner, scanner_movement)
    if delay%500000 ==0:
        print("yes")
        print(delay)
    if sum(penalty)==0 and win:
        print("Part 2:",(delay+1))
        break
