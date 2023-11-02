def solution():
    # Number of road signs at the first intersection
    intersection_1 = 40

    # Number of road signs at the second intersection
    intersection_2 = intersection_1 * (1 + 1/4)

    # Number of road signs at the third intersection
    intersection_3 = intersection_2 * 2

    # Number of road signs at the fourth intersection
    intersection_4 = intersection_3 - 20

    # Total number of road signs
    total = intersection_1 + intersection_2 + intersection_3 + intersection_4
    result = total
    return result

print(solution())