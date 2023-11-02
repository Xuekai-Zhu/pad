def solution():
    """Tommy wants to earn enough money to buy 8 new books. Each book costs $5. If Tommy already has $13, how much does he need to save up?"""
    # Define the cost of each book and the number of books Tommy wants to buy
    BOOK_COST = 5
    NUM_BOOKS = 8

    # Define the amount of money Tommy already has
    money = 13

    # Calculate the total cost of the books
    total_cost = BOOK_COST * NUM_BOOKS

    # Calculate the amount of money Tommy needs to save up
    savings_needed = total_cost - money

    # Return the result
    result = savings_needed
    return result

print(solution())