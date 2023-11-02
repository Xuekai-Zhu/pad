def solution():
    # Calculate the number of unused crayons in the first 2 boxes
    unused_crayons_1 = (5/8) * 24 * 2

    # Calculate the number of used crayons in the other 2 boxes
    used_crayons_2 = (1 - (2/3)) * 24 * 2

    # Calculate the number of unused crayons in the last box
    unused_crayons_3 = 24 - used_crayons_2 % 24

    # Calculate the total number of unused crayons
    total_unused_crayons = unused_crayons_1 + unused_crayons_3

    result = total_unused_crayons
    return result

print(solution())