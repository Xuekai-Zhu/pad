def solution():
    """Mitch is a freelancer, she works 5 hours every day from Monday to Friday and 3 hours every Saturday and Sunday. If she earns $3 per hour and earns double on weekends, how much does she earn every week?"""
    # Define the hourly rate and the number of hours worked each day
    HOURLY_RATE = 3
    WEEKDAY_HOURS = 5
    WEEKEND_HOURS = 3
    WEEKEND_RATE = HOURLY_RATE * 2

    # Calculate the total earnings for the weekdays and weekends separately
    weekday_earnings = WEEKDAY_HOURS * HOURLY_RATE * 5
    weekend_earnings = (WEEKEND_HOURS * WEEKEND_RATE * 2)

    # Calculate the total earnings for the week
    total_earnings = weekday_earnings + weekend_earnings

    # return the result
    result = total_earnings
    return result

print(solution())