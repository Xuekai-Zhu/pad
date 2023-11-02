def solution():
    # Define the hourly rate and number of hours worked each day
    hourly_rate = 2
    hours_per_day = 4

    # Calculate the total number of hours worked in 4 weeks
    total_hours = hours_per_day * 3 * 4

    # Calculate the total earnings based on the hourly rate and total hours worked
    total_earnings = hourly_rate * total_hours
    result = total_earnings
    return result

print(solution())