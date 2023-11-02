def solution():
    # Calculate the total number of crayons Madeline has
    total_crayons = 5 * 24

    # Calculate the number of unused crayons in the first two boxes
    unused_crayons_1_2 = (5/8) * 2 * 24

    # Calculate the number of used crayons in the next two boxes
    used_crayons_3_4 = (1 - 2/3) * 2 * 24

    # Calculate the number of unused crayons in the last box
    unused_crayons_5 = 24 - used_crayons_3_4

    # Add up all the unused crayons
    total_unused_crayons = unused_crayons_1_2 + unused_crayons_5

    result = total_unused_crayons
    return result

print(solution())