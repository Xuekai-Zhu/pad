def solution():
    # Define the fraction of students that like each subject
    math_fraction = 1/5
    english_fraction = 1/3
    science_fraction = 1/7

    # Calculate the number of students that like each subject
    math_students = math_fraction * 30
    english_students = english_fraction * 30

    # Calculate the remaining students
    remaining_students = 30 - math_students - english_students

    # Calculate the number of students that like Science
    science_students = remaining_students * science_fraction

    # Calculate the number of students that don't have a favorite subject
    no_favorite_students = 30 - math_students - english_students - science_students
    result = no_favorite_students
    return result

print(solution())