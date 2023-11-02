def solution():
    num_books_ryan = 5
    total_pages_ryan = 2100
    num_books_brother = 7
    pages_per_book_brother = 200

    # Calculate the average number of pages Ryan read per day
    days_to_finish = 7
    pages_per_day_ryan = total_pages_ryan / (num_books_ryan * days_to_finish)

    # Calculate the total number of pages Ryan's brother read
    total_pages_brother = num_books_brother * pages_per_book_brother

    # Calculate the average number of pages Ryan's brother read per day
    pages_per_day_brother = total_pages_brother / days_to_finish

    # Calculate the difference in the average number of pages they read per day
    diff_pages_per_day = pages_per_day_ryan - pages_per_day_brother
    result = diff_pages_per_day
    return result

print(solution())