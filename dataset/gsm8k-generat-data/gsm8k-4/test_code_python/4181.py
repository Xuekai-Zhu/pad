def solution():
    """Hannah wants to save $80 for five weeks. In the first week, she saved $4 and she plans to save twice as much as her savings as the previous week. How much will she save in the fifth week to reach her goal?"""
    # Define the goal amount to save and the initial savings in the first week
    GOAL_AMOUNT = 80
    first_week_savings = 4

    # Define a variable to keep track of the current week
    current_week = 1

    # Initialize a variable to keep track of the total savings
    total_savings = first_week_savings

    # Loop through the remaining weeks and calculate savings
    while current_week < 5:
        # Increment the current week counter
        current_week += 1

        # Calculate the savings for the current week
        current_week_savings = 2 * total_savings

        # Add the savings to the total
        total_savings += current_week_savings

    # Calculate the amount needed to reach the goal
    amount_needed = GOAL_AMOUNT - total_savings

    # Calculate the savings for the fifth week to reach the goal
    fifth_week_savings = amount_needed / (2**3)

    result = fifth_week_savings
    return result

print(solution())