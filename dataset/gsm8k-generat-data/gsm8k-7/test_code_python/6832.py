def solution():
    lunch_time = 4  # in hours
    book_time = lunch_time * 2  # Juan takes double the time to read a book

    book_pages = 4000
    book_hours = book_time / 60  # convert book time to hours
    pages_per_hour = book_pages / book_hours

    result = pages_per_hour
    return result

print(solution())