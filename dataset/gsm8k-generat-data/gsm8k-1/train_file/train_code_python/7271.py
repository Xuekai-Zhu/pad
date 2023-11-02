def solution():
    """A school library has 120 books. Each student needs 5 books for their classes. The library was able to help 4 students on the first day of school, 5 students on the second day and 6 students on the third day. How many students can the library help out on the fourth day of school?"""
    total_books = 120
    books_per_student = 5
    students_day1 = 4
    students_day2 = 5
    students_day3 = 6
    total_students = students_day1 + students_day2 + students_day3
    books_used = total_students * books_per_student
    books_remaining = total_books - books_used
    students_day4 = books_remaining // books_per_student
    result = students_day4
    return result

print(solution())