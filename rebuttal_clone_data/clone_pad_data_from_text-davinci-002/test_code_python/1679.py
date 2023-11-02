def solution():
    length = 1000
    width = 2000
    square_feet_per_tree = 20
    total_square_feet = length * width
    total_trees = total_square_feet / square_feet_per_tree
    result = total_trees
    return result

print(solution())