def solution():
    """Tina makes $18.00 an hour. If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage. If she works 10 hours every day for 5 days, how much money does she make?"""
    # Define the hourly wage and the number of hours worked per day
    hourly_wage = 18
    regular_hours = 8
    overtime_rate = 1.5

    # Calculate the total number of hours worked
    total_hours = 10 * 5

    # Calculate the number of overtime hours worked
    if total_hours > 8 * 5:
        overtime_hours = total_hours - 8 * 5
    else:
        overtime_hours = 0

    # Calculate the total earnings, including overtime
    regular_earnings = hourly_wage * regular_hours * 5
    overtime_earnings = hourly_wage * overtime_rate * overtime_hours
    total_earnings = regular_earnings + overtime_earnings

    # return the result
    result = total_earnings
    return result

print(solution())