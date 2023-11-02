def solution():
    # Calculate the number of girls in Ms. Smith's class
    num_girls = 15

    # Find the total number of students in Ms. Smith's class
    total_students = num_girls + 10

    # Divide the total number of books equally among all the students
    num_books_each = 375 / total_students

    # Calculate the total number of books all the girls got combined
    num_books_girls = num_books_each * num_girls

    result = num_books_girls
    return result

print(solution())