def solution():
    number_of_students = 10
    art_kits = 20
    students_per_kit = 2
    students_who_make_three = number_of_students / 2
    students_who_make_four = number_of_students / 2
    works_created = (students_who_make_three * 3) + (students_who_make_four * 4)
    result = works_created
    return result

print(solution())