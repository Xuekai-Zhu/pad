def solution():
    """Queenie earns $150 a day as a part-time clerk. She earns an additional $5 per hour as overtime pay. How much will Queenie receive for working 5 days with 4 hours overtime?"""
    # Define the daily salary and overtime pay rate
    DAILY_SALARY = 150
    OVERTIME_PAY = 5

    # Calculate the total hours worked
    total_hours = 5 * 8 + 4

    # Calculate the total earnings, including overtime pay
    total_earnings = 5 * DAILY_SALARY + 4 * OVERTIME_PAY

    # return the result
    result = total_earnings
    return result

print(solution())