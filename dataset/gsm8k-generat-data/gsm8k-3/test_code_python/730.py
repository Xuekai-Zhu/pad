def solution():
    """Jack bought 3 books a month at $20 each.  He sells them back at the end of the year for $500.  How much money did he lose?"""
    # Define the cost of each book
    BOOK_COST = 20

    # Calculate the total cost of the books
    total_cost = 3 * BOOK_COST * 12

    # Calculate Jack's loss
    loss = total_cost - 500

    # Display Jack's loss
    result = loss
    return result

print(solution())