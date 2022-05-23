# 40. Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
#           Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций.
#           Пример: 1+2*3 => 7; (1+2)*3 => 9;

output_str = '-1+6/(3*2)+(1+2)*3'
print(f'Выражение: {output_str}')


def math_expr(init_str):
    while '*' in init_str:
        i = init_str.index('*')
        temp = str(int(init_str[i-1]) * int(init_str[i+1]))
        init_str = init_str[:(i-1)] + temp + init_str[(i+2):]
    while '/' in init_str:
        i = init_str.index('/')
        temp = str(int(init_str[i-1]) // int(init_str[i+1]))
        init_str = init_str[:(i-1)] + temp + init_str[(i+2):]
    init_str = ''.join([i if i != '-' else '+-' for i in init_str])
    return sum([int(i) for i in init_str.split('+') if i != ''])


while '(' in output_str:
    left_bracket = output_str.index('(')
    right_bracket = output_str.index(')')
    temp_expression = output_str[left_bracket+1:right_bracket]
    temp = math_expr(temp_expression)
    output_str = output_str[:(left_bracket)] + \
        str(temp) + output_str[(right_bracket+1):]

print(f'result -> {math_expr(output_str)}')
