def solution():
    allowance = 12
    savings_goal = allowance / 2
    days_in_week = 7
    money_saved = (days_in_week - 1) * savings_goal + (savings_goal / 2)
    result = money_saved
    return result

print(solution())