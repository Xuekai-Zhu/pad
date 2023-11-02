def solution():
    """Carol gets a fixed $20 allowance each week. She can also earn $1.5 more dollars each week if she does extra chores. At the end of 10 weeks, she has 425 dollars. How many extra chores did she average each week?"""
    weeks = 10
    fixed_allowance = 20
    extra_pay_per_chore = 1.5
    total_earnings = 425
    average_extra_chores = (total_earnings - (fixed_allowance * weeks)) / (extra_pay_per_chore * weeks)
    result = average_extra_chores
    return result

print(solution())