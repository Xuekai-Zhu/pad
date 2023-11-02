def solution():
    
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