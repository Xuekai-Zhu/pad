def solution():
    # Calculate the number of students who like Math and English
    math_students = 30 * 1/5
    english_students = 30 * 1/3
    total_math_and_english = math_students + english_students

    # Calculate the remaining number of students
    remaining_students = 30 - total_math_and_english

    # Calculate the number of students who like Science
    science_students = remaining_students * 1/7

    # Calculate the number of students without a favorite subject
    no_favorite_subject = 30 - (math_students + english_students + science_students)
    result = no_favorite_subject
    return result

print(solution())