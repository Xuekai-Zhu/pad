def solution():
    """Vincent's bookstore is divided into different kinds of books. His top-selling books are fantasy books. He also sells literature books which cost half of the price of a fantasy book. If his fantasy books cost $4 each, and he sold five fantasy books and eight literature books per day, how much money will he earn after five days?"""
    # Define the price of a fantasy book and a literature book
    FANTASY_PRICE = 4
    LITERATURE_PRICE = FANTASY_PRICE / 2

    # Define the number of fantasy books and literature books sold each day
    FANTASY_SOLD = 5
    LITERATURE_SOLD = 8

    # Calculate the total earnings from selling fantasy books in 5 days
    fantasy_earnings = FANTASY_PRICE * FANTASY_SOLD * 5

    # Calculate the total earnings from selling literature books in 5 days
    literature_earnings = LITERATURE_PRICE * LITERATURE_SOLD * 5

    # Calculate the total earnings in 5 days
    total_earnings = fantasy_earnings + literature_earnings

    # return the result
    result = total_earnings
    return result

print(solution())