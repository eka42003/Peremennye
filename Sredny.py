students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
for i in range(5):
    grades[i] = sum(grades[i]) / len(grades[i])
grudents = dict(zip(students, grades))
print(grudents)