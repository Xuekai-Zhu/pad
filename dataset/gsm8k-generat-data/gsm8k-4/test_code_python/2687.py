def solution():
    """A forester is planting trees. The forest already has 30 native trees. On Monday he triples the number of total trees in the forest by planting new trees. On Tuesday, he plants a third of the amount he planted on Monday. How many trees has the forester planted in total?"""
    # Define the initial number of trees
    initial_trees = 30

    # Calculate the number of trees after planting on Monday
    trees_on_monday = initial_trees * 3

    # Calculate the number of trees planted on Monday
    trees_planted_on_monday = trees_on_monday - initial_trees

    # Calculate the number of trees planted on Tuesday
    trees_planted_on_tuesday = trees_planted_on_monday / 3

    # Calculate the total number of trees planted
    total_trees_planted = trees_planted_on_monday + trees_planted_on_tuesday

    # return the result
    result = int(total_trees_planted)
    return result

print(solution())