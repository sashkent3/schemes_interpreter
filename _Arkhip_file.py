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


def organisation(input_list):
    # print(input_list, len(input_list), 'organisation')
    if input_list[0] == '+':
        input_list = input_list[1:]
    elif input_list[0] == '-':
        input_list[1] = '-' + input_list[1]
        input_list = input_list[1:]

    if len(input_list) == 1:
        return int(input_list[0])

    for index in range(len(input_list) - 2, 0, - 2):
        # print(index, input_list[index])
        # слева направо
        if input_list[index] == '+':
            return organisation(input_list[index + 1:]) + organisation(input_list[:index])
        elif input_list[index] == '-':
            return - organisation(input_list[index + 1:]) + organisation(input_list[:index])

    return multiply_operation(input_list)


s = str(input())
s = s.split(' ')
print(organisation(s))
