def solution():
    """Abie had 20 bags of chips. She gave 4 bags to her friend and bought another 6 bags of chips in the store. How many bags of chips does Abie have in the end?"""
    # Define the initial number of bags of chips
    initial_bags = 20

    # Subtract the bags given away
    remaining_bags = initial_bags - 4

    # Add the bags bought in the store
    total_bags = remaining_bags + 6

    result = total_bags
    return result

print(solution())