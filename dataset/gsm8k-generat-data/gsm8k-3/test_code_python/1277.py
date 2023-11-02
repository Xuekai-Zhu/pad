def solution():
    """Jane picked 64 apples at the orchard. She sorted them into 4 different baskets to send to her friends. When Jane wasn't looking her sister took 3 apples from each of the baskets. How many apples are in each basket now?"""
    # Calculate the total number of apples
    total_apples = 64

    # Divide the total apples into 4 equal baskets
    apples_per_basket = total_apples / 4

    # Calculate the new number of apples in each basket
    new_apples_per_basket = apples_per_basket - 3

    # Display the new number of apples in each basket
    result = new_apples_per_basket
    return result

print(solution())