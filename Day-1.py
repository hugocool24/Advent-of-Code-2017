
num = 0
x = list(map(int, str(num)) )

def test(x):
    add_list = []
    for i in range(len(x)):
        if i == len(x)-1:
            if(x[i]==x[0]):
                add_list.append(x[i])
                return add_list
            else:
                return add_list
        if x[i] == x[i+1]:
            add_list.append(x[i])
    return add_list
print(sum(test(x)))
