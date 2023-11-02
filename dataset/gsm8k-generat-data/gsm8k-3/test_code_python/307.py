def solution():
    """Tommy wants to earn enough money to buy 8 new books. Each book costs $5. If Tommy already has $13, how much does he need to save up?"""
    # Define the cost of each book and the money Tommy already has
    BOOK_COST = 5
    TOMMY_MONEY = 13

    # Calculate the total cost of the 8 books
    book_total_cost = BOOK_COST * 8

    # Calculate how much Tommy needs to save up
    money_needed = book_total_cost - TOMMY_MONEY

    # Display how much Tommy needs to save up
    result = money_needed
    return result

print(solution())