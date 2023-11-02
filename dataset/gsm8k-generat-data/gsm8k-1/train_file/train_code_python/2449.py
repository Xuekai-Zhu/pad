def solution():
    """Jamie is a firefighter. One day an emergency call comes in from Mrs. Thompson, an elderly woman whose cat can't get down a 20-foot tree. The last time Jamie rescued a cat, he got it down from a 6-foot tree and had to climb 12 rungs of his ladder. How many rungs does he have to climb this time to get the cat down from the tree?"""
    height_of_tree = 20
    height_of_previous_tree = 6
    rungs_on_ladder_for_previous_tree = 12
    rungs_on_ladder_per_foot = rungs_on_ladder_for_previous_tree/height_of_previous_tree
    rungs_for_this_tree = height_of_tree * rungs_on_ladder_per_foot
    result = rungs_for_this_tree
    return result

print(solution())