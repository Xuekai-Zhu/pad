def solution():
    """In a class of 30 students, the teacher polls the students on their favorite subject. 1/5 of the students like Math, and 1/3 like English. 1/7 of the remaining students like Science. The rest don’t have a favorite subject. How many students don’t have a favorite subject?"""
    total_students = 30
    math_students = total_students // 5
    english_students = total_students // 3
    remaining_students = total_students - math_students - english_students
    science_students = remaining_students // 7
    no_favorite_subject_students = total_students - math_students - english_students - science_students
    result = no_favorite_subject_students
    return result

print(solution())