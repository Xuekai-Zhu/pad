def solution():
    ryan_books = 5  # Ryan got 5 books from the library
    ryan_pages = 2100  # The total number of pages in Ryan's 5 books
    ryan_pages_per_day = ryan_pages / 7  # Ryan read a total of 2100 pages in 7 days, so he read this many per day

    brother_pages_per_day = 200  # Ryan's brother read one book a day, each with 200 pages

    # Calculate the difference in pages per day between Ryan and his brother
    difference = ryan_pages_per_day - brother_pages_per_day
    result = difference
    return result

print(solution())