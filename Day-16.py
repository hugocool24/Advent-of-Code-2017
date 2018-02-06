dance = open('input_day16.txt').read().strip().split(',')
programs = list("abcdefghijklmnop")


# programs = ["a","b","c","d","e"]
# dance = ["s1","x3/4","pe/b"]
def spin(programs: object, x: object) -> object:
    programs = programs[-x:] + programs[:-x]
    return programs


def exchange(programs, i, j):
    a = programs[i]
    b = programs[j]
    programs[i] = b
    programs[j] = a
    return programs


def partner(programs, i, j):
    a = programs.index(i)
    b = programs.index(j)
    programs = exchange(programs, a, b)
    return programs


counter = 0


def day16(reps, programs):
    seen = []
    for i in range(reps):
        s = "".join(programs)
        if s in seen:
            print(seen[reps % i])
            return
        seen.append(s)

        for x in dance:
            if x[0] == "s":
                s = int(x[1:])
                programs = spin(programs, s)
            elif x[0] == "x":
                i, j = map(int, x[1:].split('/'))
                programs = exchange(programs, i, j)
            elif x[0] == "p":
                a, b = x[1:].split('/')
                programs = partner(programs, a, b)
    print(''.join(programs))  # if no cycle - part 1


day16(1, programs[:])
day16(int(1e9), programs[:])

progs = list("abcdefghijklmnop")
f = open('input_day16.txt').read().strip().split(',')
