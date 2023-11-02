def solution():
    """A school library has 120 books. Each student needs 5 books for their classes. The library was able to help 4 students on the first day of school, 5 students on the second day and 6 students on the third day. How many students can the library help out on the fourth day of school?"""
    total_books = 120
    books_per_student = 5
    students_first_day = 4
    students_second_day = 5
    students_third_day = 6
    books_first_three_days = (students_first_day + students_second_day + students_third_day) * books_per_student
    books_left = total_books - books_first_three_days
    students_fourth_day = books_left // books_per_student
    result = students_fourth_day
    return result

print(solution())