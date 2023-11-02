def solution():
    """Edric's monthly salary is $576. If he works 8 hours a day for 6 days a week, how much is his hourly rate?"""
    # Define the total number of work hours in a month
    work_hours_per_week = 8 * 6
    work_hours_per_month = work_hours_per_week * 4

    # Calculate the hourly rate
    hourly_rate = 576 / work_hours_per_month

    # Return the result
    result = hourly_rate
    return result

print(solution())