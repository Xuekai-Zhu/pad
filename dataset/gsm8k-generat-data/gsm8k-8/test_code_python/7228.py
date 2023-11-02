def solution():
    # Set variables for Matt's book reading
    matt_books_this_year = 75
    matt_books_last_year = matt_books_this_year / 1.5

    # Calculate how many books Pete read last year
    pete_books_last_year = matt_books_last_year * 2
    # Calculate how many books Pete will read this year
    pete_books_this_year = pete_books_last_year * 2

    # Calculate the total number of books Pete read across both years
    total_books_pete = pete_books_last_year + pete_books_this_year

    result = total_books_pete
    return result

print(solution())