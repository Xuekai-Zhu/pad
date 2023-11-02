def solution():
    # Calculate the total number of rings in each tree by multiplying the number of ring groups by 6
    tree1_rings = 70 * 6
    tree2_rings = 40 * 6

    # Calculate the age difference between the two trees by subtracting their total ring counts
    age_difference = tree1_rings - tree2_rings

    result = age_difference
    return result

print(solution())