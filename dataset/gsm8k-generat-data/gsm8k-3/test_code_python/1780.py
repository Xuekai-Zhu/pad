def solution():
    """Faith is getting paid $13.50 per hour. She normally works 8 hours a day, 5 days a week, plus 2 hours of overtime per day. How much will she earn by the end of the week?"""
    # Define Faith's regular hourly rate and overtime rate
    REGULAR_RATE = 13.5
    OVERTIME_RATE = REGULAR_RATE * 1.5

    # Calculate Faith's total hours worked, regular pay, and overtime pay
    total_hours = 8 * 5 + 2 * 5
    regular_pay = 8 * 5 * REGULAR_RATE
    overtime_pay = 2 * 5 * OVERTIME_RATE

    # Calculate Faith's total earnings for the week
    total_earnings = regular_pay + overtime_pay

    # Display Faith's total earnings for the week
    result = total_earnings
    return result

print(solution())