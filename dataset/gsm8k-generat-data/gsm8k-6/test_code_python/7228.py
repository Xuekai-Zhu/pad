def solution():
    # Calculate the number of books Matt read in his first year
    matt_first_year = 75 / 1.5 - 75  # Matt reads 50% more books in his second year, so he read (75/1.5) books in his first year

    # Calculate the number of books Pete read last year
    pete_last_year = 2 * matt_first_year  

    # Calculate the number of books Pete read this year
    pete_this_year = 2 * pete_last_year  

    # Calculate the total number of books Pete read across both years
    total_pete_books = pete_last_year + pete_this_year
    result = total_pete_books
    return result

print(solution())