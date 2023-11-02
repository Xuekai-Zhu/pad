def solution():
    """Matt and Blake want to watch every episode of the show The Office. There are 201 episodes. If they watch 1 episode every Monday and 2 episodes every Wednesday each week, how many weeks will it take them to watch the whole series?"""
    # Define the number of episodes and the number of episodes they can watch each week
    total_episodes = 201
    episodes_per_week = 1 + 2*2

    # Calculate the number of weeks it will take to watch all the episodes
    weeks = total_episodes / episodes_per_week

    # Round up to the nearest whole number of weeks, using the ceil function from the math module
    import math
    weeks = math.ceil(weeks)

    # return the result
    result = weeks
    return result

print(solution())