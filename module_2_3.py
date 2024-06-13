my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

poor = int (0)
while poor < len(my_list):
    if my_list[poor] > 0:
        print(my_list[poor])
        poor = poor + 1
        if my_list[poor] == 0:
            poor = poor+1
    else:
        break






