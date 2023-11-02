def solution():
    level_one = 90
    level_two = level_one + 8
    level_three = level_two + 12
    level_four = level_three - 9
    total_spaces = level_one + level_two + level_three + level_four
    available_spaces = total_spaces - 100
    result = available_spaces
    return result

print(solution())