def solution():
    """Brady worked 6 hours every day in April. He worked 5 hours every day in June and 8 hours every day in September. What is the average amount of hours that Brady worked per month in those 3 months?"""
    # Define the number of hours worked in each month
    hours_april = 6 * 30
    hours_june = 5 * 30
    hours_september = 8 * 30

    # Calculate the total number of hours worked in the 3 months
    total_hours = hours_april + hours_june + hours_september

    # Calculate the average number of hours worked per month
    average_hours = total_hours / 3

    # return the result
    result = average_hours
    return result

print(solution())