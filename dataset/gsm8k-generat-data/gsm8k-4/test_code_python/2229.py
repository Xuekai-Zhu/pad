def solution():
    """Zainab earns $2 an hour passing out flyers at the town square. She passes out flyers on Monday, Wednesday, and Saturday each week, for 4 hours at a time. After passing out flyers for 4 weeks, how much money will Zainab earn?"""
    # Define the hourly wage and number of hours worked each week
    hourly_wage = 2
    hours_per_week = 12

    # Calculate the total number of hours worked over 4 weeks
    total_hours = hours_per_week * 4

    # Calculate the total earnings
    total_earnings = total_hours * hourly_wage

    # Return the result
    result = total_earnings
    return result

print(solution())