def solution():
    """Jackie loves to climb trees. She climbed a 1000 foot tall tree. Then she climbed 2 trees that were half as tall as the first tree. She finished by climbing a tree that was 200 feet taller than her first tree. What was the average height of the trees that Jackie climbed?"""
    tree_1 = 1000
    tree_2 = tree_1 / 2
    tree_3 = tree_2
    tree_4 = tree_1 + 200
    total_height = tree_1 + tree_2 + tree_3 + tree_4
    num_trees = 4
    average_height = total_height / num_trees
    result = average_height
    return result

print(solution())