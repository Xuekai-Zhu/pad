def solution():
    hourly_rental_rate = 20  # James rents his car out for $20 an hour
    rental_hours_per_day = 8  # James rents his car out for 8 hours per day
    rental_days_per_week = 4  # James rents his car out for 4 days per week

    # Calculate the total amount James makes per week
    total_weekly_earnings = hourly_rental_rate * rental_hours_per_day * rental_days_per_week
    result = total_weekly_earnings
    return result

print(solution())