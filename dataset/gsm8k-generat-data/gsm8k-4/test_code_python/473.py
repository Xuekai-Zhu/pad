def solution():
    """James and Ali together own $250. If you know that James owns $40 more than Ali, then calculate the amount owned by James."""
    # Define the difference in amount owned between James and Ali
    difference = 40

    # Set up an equation where x is the amount owned by Ali
    # James owns 40 more than Ali, so James' amount is x + 40
    # Together, they own $250, so x + (x + 40) = 250
    # Simplifying the equation, we get 2x + 40 = 250
    # Solving for x, we get x = 105
    # Therefore, James' amount is x + 40 = 145
    james_amount = 145
    result = james_amount
    return result

print(solution())