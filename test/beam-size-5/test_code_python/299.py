def solution():
    
    # Define the number of books sold in the current year and the number of unsold books in the current year
    current_books = 50
    unsold_books_in_current_year = 50

    # Calculate the number of books sold in the first year and the number of unsold books in the second year
    books_sold_first_year = 2 * current_books
    books_in_second_year = 250 - (current_books * unsold_books_in_current_year)

    # Calculate the total earnings in the first year
    earnings_first_year = books_sold_first_year * 20

    # Calculate the total earnings in the second year
    total_earnings_second_year = earnings_first_year + books_in_second_year

    # return the result
    result = total_earnings_second_year
    return result

print(solution())