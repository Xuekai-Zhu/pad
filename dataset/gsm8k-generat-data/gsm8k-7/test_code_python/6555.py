def solution():
    previous_miles = 100
    goal_percent = 1.2  # 20% increase
    goal_days = 280

    # Calculate the total goal miles
    total_goal_miles = previous_miles * goal_percent

    # Calculate the number of days per week
    days_per_week = 7

    # Calculate the number of weeks to reach the goal
    weeks_to_reach_goal = goal_days / days_per_week

    # Calculate the additional miles needed each week
    additional_miles_per_week = (total_goal_miles - previous_miles) / weeks_to_reach_goal
    result = additional_miles_per_week
    return result

print(solution())