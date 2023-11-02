def solution():
    num_palm_trees_forest = 5000
    fraction_less_desert = 3/5

    # Calculate the number of palm trees in the desert
    num_palm_trees_desert = num_palm_trees_forest * (1 - fraction_less_desert)

    # Calculate the total number of palm trees in both the desert and the forest
    total_palm_trees = num_palm_trees_forest + num_palm_trees_desert
    result = total_palm_trees
    return result

print(solution())