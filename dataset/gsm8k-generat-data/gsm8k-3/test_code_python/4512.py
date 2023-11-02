def solution():
    """Vincent's bookstore is divided into different kinds of books. His top-selling books are fantasy books. He also sells literature books which cost half of the price of a fantasy book. If his fantasy books cost $4 each, and he sold five fantasy books and eight literature books per day, how much money will he earn after five days?"""
    # Define the price of a fantasy book and the price of a literature book
    FANTASY_PRICE = 4
    LITERATURE_PRICE = 2

    # Define the number of fantasy and literature books sold per day
    FANTASY_SOLD = 5
    LITERATURE_SOLD = 8

    # Calculate the total earnings in a day
    daily_earnings = FANTASY_SOLD * FANTASY_PRICE + LITERATURE_SOLD * LITERATURE_PRICE

    # Calculate the total earnings in 5 days
    total_earnings = daily_earnings * 5

    # Display the total earnings
    result = total_earnings
    return result

print(solution())