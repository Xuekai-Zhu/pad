def solution():
    hours_april = 6 * 30  # Total hours worked in April
    hours_june = 5 * 30  # Total hours worked in June
    hours_september = 8 * 30  # Total hours worked in September

    total_hours_worked = hours_april + hours_june + hours_september  # Calculate the total hours worked in all 3 months

    average_hours_per_month = total_hours_worked / 3  # Calculate the average hours worked per month

    result = average_hours_per_month
    return result

print(solution())