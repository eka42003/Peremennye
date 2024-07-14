def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'

    print(inner_function())

test_function()

# print(inner_function()) Тут ошшибка, поскольку  inner_function вызывается
# только изнутри test_function.
