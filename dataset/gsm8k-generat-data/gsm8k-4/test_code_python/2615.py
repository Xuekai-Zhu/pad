def solution():
    """Six bottles of 2 liters of water cost $12. What is the price of 1 liter of water?"""
    # Define the total cost of the water
    total_cost = 12

    # Calculate the total volume of water
    total_volume = 6 * 2

    # Calculate the price per liter of water
    price_per_liter = total_cost / total_volume

    # return the result
    result = price_per_liter
    return result

print(solution())