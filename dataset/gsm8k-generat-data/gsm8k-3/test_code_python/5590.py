def solution():
    """A desert has 3/5 fewer palm trees than a nearby forest, which has 5000 palm trees. How many palm trees are there in both the desert and the forest combined?"""
    # Define the number of palm trees in the nearby forest
    forest_palm_trees = 5000

    # Calculate the number of palm trees in the desert
    desert_palm_trees = forest_palm_trees - (3/5 * forest_palm_trees)

    # Calculate the total number of palm trees in both the forest and the desert
    total_palm_trees = forest_palm_trees + desert_palm_trees

    # Display the total number of palm trees
    result = total_palm_trees
    return result

print(solution())