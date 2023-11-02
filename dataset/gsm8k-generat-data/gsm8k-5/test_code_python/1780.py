def solution():
    hourly_rate = 13.50  # Faith's hourly rate is $13.50
    regular_hours = 8 * 5  # Faith works 8 hours a day, 5 days a week
    overtime_hours = 2 * 5  # Faith works 2 hours of overtime per day, 5 days a week

    # Calculate Faith's regular pay
    regular_pay = hourly_rate * regular_hours

    # Calculate Faith's overtime pay
    overtime_pay = hourly_rate * 1.5 * overtime_hours

    # Calculate Faith's total earnings for the week
    total_earnings = regular_pay + overtime_pay
    result = total_earnings
    return result

print(solution())