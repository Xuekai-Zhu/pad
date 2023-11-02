def solution():
    weekly_savings = 50
    biweekly_spending = 46
    total_savings_goal = 135

    # Calculate how long it takes to save $46
    num_biweekly_periods = biweekly_spending / weekly_savings

    # Calculate how long it takes to reach the total savings goal
    num_total_periods = (total_savings_goal / weekly_savings) + num_biweekly_periods

    result = num_total_periods
    return result

print(solution())