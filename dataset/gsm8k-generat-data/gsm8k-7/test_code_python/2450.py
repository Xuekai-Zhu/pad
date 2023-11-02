def solution():
    height_of_tree = 20
    height_of_previous_tree = 6
    rungs_of_ladder_for_previous_tree = 12

    # Calculate the proportion of heights and rungs of the ladder
    proportion = height_of_tree / height_of_previous_tree

    # Calculate the number of rungs needed to climb for the current tree
    rungs_for_current_tree = rungs_of_ladder_for_previous_tree * proportion
    result = rungs_for_current_tree
    return result

print(solution())