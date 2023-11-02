def solution():
    # Let x be the number of books Matt read in his first year
    x = 0

    # Pete read twice as many books as Matt did last year
    pete_first_year = 2 * x

    # Pete doubles the number of books he read last year
    pete_second_year = 2 * pete_first_year

    # Matt reads only 50% more than his second year, which is 75 books
    matt_second_year = 75
    matt_first_year = matt_second_year / 1.5

    # Pete's total number of books read across both years
    pete_total = pete_first_year + pete_second_year

    # Matt's total number of books read across both years
    matt_total = matt_first_year + matt_second_year

    # Calculate the total number of books that the two of them read
    total_books = pete_total + matt_total
    result = total_books
    return result

print(solution())