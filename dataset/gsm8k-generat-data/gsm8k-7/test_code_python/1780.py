def solution():
    hourly_rate = 13.5
    regular_hours = 8 * 5
    overtime_hours = 2 * 5
    total_hours = regular_hours + overtime_hours
    weekly_pay = total_hours * hourly_rate
    result = weekly_pay
    return result

print(solution())