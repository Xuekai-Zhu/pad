def solution():
    """Albert wants a paintbrush that costs $1.50, a set of paints that costs $4.35, and a wooden easel that costs $12.65. Albert already has $6.50. How much more money does Albert need?"""
    # Define the cost of each item
    PAINTBRUSH_COST = 1.5
    PAINTS_COST = 4.35
    EASEL_COST = 12.65

    # Define Albert's starting amount of money
    ALBERT_MONEY = 6.5

    # Calculate the total cost of all the items
    total_cost = PAINTBRUSH_COST + PAINTS_COST + EASEL_COST

    # Calculate how much more money Albert needs
    more_money_needed = total_cost - ALBERT_MONEY

    # Display how much more money Albert needs
    result = more_money_needed
    return result

print(solution())