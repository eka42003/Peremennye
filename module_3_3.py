def print_params(a = 1, b = 'строка', c = True):
    return a, b, c
values_list = [False, 'Chucho', 24]
values_dict = {'a': 'Paco', 'b': 'Chucho', 'c': 'Pepe'}
values_list2 = [True, 'True']

print(print_params())
print(*print_params())
print(print_params(b=25))
print(print_params(c = [1, 2, 3]))
print(*print_params(c = [1, 2, 3]))
print(print_params(*values_list))
print(print_params(**values_dict))
print(print_params(*values_list2, 42))
print(*print_params(*values_list2, 42))