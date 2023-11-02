def solution():
    """3 trees each had 7 blue birds in them. 2 different trees each had 4 blue birds. 1 final tree had 3 blue birds. How many blue birds were in the trees in total?"""
    trees_with_7 = 3
    trees_with_4 = 2
    trees_with_3 = 1
    blue_birds_per_tree_with_7 = 7
    blue_birds_per_tree_with_4 = 4
    blue_birds_per_tree_with_3 = 3
    total_blue_birds = (trees_with_7 * blue_birds_per_tree_with_7) + (trees_with_4 * blue_birds_per_tree_with_4) + (trees_with_3 * blue_birds_per_tree_with_3)
    result = total_blue_birds
    return result

print(solution())