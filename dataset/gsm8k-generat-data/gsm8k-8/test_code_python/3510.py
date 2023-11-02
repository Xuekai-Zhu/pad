def solution():
    # Define Alfred's goal and starting amount
    goal_amount = 1000
    starting_amount = 100

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = goal_amount - starting_amount

    # Calculate the amount needed to save each month
    monthly_savings = remaining_amount / 12
    result = monthly_savings
    return result

print(solution())