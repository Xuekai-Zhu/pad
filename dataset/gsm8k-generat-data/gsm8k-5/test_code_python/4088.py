def solution():
    regular_rate = 20  # Bill gets paid $20 per hour for the first 40 hours
    overtime_rate = regular_rate * 2  # After 40 hours, he gets paid double

    hours_worked = 50  # Bill worked for 50 hours

    if hours_worked <= 40:
        total_pay = hours_worked * regular_rate
    else:
        regular_pay = 40 * regular_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay

    result = total_pay
    return result

print(solution())