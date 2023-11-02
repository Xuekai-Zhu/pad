def solution():
    fantasy_book_price = 4  # Fantasy books cost $4 each
    literature_book_price = fantasy_book_price / 2  # Literature books cost half the price of a fantasy book
    fantasy_books_sold = 5  # Vincent sold 5 fantasy books per day
    literature_books_sold = 8  # Vincent sold 8 literature books per day
    days = 5  # Vincent sold books for 5 days

    # Calculate the total earnings from selling fantasy books
    fantasy_earnings = fantasy_books_sold * fantasy_book_price * days

    # Calculate the total earnings from selling literature books
    literature_earnings = literature_books_sold * literature_book_price * days

    # Calculate the total earnings from selling both types of books
    total_earnings = fantasy_earnings + literature_earnings
    result = total_earnings
    return result

print(solution())