def solution():
    native_trees = 30  # The forest already has 30 native trees

    # On Monday, the forester triples the number of total trees in the forest
    total_trees_monday = native_trees * 3

    # Calculate the number of trees planted on Monday
    trees_planted_monday = total_trees_monday - native_trees

    # On Tuesday, the forester plants a third of the amount he planted on Monday
    trees_planted_tuesday = trees_planted_monday / 3

    # Calculate the total number of trees planted
    total_trees_planted = trees_planted_monday + trees_planted_tuesday

    result = total_trees_planted
    return result

print(solution())