Last_Name = str(input('please enter your last name: '))
First_Name = str(input('please enter your first name: '))
Age = int(input('please input your age: '))
Grade_1 = float(input('please input your first grade: '))
Grade_2 = float(input('please input your second grade: '))
Grade_3 = float(input('please input your third grade: '))
Average_Grade = str(round(((Grade_1 + Grade_2 + Grade_3)/3), 2))
print(Last_Name + ', ' + First_Name + ' Age: ' + str(Age) + ' Average Grade: ' +
Average_Grade)

