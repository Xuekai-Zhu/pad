def solution():
    """Robie bought 3 bags of chocolates. She gave the 2 bags to her brothers and sisters then bought another 3 bags. How many bags of chocolates were left?"""
    # Define the initial number of bags of chocolates
    initial_bags = 3

    # Subtract the 2 bags given to siblings
    remaining_bags = initial_bags - 2

    # Add the 3 bags bought later
    remaining_bags += 3

    # return the result
    result = remaining_bags
    return result

print(solution())