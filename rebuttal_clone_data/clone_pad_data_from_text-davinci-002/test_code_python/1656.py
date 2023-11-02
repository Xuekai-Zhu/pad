def solution():
    length_of_fence = 25
    width_of_tree = 1.5
    price_of_tree = 8
    number_of_trees = length_of_fence / width_of_tree
    total_cost = number_of_trees * price_of_tree
    result = total_cost
    return result

print(solution())