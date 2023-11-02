def solution():
    # Define the data for each tree
    tree1_height = 50
    tree1_branches = 200
    tree2_height = 40
    tree2_branches = 180
    tree3_height = 60
    tree3_branches = 180
    tree4_height = 34
    tree4_branches = 153

    # Calculate the total number of branches and total height for all trees
    total_branches = tree1_branches + tree2_branches + tree3_branches + tree4_branches
    total_height = tree1_height + tree2_height + tree3_height + tree4_height

    # Calculate the average branches per foot
    average_branches_per_foot = total_branches / total_height
    result = average_branches_per_foot
    return result

print(solution())