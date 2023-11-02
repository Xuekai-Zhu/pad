def solution():
    fantasy_book_cost = 4
    literature_book_cost = fantasy_book_cost / 2
    num_fantasy_books_sold = 5
    num_literature_books_sold = 8
    num_days = 5

    # Calculate the total earnings from selling fantasy books
    total_earnings_fantasy = fantasy_book_cost * num_fantasy_books_sold * num_days

    # Calculate the total earnings from selling literature books
    total_earnings_literature = literature_book_cost * num_literature_books_sold * num_days

    # Calculate the total earnings from selling all books
    total_earnings = total_earnings_fantasy + total_earnings_literature
    result = total_earnings
    return result

print(solution())