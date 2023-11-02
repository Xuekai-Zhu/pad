def solution():
    
    total_kids = 40
    less_than_6 = total_kids * 0.1
    less_than_8 = 3 * less_than_6
    remaining = total_kids - less_than_6 - less_than_8
    more_than_14 = remaining / 6
    result = more_than_14
    return result

print(solution())