def solution():
    library_books = 120  # The school library has 120 books
    books_per_student = 5  # Each student needs 5 books
    students_per_day = [4, 5, 6]  # The library helps out 4, 5, and 6 students on the first three days, respectively

    # Calculate the total number of students helped on the first three days
    total_students = sum(students_per_day)

    # Calculate the total number of books used on the first three days
    total_books = total_students * books_per_student

    # Calculate the number of books available for the fourth day
    books_remaining = library_books - total_books

    # Calculate the number of students the library can help on the fourth day
    students_remaining = books_remaining // books_per_student
    result = students_remaining
    return result

print(solution())