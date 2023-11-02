def solution():
    total_students = 15 + 10  # There are 15 girls and 10 boys in the class
    books_per_student = 375 / total_students  # The books are divided equally among all students

    # Calculate the number of books all the girls combined received
    books_for_girls = 15 * books_per_student
    result = books_for_girls
    return result

print(solution())