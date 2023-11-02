def solution():
    # Calculate the number of books Monica read this year
    books_this_year = 16 * 2  # Monica read twice the number of books she read last year

    # Calculate the number of books Monica wants to read next year
    books_next_year = 5 + (2 * books_this_year)  # Monica wants to read 5 more than twice the number of books she read this year

    result = books_next_year
    return result

print(solution())