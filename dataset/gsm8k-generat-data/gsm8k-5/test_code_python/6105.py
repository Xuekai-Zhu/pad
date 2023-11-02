def solution():
    original_plants = 7  # The council originally planned to plant 7 cherry trees
    final_plants = original_plants * 2  # By the end of the decade, they planted twice as many trees
    leaves_per_tree = 100  # Each tree drops 100 leaves during the fall

    # Calculate the total number of leaves that fall from all the trees
    total_leaves = final_plants * leaves_per_tree
    result = total_leaves
    return result

print(solution())