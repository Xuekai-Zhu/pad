def solution():
    """Brady worked 6 hours every day in April. He worked 5 hours every day in June and 8 hours every day in September. What is the average amount of hours that Brady worked per month in those 3 months?"""
    # Define the number of days in each month
    DAYS_IN_APRIL = 30
    DAYS_IN_JUNE = 30
    DAYS_IN_SEPTEMBER = 30

    # Define the number of hours worked per day in each month
    HOURS_IN_APRIL = 6
    HOURS_IN_JUNE = 5
    HOURS_IN_SEPTEMBER = 8

    # Calculate the total number of hours worked in the three months
    total_hours = (DAYS_IN_APRIL * HOURS_IN_APRIL) + (DAYS_IN_JUNE * HOURS_IN_JUNE) + (DAYS_IN_SEPTEMBER * HOURS_IN_SEPTEMBER)

    # Calculate the average number of hours worked per month
    average_hours = total_hours / 3

    # Display the average number of hours worked per month
    result = average_hours
    return result

print(solution())