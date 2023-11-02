def solution():
    # Calculate the total number of students in the class
    total_students = 15 + 10

    # Calculate the number of books each student received
    books_per_student = 375 / total_students

    # Calculate the number of books all the girls got combined
    books_for_girls = books_per_student * 15

    result = books_for_girls
    return result

print(solution())