def solution():
    days_worked = 10
    total_earned = 250
    target_earned = 500

    # Calculate John's daily earnings
    daily_earnings = total_earned / days_worked

    # Calculate how many more days John needs to work to reach his target earnings
    days_needed = (target_earned - total_earned) / daily_earnings

    # Round up to the nearest whole day
    days_needed = int(days_needed) + 1

    result = days_needed
    return result

print(solution())