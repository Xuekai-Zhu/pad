def solution():
    """A school library has 120 books.  Each student needs 5 books for their classes.  The library was able to help 4 students on the first day of school, 5 students on the second day and 6 students on the third day.  How many students can the library help out on the fourth day of school?"""
    # Define the number of books in the library and the number of books needed per student
    BOOKS_IN_LIBRARY = 120
    BOOKS_PER_STUDENT = 5

    # Define the number of students helped on each of the first three days
    students_day1 = 4
    students_day2 = 5
    students_day3 = 6

    # Calculate the total number of books used on the first three days
    books_used = (students_day1 + students_day2 + students_day3) * BOOKS_PER_STUDENT

    # Calculate the number of books left in the library
    books_left = BOOKS_IN_LIBRARY - books_used

    # Calculate the number of students that can be helped on the fourth day
    students_day4 = books_left // BOOKS_PER_STUDENT

    # Display the number of students that can be helped on the fourth day
    result = students_day4
    return result

print(solution())