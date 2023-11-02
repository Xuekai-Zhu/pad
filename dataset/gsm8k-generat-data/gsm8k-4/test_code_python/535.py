def solution():
    """Tim buys 3 dozen eggs. Eggs cost $.50 each. How much did he pay for eggs?"""
    # Define the number of eggs and the price per egg
    eggs_per_dozen = 12
    price_per_egg = 0.5

    # Calculate the total cost of the eggs
    total_eggs = 3 * eggs_per_dozen
    total_cost = total_eggs * price_per_egg

    # return the result
    result = total_cost
    return result

print(solution())