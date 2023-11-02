def solution():
     students_at_tables = 3 * 6
     students_went_to_bathroom = 3
     students_went_to_canteen = students_went_to_bathroom * 3
     students_in_groups = 2 * 4
     students_from_germany = 3
     students_from_france = 3
     students_from_norway = 3
     total_students = students_at_tables + students_went_to_bathroom + students_went_to_canteen + students_in_groups + students_from_germany + students_from_france + students_from_norway
     result = total_students
     return result

print(solution())