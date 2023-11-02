def solution():
    """Carol gets a fixed $20 allowance each week. She can also earn $1.5 more dollars each week if she does extra chores. At the end of 10 weeks, she has 425 dollars. How many extra chores did she average each week?"""
    weekly_allowance = 20
    extra_chore_pay = 1.5
    total_earnings = 425
    total_weeks = 10
    extra_chore_count = (total_earnings - (weekly_allowance * total_weeks)) / (extra_chore_pay * total_weeks)
    result = extra_chore_count
    return result

print(solution())