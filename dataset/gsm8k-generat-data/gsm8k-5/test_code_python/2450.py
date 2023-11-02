def solution():
    height_of_previous_tree = 6  # Jamie rescued a cat from a 6-foot tree
    rungs_on_ladder_for_previous_tree = 12  # Jamie had to climb 12 rungs to rescue the cat

    height_of_current_tree = 20  # Mrs. Thompson's cat is stuck in a 20-foot tree

    # Calculate the number of rungs Jamie needs to climb to rescue the cat
    # using a proportion of heights and rungs on the ladder
    rungs_on_ladder_for_current_tree = (height_of_current_tree * rungs_on_ladder_for_previous_tree) / height_of_previous_tree
    result = rungs_on_ladder_for_current_tree
    return result

print(solution())