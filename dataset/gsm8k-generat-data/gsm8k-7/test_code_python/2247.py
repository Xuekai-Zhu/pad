def solution():
    fat_rings = 2
    thin_rings = 4

    tree1_rings = 70 * (fat_rings + thin_rings)  # Total number of rings in tree 1
    tree2_rings = 40 * (fat_rings + thin_rings)  # Total number of rings in tree 2

    age_diff = (tree1_rings - tree2_rings) / 2  # Divide by 2 to get the age difference in years
    result = age_diff
    return result

print(solution())