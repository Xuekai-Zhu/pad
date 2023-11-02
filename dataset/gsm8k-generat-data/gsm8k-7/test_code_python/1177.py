def solution():
    rental_rate = 20
    hours_per_day = 8
    days_per_week = 4

    # Calculate the total hours rented per week
    total_hours = hours_per_day * days_per_week

    # Calculate the total amount earned per week
    total_earned = total_hours * rental_rate
    result = total_earned
    return result

print(solution())