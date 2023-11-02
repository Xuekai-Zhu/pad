def solution():
    
    level_one = 90
    level_two = level_one + 8
    level_three = level_two + 12
    level_four = level_three - 9
    total_spaces = level_one + level_two + level_three + level_four
    spaces_available = total_spaces - 100
    result = spaces_available
    return result

print(solution())