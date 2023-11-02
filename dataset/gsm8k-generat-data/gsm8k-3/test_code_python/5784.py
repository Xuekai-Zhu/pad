def solution():
    """Jay bought a book for $25, a pen for $4, and a ruler for $1. He paid with a fifty-dollar bill. How much change, in dollars, did Jay get?"""
    # Define the cost of each item
    BOOK_COST = 25
    PEN_COST = 4
    RULER_COST = 1

    # Calculate the total cost of the items
    total_cost = BOOK_COST + PEN_COST + RULER_COST

    # Calculate the change that Jay will receive
    change = 50 - total_cost
    
    # Display the change that Jay will receive
    result = change
    return result

print(solution())