grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}

students=sorted(students)
estimation= (sum(grades[0])/len(grades[0]),
             sum(grades[1])/len(grades[1]),
             sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),
             sum(grades[4])/len(grades[4]))

a= {students[0]: estimation[0],
    students[1]: estimation[1],
    students[2]: estimation[2],
    students[3]: estimation[3],
    students[4]: estimation[4]}
print('Годовая аттестация', a)