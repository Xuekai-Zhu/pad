def solution():
    
    total_bread = 200
    eaten_first_day = total_bread * (1 / 4)
    remaining_bread1 = total_bread - eaten_first_day
    eaten_second_day = remaining_bread1 * (2 / 5)
    remaining_bread2 = remaining_bread1 - eaten_second_day
    eaten_third_day = remaining_bread2 * (1 / 2)
    remaining_bread3 = remaining_bread2 - eaten_third_day
    result = remaining_bread3
    return result

print(solution())