def solution():
    total_books = 10  # total number of books
    reading_books = (2/5) * total_books  # number of reading books
    math_books = (3/10) * total_books  # number of math books
    science_books = math_books - 1  # number of science books
    history_books = total_books - reading_books - math_books - science_books  # number of history books

    result = history_books
    return result

print(solution())