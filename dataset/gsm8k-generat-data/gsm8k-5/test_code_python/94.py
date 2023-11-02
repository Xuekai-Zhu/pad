def solution():
    pages_per_day = 20  # John writes 20 pages a day
    pages_per_book = 400  # Each book has 400 pages
    num_books = 3  # John wants to write 3 books

    # Calculate the total number of pages John needs to write
    total_pages = pages_per_book * num_books

    # Calculate the number of days it will take John to write all the books
    num_days = total_pages / pages_per_day
    result = num_days
    return result

print(solution())