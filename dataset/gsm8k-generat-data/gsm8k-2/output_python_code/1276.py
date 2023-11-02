def solution():
    """Jane picked 64 apples at the orchard. She sorted them into 4 different baskets to send to her friends. When Jane wasn't looking her sister took 3 apples from each of the baskets. How many apples are in each basket now?"""
    total_apples = 64
    num_baskets = 4
    apples_per_basket = total_apples / num_baskets
    apples_per_basket -= 3
    result = apples_per_basket
    return result

print(solution())