def solution():
    # calculate the number of parking spaces on each level
    level1 = 90
    level2 = level1 + 8
    level3 = level2 + 12
    level4 = level3 - 9

    # calculate the total number of parking spaces
    total_spaces = level1 + level2 + level3 + level4

    # calculate the number of open parking spaces
    open_spaces = total_spaces - 100

    result = open_spaces
    return result

print(solution())