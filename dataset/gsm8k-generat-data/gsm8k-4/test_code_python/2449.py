def solution():
    """Yanna bought ten shirts at $5 each and three pairs of sandals at $3 each. How much change did she get back if she gave a one hundred dollar bill?"""
    # Define the cost of the shirts and sandals
    shirt_cost = 5
    sandal_cost = 3

    # Calculate the total cost of the shirts and sandals
    total_cost = (10 * shirt_cost) + (3 * sandal_cost)

    # Calculate the amount of change she would get back from a $100 bill
    change = 100 - total_cost

    # return the result
    result = change
    return result

print(solution())