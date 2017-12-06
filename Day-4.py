
#Part 1
filename = 'input_day4.txt'
f = open(filename,'rt')
result = 0
passphrase = []
for line in f:
    line = list(map(str, line.split()))
    passphrase.append(line)

for check in passphrase:
    unique_pass = True
    counter = 0
    check2 = list(check)
    for word in check:
        try:
            check2.remove(word)
        except:
            pass
        if word in check2:
            unique_pass = False
    if unique_pass == True:
        result += 1
print(result)
#Part 2
#Part 1
filename = 'input_day4-2.txt'
f = open(filename,'rt')
result = 0
passphrase = []
for line in f:
    line = list(map(str, line.split()))
    passphrase.append(line)

def alphabet_words(list_to_sort):
    new_list = []
    for words in list_to_sort:
        words = ''.join(sorted(words))
        new_list.append(words)
    return new_list


for check in passphrase:
    unique_pass = True
    counter = 0
    check = alphabet_words(check)
    check2 = list(check)
    for word in check:
        try:
            check2.remove(word)
        except:
            pass
        if word in check2:
            unique_pass = False
    if unique_pass == True:
        result += 1
print(result)
