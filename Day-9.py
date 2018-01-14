filename = 'input_day9.txt'
f = open(filename,'rt')

for flood in f:
    flood = list(map(str, flood.split()))

flood = flood[0]

def score(string):
    puzzle_score = 0
    flag = False
    s = 0
    depth = 0
    canc = 0
    while True:
        if s >= len(string):
            break
        if string[s] == "!":
            s += 1
        elif flag:
            if string[s] == ">":
                flag = False
            else:
                canc += 1
        elif string[s] == "{":
            depth += 1
            puzzle_score += depth
        elif string[s] =="<":
            flag = True
        elif string[s] == "}":
            depth -= 1
        s += 1
    return puzzle_score,canc


result = score(flood)

print(result)
