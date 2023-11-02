def solution():
    # Calculate the number of pages Sabrina has to read in the first month
    num_books_first_month = 4
    num_pages_first_month = num_books_first_month * 200

    # Calculate the number of books Sabrina has left to read
    num_books_left = 14 - num_books_first_month
    num_books_second_month = num_books_left / 2

    # Calculate the number of pages Sabrina has to read in the second month
    num_pages_second_month = num_books_second_month * 200

    # Calculate the total number of pages Sabrina has to read to finish the series
    total_num_pages = num_pages_first_month + num_pages_second_month

    result = total_num_pages
    return result

print(solution())