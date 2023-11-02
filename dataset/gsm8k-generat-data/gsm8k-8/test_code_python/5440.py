def solution():
    weekly_savings = 50
    biweekly_spending = 46
    total_savings_goal = 135

    # Calculate how many weeks it takes to save up for a biweekly lunch
    biweekly_cost = 2 * biweekly_spending
    biweekly_savings = 2 * weekly_savings - biweekly_cost
    weeks_for_biweekly_lunch = biweekly_cost / biweekly_savings

    # Calculate how many weeks it takes to reach the savings goal
    total_weeks = (total_savings_goal - biweekly_spending) / (weekly_savings - biweekly_savings) + weeks_for_biweekly_lunch
    result = total_weeks
    return result

print(solution())