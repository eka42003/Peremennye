
def parol(a):
    result = []
    for i in range(1,21):
        for j in range(i,21):
            if i == j:
                pass
            elif a % (i + j) == 0:
                result = result + [i,j] # добавляем один список к другому

    result = ''.join(map(str, result)) # превращаем каждый элемент
    # списка в строку и объединяем список в одну строку без пробелов
    return result

print(parol(3))
print(parol(4))
print(parol(5))
print(parol(9))
print(parol(11))
print(parol(19))