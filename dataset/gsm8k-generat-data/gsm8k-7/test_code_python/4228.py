def solution():
    daily_allowance = 12
    days_in_week = 7

    # Calculate the total amount Martha would have saved if she saved half every day
    savings_half = (daily_allowance / 2) * (days_in_week - 1)

    # Calculate the additional savings from the day she saved only a quarter
    savings_quarter = (daily_allowance / 4)

    # Calculate the total savings for the week
    total_savings = savings_half + savings_quarter

    result = total_savings
    return result

print(solution())