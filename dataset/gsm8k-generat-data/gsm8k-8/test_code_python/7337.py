def solution():
    # Calculate the number of road signs at the second intersection
    intersection2 = 1.25 * 40

    # Calculate the number of road signs at the third intersection
    intersection3 = 2 * intersection2

    # Calculate the number of road signs at the fourth intersection
    intersection4 = intersection3 - 20

    # Calculate the total number of road signs
    total_signs = 40 + intersection2 + intersection3 + intersection4
    result = total_signs
    return result

print(solution())