import random

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
# print(new_list)

range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
names_list = [name for name in names if len(name) == 4]
# print(names_list)
uppercase_list = [name.upper() for name in names if len(name) > 5]
# print(uppercase_list)

student_scores = {student: random.randint(0, 100) for student in names}
# print(student_scores)

passed_students = {student: score for (
    student, score) in student_scores.items() if score >= 60}
# print(passed_students)
