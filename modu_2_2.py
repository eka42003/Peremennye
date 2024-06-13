first = int(input("Введите любое число и нажмите enter: "))
second = int(input("Введите любое число и нажмите enter: "))
third = int(input("Введите любое числои нажмите enter: "))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
