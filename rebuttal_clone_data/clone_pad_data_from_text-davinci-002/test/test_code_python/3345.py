def solution():
    coconuts_per_tree = 5
    coconut_price = 3
    desired_amount = 90
    number_of_trees = desired_amount / (coconuts_per_tree * coconut_price)
    result = number_of_trees
    return result

print(solution())