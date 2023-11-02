def solution():
     
     students_in_class = 40
     absent_students = students_in_class / 10
     present_students = students_in_class - absent_students
     students_in_classroom = present_students * (3/4)
     students_in_canteen = present_students - students_in_classroom
     result = students_in_canteen
     return result

print(solution())