def solution():
    """If Pete read twice as many books as Matt did last year, and this year he doubles that number while Matt reads only 50% more, how many books does Pete read across both years if Matt read 75 books in his second year?"""
    
    # Matt's books in the first year are half of Pete's books in the first year
    matt_first_year = 0.5 * pete_first_year_books
    
    # Pete's books in the second year are twice as many as his books in the first year
    pete_second_year = 2 * pete_first_year_books
    
    # Matt's books in the second year are 50% more than his books in the first year
    matt_second_year = 1.5 * matt_first_year
    
    total_books = pete_first_year_books + pete_second_year + matt_first_year + matt_second_year + 75
    
    result = total_books
    return result

print(solution())