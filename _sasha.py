def calculator(input_string):
    return no_scope_calculator(list(map(map_light_int, input_string.split())))


def map_light_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        return input_string


def no_scope_calculator(main_list):
    symbol_index = 0
    while main_list[symbol_index] != '+':
        while main_list[symbol_index] != '-':
            if symbol_index + 1 == len(main_list):
                return multiply_calculator(main_list)
            symbol_index += 1
            continue
        return multiply_calculator(main_list[0:symbol_index]) - no_scope_calculator(main_list[symbol_index + 1:])
    return multiply_calculator(main_list[0:symbol_index]) + no_scope_calculator(main_list[symbol_index + 1:])


def multiply_calculator(no_pluses_list):
    multiply_result = no_pluses_list[0]
    for symbol_index in range(1, len(no_pluses_list), 2):
        if no_pluses_list[symbol_index] == '*':
            multiply_result *= no_pluses_list[symbol_index + 1]
        elif no_pluses_list[symbol_index] == '/':
            multiply_result /= no_pluses_list[symbol_index + 1]
    return multiply_result
