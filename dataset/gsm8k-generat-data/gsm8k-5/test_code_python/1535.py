def solution():
    books_last_month = 5
    books_this_month = 2 * books_last_month
    pages_per_book = 10

    # Calculate the total number of pages Janine read in two months
    total_pages = (books_last_month + books_this_month) * pages_per_book
    result = total_pages
    return result

print(solution())