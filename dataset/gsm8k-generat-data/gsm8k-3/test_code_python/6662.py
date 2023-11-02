def solution():
    """Queenie earns $150 a day as a part-time clerk. She earns an additional $5 per hour as overtime pay. How much will Queenie receive for working 5 days with 4 hours overtime?"""
    # Define Queenie's regular rate and overtime rate
    REGULAR_RATE = 150
    OVERTIME_RATE = 5

    # Get the number of days worked and hours of overtime worked
    days_worked = 5
    overtime_hours = 4

    # Calculate Queenie's earnings
    regular_earnings = days_worked * REGULAR_RATE
    overtime_earnings = overtime_hours * OVERTIME_RATE
    total_earnings = regular_earnings + overtime_earnings

    # Display Queenie's earnings
    result = total_earnings
    return result

print(solution())