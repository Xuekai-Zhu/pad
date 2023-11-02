def solution():
    """Jane picked 64 apples at the orchard. She sorted them into 4 different baskets to send to her friends. When Jane wasn't looking her sister took 3 apples from each of the baskets. How many apples are in each basket now?"""
    # Define the number of apples picked by Jane and the number of baskets
    apples_picked = 64
    num_baskets = 4

    # Subtract the number of apples taken from each basket
    apples_picked -= (num_baskets * 3)

    # Divide the remaining apples evenly among the baskets
    apples_per_basket = apples_picked / num_baskets

    # return the result
    result = apples_per_basket
    return result

print(solution())