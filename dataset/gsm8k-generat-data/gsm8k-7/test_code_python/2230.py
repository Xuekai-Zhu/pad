def solution():
    daily_earnings = 6
    target_cost = 340
    current_savings = 40
    days_per_week = 5

    # Calculate how much Alfonso needs to save
    remaining_cost = target_cost - current_savings

    # Calculate how many days Alfonso needs to work to save up
    total_days = remaining_cost / daily_earnings

    # Calculate how many weeks Alfonso needs to work
    weeks_to_save = total_days / days_per_week
    result = weeks_to_save
    return result

print(solution())