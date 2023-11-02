def solution():
    """If Pete read twice as many books as Matt did last year, and this year he doubles that number while Matt reads only 50% more, how many books does Pete read across both years if Matt read 75 books in his second year?"""
    # Determine how many books Matt read last year
    matt_last_year = 75 / 1.5

    # Determine how many books Pete read last year
    pete_last_year = 2 * matt_last_year

    # Determine how many books Pete read this year
    pete_this_year = 2 * pete_last_year

    # Determine the total number of books Pete read across both years
    total_books = pete_last_year + pete_this_year

    # Display the total number of books Pete read 
    result = total_books
    return result

print(solution())