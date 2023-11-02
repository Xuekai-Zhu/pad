def solution():
    num_trees = 10
    baskets_per_tree = 20
    apples_per_basket = 15

    # Calculate the total number of baskets
    total_baskets = num_trees * baskets_per_tree

    # Calculate the total number of apples
    total_apples = total_baskets * apples_per_basket
    result = total_apples
    return result

print(solution())