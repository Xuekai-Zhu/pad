def solution():
    """Alfonso earns $6 each day walking his aunt's dog. He is saving to buy a mountain bike helmet for $340. Currently, he already has $40. If he walks his aunt's dog 5 days a week, in how many weeks should Alfonso work to buy his mountain bike?"""
    # Define the amount he needs to save
    total_savings_needed = 340 - 40

    # Define the amount he can save each week
    weekly_savings = 6 * 5

    # Calculate the number of weeks needed to save enough money
    weeks_needed = total_savings_needed / weekly_savings

    # Round up to the nearest week
    weeks_needed = math.ceil(weeks_needed)

    # Return the result
    result = weeks_needed
    return result

print(solution())