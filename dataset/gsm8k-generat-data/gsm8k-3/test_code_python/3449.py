def solution():
    """An apple tree can fill 20 baskets. Each basket can be filled with 15 apples. How many apples can you get from 10 trees?"""
    # Define the number of baskets that can be filled from one tree
    BASKETS_PER_TREE = 20

    # Define the number of apples that can fit in one basket
    APPLES_PER_BASKET = 15

    # Calculate the total number of apples from 10 trees
    total_apples = BASKETS_PER_TREE * APPLES_PER_BASKET * 10

    # Display the total number of apples
    result = total_apples
    return result

print(solution())