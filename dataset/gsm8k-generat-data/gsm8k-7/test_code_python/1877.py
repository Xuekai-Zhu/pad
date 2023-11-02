def solution():
    num_books_last_week = 5
    pages_per_book = 300
    num_books_this_week = num_books_last_week * 2

    # Calculate the total number of pages read last week
    total_pages_last_week = num_books_last_week * pages_per_book

    # Calculate the total number of pages read this week
    total_pages_this_week = num_books_this_week * pages_per_book

    # Calculate the total number of pages read in total
    total_pages = total_pages_last_week + total_pages_this_week
    result = total_pages
    return result

print(solution())