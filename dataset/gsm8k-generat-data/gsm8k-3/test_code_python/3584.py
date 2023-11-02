def solution():
    """Mary earns $20 washing cars and $40 walking dogs each month. If she puts half of that money away each month how long would it take her to save $150?"""
    # Define Mary's earnings for each activity
    CAR_WASH_EARNINGS = 20
    DOG_WALK_EARNINGS = 40

    # Calculate Mary's monthly savings
    total_earnings = CAR_WASH_EARNINGS + DOG_WALK_EARNINGS
    monthly_savings = total_earnings / 2

    # Calculate the number of months needed to save $150
    months_needed = 150 / monthly_savings

    # Display the result
    result = months_needed
    return result

print(solution())