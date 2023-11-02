def solution():
    """Roxanne bought 2 cups of lemonade for $2 each and 2 sandwiches for $2.50 each. How much change must she get from a $20 bill?"""
    # Calculate the total cost of the lemonades and sandwiches
    total_cost = (2 * 2) + (2 * 2.5)

    # Calculate the amount of change from a $20 bill
    change = 20 - total_cost
    
    result = change
    return result

print(solution())