def solution():
    """A school library has 120 books. Each student needs 5 books for their classes. The library was able to help 4 students on the first day of school, 5 students on the second day and 6 students on the third day. How many students can the library help out on the fourth day of school?"""
    # Define the number of books and students
    num_books = 120
    num_students_1 = 4
    num_students_2 = 5
    num_students_3 = 6

    # Calculate the number of books required for the first 3 days of school
    books_required = (num_students_1 + num_students_2 + num_students_3) * 5

    # Calculate the number of books remaining in the library
    books_remaining = num_books - books_required

    # Calculate the number of students the library can help on the fourth day of school
    students_remaining = books_remaining / 5

    # return the result
    result = students_remaining
    return result

print(solution())