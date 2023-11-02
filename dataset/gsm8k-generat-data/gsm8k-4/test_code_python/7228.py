def solution():
    """
    If Pete read twice as many books as Matt did last year, and this year he doubles
    that number while Matt reads only 50% more, how many books does Pete read across
    both years if Matt read 75 books in his second year?
    """
    # Define the number of books Matt read in his second year
    matt_books_second_year = 75

    # Calculate the number of books Matt read in his first year
    matt_books_first_year = matt_books_second_year / 1.5

    # Calculate the number of books Pete read last year
    pete_books_last_year = 2 * matt_books_first_year

    # Calculate the number of books Pete read this year
    pete_books_this_year = 2 * pete_books_last_year

    # Calculate the total number of books Pete read across both years
    total_books_pete = pete_books_last_year + pete_books_this_year

    # return the result
    result = total_books_pete
    return result

print(solution())