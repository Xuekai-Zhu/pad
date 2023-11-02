def solution():
    """Bailey starts with a certain amount of money. Then she receives a weekly allowance of $5 for 8 weeks. At the end of the 8 weeks, if she has a total of $100, how much money did Bailey start with?"""
    weekly_allowance = 5
    num_weeks = 8
    total_allowance = weekly_allowance * num_weeks
    end_amount = 100
    start_amount = end_amount - total_allowance
    result = start_amount
    return result

print(solution())