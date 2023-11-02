def solution():
    weekly_savings = 50  # Jaime saves $50 per week
    lunch_spending = 46  # Jaime spends $46 on lunch every 2 weeks
    target_savings = 135  # Jaime wants to save $135 in total

    # Calculate the number of weeks it will take Jaime to save enough for the lunch
    weeks_for_lunch = lunch_spending / weekly_savings * 2

    # Calculate the total number of weeks it will take Jaime to reach her target savings
    total_weeks = (target_savings + lunch_spending) / weekly_savings + weeks_for_lunch
    result = total_weeks
    return result

print(solution())