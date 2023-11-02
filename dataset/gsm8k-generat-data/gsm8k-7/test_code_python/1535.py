def solution():
    books_last_month = 5
    books_this_month = 2 * books_last_month
    pages_per_book = 10

    # Calculate the total number of pages Janine read last month
    pages_last_month = books_last_month * pages_per_book

    # Calculate the total number of pages Janine read this month
    pages_this_month = books_this_month * pages_per_book

    # Calculate the total number of pages Janine read in two months
    total_pages = pages_last_month + pages_this_month
    result = total_pages
    return result

print(solution())