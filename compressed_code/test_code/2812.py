def solution():
    
    target_amount = 75
    weekly_chore_goal = 12
    extra_chore_pay = 2
    days = 14
    chores_done = days * 4
    extra_chores_done = chores_done - (weekly_chore_goal * 2)
    earnings = extra_chores_done * extra_chore_pay
    result = earnings
    return result

print(solution())