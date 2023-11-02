def solution():
    """Janice gets paid $10 an hour for the first 40 hours she works each week, and $15 each hour of overtime after that. If Janice works 60 hours one week, how much money does she make?"""
    # Define the hourly pay rates and the number of hours worked
    REGULAR_RATE = 10
    OVERTIME_RATE = 15
    REGULAR_HOURS = 40
    total_hours = 60

    # Calculate the regular pay and overtime pay
    if total_hours <= REGULAR_HOURS:
        regular_pay = total_hours * REGULAR_RATE
        overtime_pay = 0
    else:
        regular_pay = REGULAR_HOURS * REGULAR_RATE
        overtime_pay = (total_hours - REGULAR_HOURS) * OVERTIME_RATE

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay

    # return the result
    result = total_pay
    return result

print(solution())