def solution():
    total_shells = 65
    purple_shells = 13
    pink_shells = 8
    yellow_shells = 18
    blue_shells = 12

    # Calculate the total number of shells for the other colors
    other_shells = purple_shells + pink_shells + yellow_shells + blue_shells

    # Calculate the number of orange shells
    orange_shells = total_shells - other_shells
    result = orange_shells
    return result

print(solution())