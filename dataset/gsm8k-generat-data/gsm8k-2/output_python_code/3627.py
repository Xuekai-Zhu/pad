def solution():
    """Edmund is buying a new computer and needs to save up $75 before he has enough. He convinces his parents to pay him for extra chores. He normally has to do 12 chores a week. His parents agree to pay him $2 for every extra chore he does during the week. If he does 4 chores a day for two weeks, how much does he earn?"""
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