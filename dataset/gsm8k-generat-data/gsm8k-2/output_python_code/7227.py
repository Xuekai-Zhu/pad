def solution():
    """If Pete read twice as many books as Matt did last year, and this year he doubles that number while Matt reads only 50% more, how many books does Pete read across both years if Matt read 75 books in his second year?"""
    matt_second_year = 75
    matt_first_year = matt_second_year / 1.5
    pete_first_year = 2 * matt_first_year
    pete_second_year = 2 * pete_first_year
    total_books = pete_first_year + pete_second_year
    result = total_books
    return result

print(solution())