def solution():
    """An apple tree can fill 20 baskets. Each basket can be filled with 15 apples. How many apples can you get from 10 trees?"""
    # Define the number of baskets per tree and the number of apples per basket
    baskets_per_tree = 20
    apples_per_basket = 15

    # Calculate the total number of apples from all trees
    total_apples = baskets_per_tree * apples_per_basket * 10

    # Return the total number of apples
    result = total_apples
    return result

print(solution())