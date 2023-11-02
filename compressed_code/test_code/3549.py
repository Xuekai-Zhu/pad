def solution():
    
    allowance = 12
    spent_first_week = allowance / 3
    remaining_money = allowance - spent_first_week
    spent_second_week = remaining_money / 4
    remaining_money -= spent_second_week
    result = remaining_money
    return result

print(solution())