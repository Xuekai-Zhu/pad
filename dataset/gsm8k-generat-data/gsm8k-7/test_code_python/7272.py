def solution():
    num_books = 120
    books_per_student = 5

    num_students_day1 = 4
    num_students_day2 = 5
    num_students_day3 = 6

    # Calculate the total number of books used by the first 3 days
    books_used = (num_students_day1 + num_students_day2 + num_students_day3) * books_per_student

    # Calculate how many books are left
    books_left = num_books - books_used

    # Calculate how many students can be helped on the 4th day
    students_day4 = books_left // books_per_student
    result = students_day4
    return result

print(solution())