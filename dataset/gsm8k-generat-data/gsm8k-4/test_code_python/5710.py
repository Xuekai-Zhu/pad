def solution():
    """Peter has a plan to take his family on a vacation to Germany. He needs $5,000 to cover all the spending for the travel, and he has $2,900 in savings right now. If he can save up $700 each month, how many months does he need to wait to reach his goal?"""
    # Define the total cost of the trip and Peter's current savings
    total_cost = 5000
    savings = 2900

    # Define Peter's monthly savings and initialize the month counter
    monthly_savings = 700
    months = 0

    # Calculate the number of months needed to reach the total cost
    while savings < total_cost:
        # Increment the month counter
        months += 1

        # Add Peter's monthly savings to his total savings
        savings += monthly_savings

    # Return the result
    result = months
    return result

print(solution())