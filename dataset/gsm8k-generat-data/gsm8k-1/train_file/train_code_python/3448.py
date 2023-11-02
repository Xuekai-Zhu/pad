def solution():
    """An apple tree can fill 20 baskets. Each basket can be filled with 15 apples. How many apples can you get from 10 trees?"""
    baskets_per_tree = 20
    apples_per_basket = 15
    trees = 10
    total_baskets = baskets_per_tree * trees
    total_apples = total_baskets * apples_per_basket
    result = total_apples
    return result

print(solution())