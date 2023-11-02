def solution():
    # Calculate the total number of episodes they need to watch
    total_episodes = 201

    # Calculate the number of episodes they can watch each week
    episodes_per_week = 1 + 2*2

    # Calculate the number of weeks it will take to watch the whole series
    weeks_to_watch = total_episodes / episodes_per_week

    # Return the result
    result = weeks_to_watch
    return result

print(solution())