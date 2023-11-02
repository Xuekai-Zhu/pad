def solution():
    num_students = 30
    math_students = num_students / 5
    english_students = num_students / 3
    remaining_students = num_students - math_students - english_students
    science_students = remaining_students / 7
    no_favorite = num_students - math_students - english_students - science_students
    result = no_favorite
    return result

print(solution())