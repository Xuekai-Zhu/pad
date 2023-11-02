def solution():
    """Faith is getting paid $13.50 per hour. She normally works 8 hours a day, 5 days a week, plus 2 hours of overtime per day. How much will she earn by the end of the week?"""
    # Define Faith's hourly rate and daily working hours
    hourly_rate = 13.50
    regular_hours = 8
    overtime_hours = 2

    # Calculate Faith's regular earnings for a day
    regular_earnings = hourly_rate * regular_hours

    # Calculate Faith's overtime earnings for a day
    overtime_earnings = hourly_rate * 1.5 * overtime_hours

    # Calculate Faith's total earnings for a day
    total_earnings = regular_earnings + overtime_earnings

    # Calculate Faith's total earnings for a week
    weekly_earnings = total_earnings * 5

    result = weekly_earnings
    return result

print(solution())