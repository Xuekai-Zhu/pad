def solution():
    goal = 80  # Hannah wants to save $80 in five weeks
    current_savings = 4  # Hannah saved $4 in the first week
    savings_multiplier = 2  # Hannah plans to save twice as much as her savings in the previous week

    # Calculate the total savings required for the next four weeks
    remaining_goal = goal - current_savings
    remaining_weeks = 4
    total_savings_required = remaining_goal / remaining_weeks

    # Calculate how much Hannah needs to save in the fifth week to reach her goal
    last_week_savings = total_savings_required / savings_multiplier**3
    result = last_week_savings
    return result

print(solution())