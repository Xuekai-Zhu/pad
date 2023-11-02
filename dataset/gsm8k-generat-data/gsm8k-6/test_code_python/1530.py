def solution():
    # Calculate the total number of hours Miles will spend reading
    total_hours = 1/6

    # Calculate the time Miles will spend reading each type of book
    time_per_book = total_hours / 3

    # Calculate the total number of pages Miles will read for each type of book
    novels_pages = 21 * time_per_book
    graphic_novels_pages = 30 * time_per_book
    comic_books_pages = 45 * time_per_book

    # Calculate the total number of pages Miles will read
    total_pages = novels_pages + graphic_novels_pages + comic_books_pages
    result = total_pages
    return result

print(solution())