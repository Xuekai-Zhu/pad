def solution():
    """Janice gets paid $10 an hour for the first 40 hours she works each week, and $15 each hour of overtime after that. If Janice works 60 hours one week, how much money does she make?"""
    # Define the regular hourly rate and the overtime hourly rate
    REGULAR_RATE = 10
    OVERTIME_RATE = 15

    # Get the number of hours Janice worked
    hours_worked = 60

    # Calculate Janice's earnings
    if hours_worked <= 40:
        earnings = hours_worked * REGULAR_RATE
    else:
        regular_hours = 40
        overtime_hours = hours_worked - regular_hours
        overtime_earnings = overtime_hours * OVERTIME_RATE
        regular_earnings = regular_hours * REGULAR_RATE
        earnings = regular_earnings + overtime_earnings

    # Display Janice's earnings
    result = earnings
    return result

print(solution())