def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_word.lower():
            same_words.append(i)
        else:
            continue
    return same_words

print(single_root_words('кот', 'Котёнок', 'киска', 'коТорый', 'котёл', 'сКОТина', 'ко','скоТный'))
print(single_root_words("кис", "Кисть", "Прокисший", "Прогорклый", "КИСет", "сетка"))
