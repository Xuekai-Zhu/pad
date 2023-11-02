def solution():
    fixed_allowance = 20
    extra_earnings_per_chore = 1.5
    num_weeks = 10
    total_earnings = 425

    # Calculate the total amount earned from fixed allowance over 10 weeks
    total_fixed_allowance = fixed_allowance * num_weeks

    # Calculate the total amount earned from extra chores over 10 weeks
    extra_earnings = total_earnings - total_fixed_allowance

    # Calculate the number of extra chores done each week on average
    num_extra_chores = extra_earnings / (extra_earnings_per_chore * num_weeks)
    result = num_extra_chores
    return result

print(solution())