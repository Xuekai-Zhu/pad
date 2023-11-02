def solution():
    """Sandy earns $15 per hour. She worked 10 hours on Friday with her best friend, 6 hours on Saturday alone and 14 hours on Sunday with her other co-workers. How much money did Sandy earn in all on Friday, Saturday and Sunday?"""
    # Define the hourly wage and the number of hours worked each day
    HOURLY_WAGE = 15
    FRIDAY_HOURS = 10
    SATURDAY_HOURS = 6
    SUNDAY_HOURS = 14

    # Calculate the total earnings for each day
    friday_earnings = FRIDAY_HOURS * HOURLY_WAGE
    saturday_earnings = SATURDAY_HOURS * HOURLY_WAGE
    sunday_earnings = SUNDAY_HOURS * HOURLY_WAGE

    # Calculate the total earnings for all three days
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())