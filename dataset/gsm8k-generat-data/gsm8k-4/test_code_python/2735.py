def solution():
    """Bob gets paid $5 an hour for the regular hours he works and $6 an hour for any overtime hours he works. All hours over 40 in a week are considered overtime. If Bob works 44 hours in the first week and 48 hours in the second week, how much did he make?"""
    # Define the regular pay rate and the overtime pay rate
    REGULAR_RATE = 5
    OVERTIME_RATE = 6

    # Define the number of hours in a regular work week and the overtime threshold
    REGULAR_WEEK_HOURS = 40
    OVERTIME_THRESHOLD = 40

    # Calculate the pay for the first week
    if 44 <= REGULAR_WEEK_HOURS:
        regular_pay = REGULAR_WEEK_HOURS * REGULAR_RATE
        overtime_pay = (44 - REGULAR_WEEK_HOURS) * OVERTIME_RATE
    else:
        regular_pay = 44 * REGULAR_RATE
        overtime_pay = 0
    week1_pay = regular_pay + overtime_pay

    # Calculate the pay for the second week
    if 48 <= REGULAR_WEEK_HOURS:
        regular_pay = REGULAR_WEEK_HOURS * REGULAR_RATE
        overtime_pay = (48 - REGULAR_WEEK_HOURS) * OVERTIME_RATE
    else:
        regular_pay = 48 * REGULAR_RATE
        overtime_pay = 0
    week2_pay = regular_pay + overtime_pay

    # Calculate the total pay for both weeks
    total_pay = week1_pay + week2_pay

    # return the result
    result = total_pay
    return result

print(solution())