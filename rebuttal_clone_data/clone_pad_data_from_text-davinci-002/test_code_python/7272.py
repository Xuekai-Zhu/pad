def solution():
    books = 120
    students = 4 + 5 + 6
    books_needed = students * 5
    books_left = books - books_needed
    fourth_day_students = books_left // 5
    result = fourth_day_students
    return result

print(solution())