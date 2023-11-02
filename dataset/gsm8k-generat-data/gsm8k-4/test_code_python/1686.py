def solution():
    """Every day, Bob logs 10 hours of work in his office. If he works for five days a week, calculate the total number of hours he logs in a month."""
    # Calculate the total number of hours Bob works in a week
    weekly_hours = 10 * 5

    # Calculate the total number of hours Bob works in a month
    monthly_hours = weekly_hours * 4

    # Return the result
    result = monthly_hours
    return result

print(solution())