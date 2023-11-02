def solution():
    """John plays at the arcade for 3 hours. He uses $.50 for every 6 minutes. How much money did he spend, in dollars?"""
    # Define the number of minutes John played
    minutes_played = 3 * 60

    # Calculate the number of $.50 increments John used
    cost_increments = minutes_played / 6

    # Calculate the total cost in dollars
    total_cost = cost_increments * 0.5

    # Return the result
    result = total_cost
    return result

print(solution())