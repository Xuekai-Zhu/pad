def solution():
    forest_palm_trees = 5000  # The nearby forest has 5000 palm trees
    desert_palm_trees = (3/5) * forest_palm_trees  # The desert has 3/5 fewer palm trees than the forest

    # Calculate the total number of palm trees in both the forest and the desert
    total_palm_trees = forest_palm_trees + desert_palm_trees
    result = total_palm_trees
    return result

print(solution())