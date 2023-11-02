def solution():
    # Calculate the number of palm trees in the forest
    forest_palm_trees = 5000

    # Calculate the number of palm trees in the desert
    desert_palm_trees = forest_palm_trees - (3/5 * forest_palm_trees)

    # Calculate the total number of palm trees
    total_palm_trees = forest_palm_trees + desert_palm_trees

    result = total_palm_trees
    return result

print(solution())