def solution():
    """Rose is an aspiring artist. She wants a paintbrush that costs $2.40, a set of paints that costs $9.20, and an easel that costs $6.50 so she can do some paintings. Rose already has $7.10. How much more money does Rose need?"""
    # Define the cost of each item
    BRUSH_COST = 2.40
    PAINTS_COST = 9.20
    EASEL_COST = 6.50

    # Define the amount of money Rose already has
    INITIAL_MONEY = 7.10

    # Calculate the total cost of all the items
    total_cost = BRUSH_COST + PAINTS_COST + EASEL_COST

    # Calculate how much more money Rose needs
    extra_money = total_cost - INITIAL_MONEY

    # Display how much more money Rose needs
    result = extra_money
    return result

print(solution())