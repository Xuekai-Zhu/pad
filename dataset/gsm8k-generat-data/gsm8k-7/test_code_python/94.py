def solution():
    pages_per_day = 20
    pages_per_book = 400
    num_books = 3

    # Calculate the total number of pages John needs to write
    total_pages = pages_per_book * num_books

    # Calculate the number of days it will take John to write all the pages
    num_days = total_pages / pages_per_day
    result = num_days
    return result

print(solution())