def solution():
    regular_rate = 5  # Bob gets paid $5 per regular hour
    overtime_rate = 6  # Bob gets paid $6 per overtime hour
    regular_hours = 40  # Bob works 40 regular hours per week
    total_pay = 0  # initialize total pay to 0

    # Calculate pay for the first week
    if 44 > regular_hours:
        overtime_hours = 44 - regular_hours  # Bob worked 4 overtime hours in the first week
        total_pay += (regular_hours * regular_rate) + (overtime_hours * overtime_rate)
    else:
        total_pay += 44 * regular_rate

    # Calculate pay for the second week
    if 48 > regular_hours:
        overtime_hours = 48 - regular_hours  # Bob worked 8 overtime hours in the second week
        total_pay += (regular_hours * regular_rate) + (overtime_hours * overtime_rate)
    else:
        total_pay += 48 * regular_rate

    result = total_pay
    return result

print(solution())