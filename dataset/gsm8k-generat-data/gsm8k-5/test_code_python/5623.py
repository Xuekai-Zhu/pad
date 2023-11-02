def solution():
    # Number of students who like Math
    math_students = 30 * (1/5)

    # Number of students who like English
    english_students = 30 * (1/3)

    # Number of students who don't like Math or English
    remaining_students = 30 - math_students - english_students

    # Number of students who like Science
    science_students = remaining_students * (1/7)

    # Number of students who don't have a favorite subject
    no_favorite_subject = 30 - math_students - english_students - science_students

    result = no_favorite_subject
    return result

print(solution())