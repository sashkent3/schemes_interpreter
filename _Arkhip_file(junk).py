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
