def solution():
    allowance = 20
    extra_money = 1.5
    total_money = 425
    weeks = 10
    total_extra_money = extra_money * weeks
    total_allowance = allowance * weeks
    total_earned = total_money - total_allowance
    average_extra_chores = total_earned / weeks
    result = average_extra_chores
    return result

print(solution())