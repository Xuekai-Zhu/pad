def solution():
    """Mitch is a freelancer, she works 5 hours every day from Monday to Friday and 3 hours every Saturday and Sunday. 
    If she earns $3 per hour and earns double on weekends, how much does she earn every week?"""
    # Define the hourly rate and weekend rate multiplier
    HOURLY_RATE = 3
    WEEKEND_RATE_MULTIPLIER = 2

    # Calculate Mitch's earnings for weekdays
    weekday_hours = 5 * 5  # 5 hours per day for 5 days
    weekday_earnings = weekday_hours * HOURLY_RATE

    # Calculate Mitch's earnings for weekends
    weekend_hours = 3 * 2  # 3 hours per day for 2 days
    weekend_earnings = weekend_hours * HOURLY_RATE * WEEKEND_RATE_MULTIPLIER

    # Calculate Mitch's total earnings for the week
    total_earnings = weekday_earnings + weekend_earnings

    # Display Mitch's total earnings for the week
    result = total_earnings
    return result

print(solution())