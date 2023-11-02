def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    # Define the amount John puts in his piggy bank each month
    MONTHLY_SAVINGS = 25

    # Calculate the total savings over 2 years
    total_savings = MONTHLY_SAVINGS * 24

    # Subtract the amount John spent on his car repair
    remaining_savings = total_savings - 400

    # Display the remaining savings
    result = remaining_savings
    return result

print(solution())