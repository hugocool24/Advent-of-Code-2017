puzzle_input = 349
#puzzle_input = 3

def spinlock(step_size: int, pos: int, state: list,number: int):
    pos = (pos + step_size) % len(state)
    state.insert(pos,number)
    pos += 1
    return state, pos
algo = [0]
pos = 0
print("{",algo,"}", "POS: ",pos)
for x in range(1,2018):
    algo, pos = spinlock(puzzle_input,pos,algo,x)
    print(algo[pos-3:pos+3])


def second_spot(step_size, number):
    length = 1
    pos = 0
    second = None
    for i in range(1, number + 1):
        pos = (pos + step_size) % length

        if pos == 0:
            second = i

        length += 1
        pos = (pos + 1) % length

        if i % 1_000_000 == 0:
            print(i)
    return second

print(second_spot(puzzle_input,50_000_000))
