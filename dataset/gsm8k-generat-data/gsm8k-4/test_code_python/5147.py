def solution():
    """Rachel makes $12.00 as a waitress in a coffee shop. In one hour, she serves 20 different people and they all leave her a $1.25 tip. How much money did she make in that hour?"""
    # Define the hourly wage and the tip amount
    hourly_wage = 12.00
    tip_amount = 1.25

    # Calculate the total amount earned from tips
    tip_earnings = 20 * tip_amount

    # Calculate the total earnings for the hour
    total_earnings = hourly_wage + tip_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())