def solution():
    total_books = 10
    reading_books = int(total_books * (2/5))
    math_books = int(total_books * (3/10))
    science_books = math_books - 1
    history_books = total_books - reading_books - math_books - science_books
    result = history_books
    return result

print(solution())