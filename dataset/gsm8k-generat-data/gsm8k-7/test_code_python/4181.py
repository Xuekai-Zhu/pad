def solution():
    total_weeks = 5
    goal_savings = 80
    current_savings = 4
    
    # Calculate the total amount she needs to save for four weeks
    remaining_goal = goal_savings - current_savings
    
    # Calculate the amount she needs to save each week to reach her goal
    weekly_goal = remaining_goal / (total_weeks - 1)
    
    # Calculate her savings for the fifth week
    fifth_week_savings = 2 * weekly_goal
    
    result = fifth_week_savings
    return result

print(solution())