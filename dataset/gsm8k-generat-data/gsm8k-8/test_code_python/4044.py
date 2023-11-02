def solution():
    # Define hourly rate and overtime rate
    hourly_rate = 10
    overtime_rate = 15

    # Define regular hours and overtime hours
    regular_hours = 40
    overtime_hours = 20

    # Calculate total pay
    total_pay = (regular_hours * hourly_rate) + (overtime_hours * overtime_rate)

    result = total_pay
    return result

print(solution())