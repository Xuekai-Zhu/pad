def solution():
    # Calculate the total number of rings in each tree
    tree1_rings = 70 * (2+4)  # 70 ring groups, each group has 2 fat and 4 thin rings
    tree2_rings = 40 * (2+4)  # 40 ring groups, each group has 2 fat and 4 thin rings

    # Calculate the age difference between the two trees
    age_diff = (tree1_rings - tree2_rings) / 2  # trees grow 1 ring per year, and there are two rings per group
    result = age_diff
    return result

print(solution())