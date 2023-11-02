def solution():
    """Hallie is working as a waitress for $10/hour. On Monday, she works for 7 hours, and she receives $18 in tips. On Tuesday she works for 5 hours, and she receives $12 in tips. On Wednesday she works for 7 hours, and she receives $20 in tips. How much money does she earn in total from Monday to Wednesday?"""
    # Define the hourly wage
    hourly_wage = 10

    # Calculate the total earnings on Monday
    monday_earnings = (7 * hourly_wage) + 18

    # Calculate the total earnings on Tuesday
    tuesday_earnings = (5 * hourly_wage) + 12

    # Calculate the total earnings on Wednesday
    wednesday_earnings = (7 * hourly_wage) + 20

    # Calculate the total earnings for all three days
    total_earnings = monday_earnings + tuesday_earnings + wednesday_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())