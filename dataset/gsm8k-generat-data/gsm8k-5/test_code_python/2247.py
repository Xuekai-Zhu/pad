def solution():
    # Determine the total number of rings in the first tree
    fat_rings = 2 * 70  # There are 2 fat rings in every group, and there are 70 groups
    thin_rings = 4 * 70  # There are 4 thin rings in every group, and there are 70 groups
    total_rings_first = fat_rings + thin_rings

    # Determine the total number of rings in the second tree
    fat_rings = 2 * 40  # There are 2 fat rings in every group, and there are 40 groups
    thin_rings = 4 * 40  # There are 4 thin rings in every group, and there are 40 groups
    total_rings_second = fat_rings + thin_rings

    # Calculate the age difference between the two trees
    age_difference = total_rings_first - total_rings_second

    # Convert age difference from number of rings to number of years
    result = age_difference
    return result

print(solution())