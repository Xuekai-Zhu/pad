def solution():
    total_hours = 1500  # Sangita needs to fly a total of 1500 hours
    completed_hours = 50 + 9 + 121  # Sangita has already completed 50 hours of day flying, 9 hours of night flying, and 121 hours flying cross-country
    remaining_hours = total_hours - completed_hours  # Sangita needs to fly the remaining hours
    six_months = 6  # Sangita has exactly 6 months to meet her goal

    # Calculate the number of hours Sangita must fly per month to meet her goal
    hours_per_month = remaining_hours / six_months
    result = hours_per_month
    return result

print(solution())