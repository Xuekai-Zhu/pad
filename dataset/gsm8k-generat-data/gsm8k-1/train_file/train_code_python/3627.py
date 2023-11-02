def solution():
    """Edmund is buying a new computer and needs to save up $75 before he has enough. He convinces his parents to pay him for extra chores. He normally has to do 12 chores a week. His parents agree to pay him $2 for every extra chore he does during the week. If he does 4 chores a day for two weeks, how much does he earn?"""
    needed_savings = 75
    chores_per_week = 12
    extra_chore_payment = 2
    extra_chores_per_day = 4
    weeks = 2
    total_chores = chores_per_week * weeks
    extra_chores = (total_chores - (weeks * 7 * 4))
    extra_earnings = extra_chore_payment * extra_chores
    result = extra_earnings
    
    return result

print(solution())