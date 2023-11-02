def solution():
    """Monica read 16 books last year. This year, she read twice the number of books she read last year. Next year, she wants to read 5 more than twice the number of books she read this year. How many books will Monica read next year?"""
    # Define the number of books Monica read last year
    last_year_books = 16

    # Define the number of books Monica read this year
    this_year_books = last_year_books * 2

    # Define the number of books Monica wants to read next year
    next_year_books = (this_year_books * 2) + 5

    # Return the result
    result = next_year_books
    return result

print(solution())