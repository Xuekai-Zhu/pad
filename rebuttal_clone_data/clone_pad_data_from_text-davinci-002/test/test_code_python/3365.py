def solution():
     number_of_students_in_sixth_level_math_class = 40
     number_of_students_in_fourth_level_math_class = number_of_students_in_sixth_level_math_class * 4
     number_of_students_in_seventh_level_math_class = number_of_students_in_fourth_level_math_class * 2
     total_number_of_students = number_of_students_in_sixth_level_math_class + number_of_students_in_fourth_level_math_class + number_of_students_in_seventh_level_math_class
     result = total_number_of_students
     return result

print(solution())