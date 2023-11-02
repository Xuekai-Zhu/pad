def solution():
    # Define the height of the tree and the number of rungs needed to climb a 6-foot tree
    tree_height = 20
    rungs_per_six_feet = 12

    # Calculate the total number of rungs needed to climb the tree
    total_rungs = (tree_height / 6) * rungs_per_six_feet
    result = total_rungs
    return result

print(solution())