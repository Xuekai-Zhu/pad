def solution():
    
    allowance = 12
    spent_first_week = allowance/3
    remaining1 = allowance - spent_first_week
    spent_second_week = remaining1/4
    remaining2 = remaining1 - spent_second_week
    result = remaining2
    return result

print(solution())