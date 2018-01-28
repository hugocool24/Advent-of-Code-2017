
factorA = 16807
factorB = 48271
startA = 516
startB = 190
div_factor = 2147483647
#startA = 65
#startB = 8921

def generatorA(start,factor):
    previous_value = start
    while True:
        new_value = factor*previous_value % div_factor
        previous_value = new_value
        if new_value % 4 == 0:
            yield new_value

def generatorB(start,factor):
    previous_value = start
    while True:
        new_value = factor*previous_value % div_factor
        previous_value = new_value
        if new_value % 8 == 0:
            yield new_value


A = generatorA(startA,factorA)
B = generatorB(startB,factorB)

counter = 0
part1 = 0
while counter <= 5e6:
    a = next(A)
    a = format(a,'016b')
    if len(a)>16:
        a = a[len(a)-16:]
    b = next(B)
    b = format(b,'016b')
    if len(b)>16:
        b = b[len(b)-16:]
    if a == b:
        part1 += 1
    counter += 1
print(part1)
