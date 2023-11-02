def solution():
    """John plays at the arcade for 3 hours. He uses $.50 for every 6 minutes. How much money did he spend, in dollars?"""
    play_time = 3 * 60 # convert hours to minutes
    cost_per_minute = 0.50 / 6
    total_cost = play_time * cost_per_minute
    result = total_cost
    return result

print(solution())