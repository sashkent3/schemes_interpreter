def scope_balance(input_string):
    counter = 0
    for sym in input_string:
        if sym == '(':
            counter += 1
        elif sym == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True


def sum_operation(input_list):
    input_list[0] = int(input_list[0])
    for index in range(0, len(input_list) - 2, 2):
        input_list[index + 2] = int(input_list[index + 2])
        if input_list[index + 1] == '+':
            input_list[index + 2] += input_list[index]
        elif input_list[index + 1] == '-':
            input_list[index + 2] -= input_list[index]
        else:
            raise SyntaxError('')
    return input_list[len(input_list) - 1]


def multiply_operation(input_list):
    input_list[0] = int(input_list[0])
    for index in range(0, len(input_list) - 2, 2):
        input_list[index + 2] = int(input_list[index + 2])
        if input_list[index + 1] == '*':
            input_list[index + 2] *= input_list[index]
        elif input_list[index + 1] == '%':
            input_list[index + 2] = input_list[index] % input_list[index + 2]
        elif input_list[index + 1] == '/':
            input_list[index + 2] = input_list[index] / input_list[index + 2]
        elif input_list[index + 1] == '//':
            input_list[index + 2] = input_list[index] // input_list[index + 2]
        else:
            raise SyntaxError('')
    return input_list[len(input_list) - 1]


s = str(input())
s = s.split(' ')
print (multiply_operation(s))