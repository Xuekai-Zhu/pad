def solution():
    baskets_per_tree = 20  # Each apple tree can fill 20 baskets
    apples_per_basket = 15  # Each basket can be filled with 15 apples
    number_of_trees = 10  # We want to know the total number of apples from 10 trees

    # Calculate the total number of baskets from 10 trees
    total_baskets = baskets_per_tree * number_of_trees

    # Calculate the total number of apples
    total_apples = total_baskets * apples_per_basket
    result = total_apples
    return result

print(solution())