filename = 'input_day8.txt'
f = open(filename,'rt')
register = []
for line in f:
    line = list(map(str, line.split()))
    register.append(line)

variables = {}
global_highest_variable = 0


def operator_converter(first_value, operator,last_value):
    last_value = int(last_value)
    #print(first_value)
    if not first_value in variables:
        variables[first_value] = 0

        #print(variables[first_value])
    if operator == ">":
        return variables[first_value]>last_value
    elif operator == '<':
        return variables[first_value]<last_value
    elif operator == "<=":
        return variables[first_value]<=last_value
    elif operator == ">=":
        return variables[first_value]>=last_value
    elif operator == "==":
        return variables[first_value]==last_value
    elif operator == "!=":
        return variables[first_value] != last_value
    elif operator == "inc":
        variables[first_value] = variables[first_value] + last_value
    elif operator == "dec":
         variables[first_value] = variables[first_value] - last_value


for operations in register:
    if operator_converter(operations[4],operations[5],operations[6]):
        operator_converter(operations[0],operations[1],operations[2])
        if variables[operations[0]] > global_highest_variable:
            global_highest_variable = variables[operations[0]]
    #print(variables)



print(max(variables.values()))
print(global_highest_variable)
