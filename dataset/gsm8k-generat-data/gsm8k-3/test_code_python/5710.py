def solution():
    """Peter has a plan to take his family on a vacation to Germany. He needs $5,000 to cover all the spending for the travel, and he has $2,900 in savings right now. If he can save up $700 each month, how many months does he need to wait to reach his goal?"""
    # Define the goal amount and current savings
    GOAL_AMOUNT = 5000
    CURRENT_SAVINGS = 2900

    # Define the amount saved per month
    AMOUNT_SAVED_PER_MONTH = 700

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = GOAL_AMOUNT - CURRENT_SAVINGS

    # Calculate the number of months needed to save up the remaining amount
    months_needed = remaining_amount / AMOUNT_SAVED_PER_MONTH
    months_needed = int(months_needed) + (months_needed % 1 > 0)

    # Display the number of months needed
    result = months_needed
    return result

print(solution())