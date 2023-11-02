def solution():
    total_required_hours = 1500
    completed_day_flying = 50
    completed_night_flying = 9
    completed_cross_country_flying = 121
    time_period_in_months = 6

    # Calculate the total completed hours of flying
    total_completed_hours = completed_day_flying + completed_night_flying + completed_cross_country_flying

    # Calculate the remaining hours of flying required to meet the goal
    remaining_hours = total_required_hours - total_completed_hours

    # Calculate the required hours of flying per month
    hours_per_month = remaining_hours / time_period_in_months
    result = hours_per_month
    return result

print(solution())