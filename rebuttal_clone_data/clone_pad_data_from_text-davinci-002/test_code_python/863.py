def solution():
    total_students = 25
    students_liking_fries = 15
    students_liking_burgers = 10
    students_liking_both = 6
    students_liking_neither = total_students - (students_liking_fries + students_liking_burgers + students_liking_both)
    result = students_liking_neither
    return result

print(solution())