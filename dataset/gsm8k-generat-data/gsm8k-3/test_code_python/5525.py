def solution():
    """Abie had 20 bags of chips. She gave 4 bags to her friend and bought another 6 bags of chips in the store. How many bags of chips does Abie have in the end?"""
    # Define the initial number of bags
    initial_bags = 20

    # Subtract the bags given away
    bags_after_gift = initial_bags - 4

    # Add the bags bought
    bags_after_purchase = bags_after_gift + 6

    # Display the final number of bags
    result = bags_after_purchase
    return result

print(solution())