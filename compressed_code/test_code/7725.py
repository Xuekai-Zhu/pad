def solution():
    
    height_of_tree = 20
    height_of_previous_tree = 6
    rungs_on_ladder_for_previous_tree = 12
    rungs_on_ladder_per_foot = rungs_on_ladder_for_previous_tree/height_of_previous_tree
    rungs_for_this_tree = height_of_tree * rungs_on_ladder_per_foot
    result = rungs_for_this_tree
    return result

print(solution())