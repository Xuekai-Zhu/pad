def solution():
    """Hallie is working as a waitress for $10/hour. On Monday, she works for 7 hours, and she receives $18 in tips. On Tuesday she works for 5 hours, and she receives $12 in tips. On Wednesday she works for 7 hours, and she receives $20 in tips. How much money does she earn in total from Monday to Wednesday?"""
    # Define Hallie's hourly pay rate
    PAY_RATE = 10

    # Calculate Hallie's earnings for Monday
    monday_earnings = (PAY_RATE * 7) + 18

    # Calculate Hallie's earnings for Tuesday
    tuesday_earnings = (PAY_RATE * 5) + 12

    # Calculate Hallie's earnings for Wednesday
    wednesday_earnings = (PAY_RATE * 7) + 20

    # Calculate Hallie's total earnings for the three days
    total_earnings = monday_earnings + tuesday_earnings + wednesday_earnings

    # Display Hallie's total earnings
    result = total_earnings
    return result

print(solution())