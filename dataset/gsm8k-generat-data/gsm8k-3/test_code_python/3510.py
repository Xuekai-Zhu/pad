def solution():
    """Alfred likes to save $1,000.00 over 12 months for his Christmas shopping.  He has $100.00 left over from last year's holiday to put towards this year's goal.  How much money does Alfred now need to save each month in order to reach his goal in 12 months?"""
    # Define Alfred's goal amount and starting balance
    GOAL_AMOUNT = 1000
    STARTING_BALANCE = 100

    # Calculate the amount still needed to reach the goal
    amount_needed = GOAL_AMOUNT - STARTING_BALANCE

    # Calculate the monthly amount needed to reach the goal
    monthly_amount = amount_needed / 12

    # Round the monthly amount to two decimal places
    monthly_amount = round(monthly_amount, 2)

    # Display the monthly amount needed
    result = monthly_amount
    return result

print(solution())