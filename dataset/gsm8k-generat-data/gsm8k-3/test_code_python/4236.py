def solution():
    """John plays at the arcade for 3 hours.  He uses $.50 for every 6 minutes.  How much money did he spend, in dollars?"""
    # Define the cost per 6 minutes
    COST_PER_6_MIN = 0.5

    # Convert 3 hours to minutes
    play_time = 3 * 60

    # Calculate the total number of 6-minute increments played
    increments_played = play_time // 6

    # Calculate the total cost
    total_cost = increments_played * COST_PER_6_MIN

    # Display the total cost
    result = total_cost
    return result

print(solution())