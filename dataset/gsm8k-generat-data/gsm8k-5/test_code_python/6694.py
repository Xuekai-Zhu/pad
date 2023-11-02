def solution():
    days_worked = 10  # John has been working for 10 days
    total_earned = 250  # John has earned $250 so far
    daily_earnings = total_earned / days_worked  # John's daily earnings

    # Calculate how much John needs to earn to make twice his current amount
    double_earned = total_earned * 2
    remaining_amount = double_earned - total_earned

    # Calculate how many days John needs to work to make the remaining amount
    days_to_double = remaining_amount / daily_earnings
    result = int(days_to_double)  # Round down to the nearest whole day
    return result

print(solution())