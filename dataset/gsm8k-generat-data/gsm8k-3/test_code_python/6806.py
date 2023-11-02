def solution():
    """Daniel collects Russian dolls that normally cost $4 each. He saves enough money to buy 15 Russian dolls. However, the price suddenly drops to $3 each. How many Russian dolls can he buy now at the discounted price, given his savings?"""
    # Define the original cost and the discounted cost of each Russian doll
    ORIGINAL_COST = 4
    DISCOUNTED_COST = 3

    # Define the number of Russian dolls Daniel saved enough money to buy
    num_dolls = 15

    # Calculate how many dolls he can buy now at the discounted price
    num_discounted_dolls = num_dolls * (ORIGINAL_COST / DISCOUNTED_COST)

    # Display the number of discounted dolls he can buy
    result = num_discounted_dolls
    return result

print(solution())